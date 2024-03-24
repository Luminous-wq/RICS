import json

import networkx as nx
import time
import numpy as np
import pymetis

R_MAX = 3
d = 5


def construct_index(Graph: nx.Graph) -> list:

    nodes = list(Graph.nodes())
    num_partition = 16
    start_time = time.time()
    root_node = root_tree(node_list=nodes, num_partition=num_partition, level=0, Graph=Graph)
    print("Tree index is finished")
    print("Construct cost time:{}".format(time.time()-start_time))
    return root_node


def partition_blocks(nodelist: list, Graph: nx.Graph, num_partition: int) -> list:
    # nodelist = np.array(nodelist)
    # print(nodelist)
    # print(type(nodelist))
    G = Graph.subgraph(nodelist)
    node_index_map = {node: i for i, node in enumerate(nodelist)}
    rebuilt_subgraph = nx.relabel_nodes(G, node_index_map)
    adjacency_list = []
    for node in range(len(nodelist)):
        neighbors = []
        # 检查邻居节点是否在子图中，只有在子图中的节点才会被添加到邻接表中
        for neighbor in rebuilt_subgraph.neighbors(node):
            if neighbor in node_index_map:
                neighbors.append(int(node_index_map[neighbor]))
        adjacency_list.append(np.array(neighbors))
    edgecuts, partitions = pymetis.part_graph(num_partition, adjacency=adjacency_list)
    partition_nodes = [[] for _ in range(num_partition)]
    for node, partition in enumerate(partitions):
        original_node = nodelist[node]
        partition_nodes[partition].append(str(original_node))
    # adjacency_list = [np.array([int(node) for node in list(Graph.neighbors(node))]) for node in nodelist]
    # adjacency_list = [np.array([int(node) for node in list(G.neighbors(node))]) for node in G.nodes()]
    # print(adjacency_list)
    # edgecuts, partitions = pymetis.part_graph(num_partition, adjacency=adjacency_list)
    #
    # partition_nodes = [[] for _ in range(num_partition)]
    # for node, partition in enumerate(partitions):
    #     partition_nodes[partition].append(str(node))

    # partition_nodes: [[p1], [p2], [p3]...]
    return partition_nodes


def root_tree(node_list: list, num_partition: int, level: int, Graph: nx.Graph):
    if len(node_list) < num_partition:
        # print(node_list[0])
        # print(Graph.nodes[node_list[0]])
        return [
            {
                "P": node,  # node index
                "LD": Graph.nodes[node]["dist"],
                "UD": Graph.nodes[node]["dist"],
                # "D": Graph.nodes[node]["dist"],  # node distance list
                "R": Graph.nodes[node]["Aux"],  # node synopsis
                "T": True,  # leaf node
                "L": level  # level
            } for node in node_list
        ]
    # print(level)
    # print(node_list)

    node_partition_blocks = partition_blocks(node_list, Graph, num_partition)

    aggregated_child_entry_list = []

    aggregated_synopsis_d = [{
            "lb_dist": [0 for _ in range(5)],
            "ub_dist": [0 for _ in range(5)]
        }]
    aggregated_synopsis_aux = [{
            "BV_r": 0,
            "ub_sup_r": 0,
            "ub_inf_r": 0
        } for _ in range(3)]
    aggregated_synopsis = []
    aggregated_synopsis.append(aggregated_synopsis_d)
    aggregated_synopsis.append(aggregated_synopsis_aux)
    # aggregated_synopsis.append([{
    #                                "BV_r": 0,
    #                                "ub_sup_r": 0,
    #                                "ub_inf_r": 0
    #                            } for _ in range(R_MAX)])
    for i in range(num_partition):
        partition_node_array = node_partition_blocks[i]
        # print(partition_node_array)
        child_entry_list = root_tree(partition_node_array, num_partition, level+1, Graph)

        for i_d in range(d):
            for child_entry in child_entry_list:
                # print(type(aggregated_synopsis[0]["lb_dist"][i_d]))
                # print(child_entry)
                if aggregated_synopsis[0][0]["lb_dist"][i_d] > child_entry["LD"][i_d]:
                    aggregated_synopsis[0][0]["lb_dist"][i_d] = child_entry["LD"][i_d]
                if aggregated_synopsis[0][0]["ub_dist"][i_d] < child_entry["UD"][i_d]:
                    aggregated_synopsis[0][0]["ub_dist"][i_d] = child_entry["UD"][i_d]

        for r in range(R_MAX):
            for child_entry in child_entry_list:
                # print("aggregated_synopsis:{}".format(aggregated_synopsis))
                # print("child_entry:{}".format(child_entry))
                # print(aggregated_synopsis[1][r]["BV_r"])
                # print(int(child_entry['R'][r]["BV_r"]))
                aggregated_synopsis[1][r]["BV_r"] = aggregated_synopsis[1][r]["BV_r"] | int(child_entry['R'][r]["BV_r"])
                if aggregated_synopsis[1][r]["ub_sup_r"] < child_entry["R"][r]["ub_sup_r"]:
                    aggregated_synopsis[1][r]["ub_sup_r"] = child_entry["R"][r]["ub_sup_r"]
                if aggregated_synopsis[1][r]["ub_inf_r"] < child_entry["R"][r]["ub_inf_r"]:
                    aggregated_synopsis[1][r]["ub_inf_r"] = child_entry["R"][r]["ub_inf_r"]

                # aggregated_synopsis[r]["BV_r"] = aggregated_synopsis[r]["BV_r"] | int(child_entry['R'][r]["BV_r"])
                # if aggregated_synopsis[r]["ub_sup_r"] < child_entry["R"][r]["ub_sup_r"]:
                #     aggregated_synopsis[r]["ub_sup_r"] = child_entry["R"][r]["ub_sup_r"]
                # if aggregated_synopsis[r]["ub_inf_r"] < child_entry["R"][r]["ub_inf_r"]:
                #     aggregated_synopsis[r]["ub_inf_r"] = child_entry["R"][r]["ub_inf_r"]

        aggregated_child_entry_list.append(child_entry_list)
    return [
        {
            "P": child_entry_list,  # partition
            "LD": aggregated_synopsis[0][0]["lb_dist"],
            "UD": aggregated_synopsis[0][0]["ub_dist"],
            "R": aggregated_synopsis[1],  # aggregated synopsis
            "T": False,  # leaf node
            "L": level
        } for child_entry_list in aggregated_child_entry_list
    ]


def save_index_as_json(index, filename):
    with open(filename, 'w') as file:
        json.dump(index, file)


def load_index_from_json(filename):
    with open(filename, 'r') as file:
        index = json.load(file)
    return index


def print_index_tree(node, depth=0):
    if isinstance(node, list):
        for subnode in node:
            print_index_tree(subnode, depth)
    elif isinstance(node, dict):
        print("  " * depth + "Node:")
        print("  " * (depth + 1) + f"P: {node['P']}")
        print("  " * (depth + 1) + f"R: {node['R']}")
        print("  " * (depth + 1) + f"T: {node['T']}")
        if 'P' in node:
            print_index_tree(node['P'], depth + 1)


def count_nodes_per_level(root, level_counts=None, level=0):
    # if level_counts is None:
    #     level_counts = {}
    # if level not in level_counts:
    #     level_counts[level] = 0
    # level_counts[level] += 1
    #
    # if isinstance(node, list):
    #     for subnode in node:
    #         count_nodes_per_level(subnode, level + 1, level_counts)
    # elif isinstance(node, dict):
    #     if 'P' in node:
    #         count_nodes_per_level(node['P'], level + 1, level_counts)

    if level in level_counts:
        level_counts[level] += len(root)
    else:
        level_counts[level] = len(root)

    for entry in root:
        if not entry['T']:
            child_entry_list = entry['P']
            count_nodes_per_level(child_entry_list, level_counts, level + 1)

    return level_counts


if __name__ == '__main__':
    G = nx.read_gml("Out/pre-compute/synthetic/10000-25032-50-3/G_Aux+.gml")
    # root = construct_index(G)
    # save_index_as_json(root, "index_1w.json")

    # G = nx.read_gml("Out/pre-compute/Facebook/4039-88234-50-3/G_Aux+.gml")
    # root = construct_index(G)
    # save_index_as_json(root, "index_facebook.json")

    # G = nx.read_gml("Out/pre-compute/DBLP/317080-1049866-50-3/G_Aux+.gml")
    # root = construct_index(G)
    # save_index_as_json(root, "index_dblp.json")

    # G = nx.read_gml("Out/pre-compute/Amazon/334863-925872-50-3/G_Aux+.gml")
    # root = construct_index(G)
    # save_index_as_json(root, "index_amazon.json")

    root = load_index_from_json("index_1w.json")
    # print_index_tree(root)
    # level_counts = {}
    # count_nodes_per_level(root, level_counts, 0)
    # for level, count in level_counts.items():
    #     print(f"Level {level}: {count} nodes")
    for idx, entry in enumerate(root):
        print("idx:{}, key:{}".format(idx, min([abs(entry["LD"][d_i] - G.nodes["6273"]["dist"][d_i]) for d_i in range(d)])))
        # print(entry)