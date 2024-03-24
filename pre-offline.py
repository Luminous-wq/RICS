import networkx as nx
import os
import matplotlib.pyplot as plt
import random
import numpy as np
import time
from Tools.calculate import compute_distance, compute_support
from Tools.aid import create_folder
from Tools.inf_score_u_v import max_weight_path, max_weight_product_path
from Tools.collapse_calculate import collapse_calculate

rand_seed = 2023
random.seed(rand_seed)
np.random.seed(rand_seed)

def get_dataset(dataset, path, keywords_num, keywords_pre_need_num, R_MAX, N_MAX, number_select_pivots):
    G = nx.Graph()
    Graph_dataset = open(path, "r")
    lines = Graph_dataset.readlines()
    for lines in lines:
        list = lines.split()
        node1, node2 = int(list[0]), int(list[1])
        G.add_edge(node1, node2)
        # print(list, type(list))

    graphData_build(G=G,
                    keywords_num=keywords_num,
                    keywords_pre_need_num=keywords_pre_need_num,
                    dataset=dataset,
                    n=number_select_pivots)

    for node_index in G.nodes:
        # print(type(node_index))
        compute_bv_and_ub_sup(node_index=node_index, R_MAX=R_MAX, N_MAX=N_MAX, G=G)
        compute_range(node_index=node_index, G=G, R_MAX=R_MAX)

    folder_name = os.path.join(
        "Out",
        "pre-compute",
        dataset,
        "{}-{}-{}-{}".format(
            G.number_of_nodes(),
            G.number_of_edges(),
            keywords_num,
            keywords_pre_need_num
        )
    )

    create_folder(folder_name)
    initial_directory = os.getcwd()
    os.chdir(folder_name)
    nx.write_gml(G, 'G.gml')
    print(folder_name, 'G.gml', 'saved successfully!')
    os.chdir(initial_directory)

def graphData_build(G: nx.classes.graph.Graph, keywords_num: int, keywords_pre_need_num: int, dataset: str, n: int):
    # print("nodes number: {}".format(G.number_of_nodes()))
    # print("edges number: {}".format(G.number_of_edges()))
    # print(nx.info(G))
    print(G)
    # print(type(G))
    # print(nx.degree(G))
    # print(G.number_of_nodes())
    average_degree = sum(d for v, d in nx.degree(G)) / G.number_of_nodes()
    print("Average degree: {}".format(average_degree))
    print("Max degree: {}".format(max(d for v, d in nx.degree(G))))
    print("Min degree: {}".format(min(d for v, d in nx.degree(G))))

    # TODO: add keywords to vertices
    # the type of node_index is str
    keywords_set = range(0, keywords_num)
    label_cnt = [0] * keywords_num
    for i in G.nodes:

        # every vertex keywords size in (keywords_pre_need_num-1, keywords_pre_need_num+1)
        keywords_need_num = np.random.randint(max(keywords_pre_need_num-1, 1), keywords_pre_need_num+2)
        keywords = random.sample(keywords_set, keywords_need_num)
        G.nodes[i]['keywords'] = keywords
        for keyword in keywords:
            label_cnt[keyword] += 1
        # print(G.nodes[i])
    # print(label_cnt)

    # TODO: vit vector(bin)
    for node in G.nodes:
        bv = 0
        for keyword in G.nodes[node]["keywords"]:
            bv |= (1 << keyword)
        # print(G_data.nodes[node_index]['keywords'])
        # print(bin(bv))
        G.nodes[node]["BV"] = bv
        # print(type(G.nodes[node]["BV"]))

    # TODO: add weight to edges
    for i in G.nodes:
        for neighbor in G.neighbors(i):
            G.edges[i, neighbor]['weight'] = random.uniform(0.5, 0.6)

    # TODO: add distance to nodes
    pivots = random.sample(G.nodes, n)
    print("randomly select pivots: {}".format(pivots))

    # TODO: update pivots by cost model
    for node in G.nodes:
        dist = [0] * n
        for i in range(n):
            dist[i] = compute_distance(G, node, pivots[i])
        G.nodes[node]["dist"] = dist


    folder_name = os.path.join(
        "Out",
        "pre-compute",
        dataset,
        "{}-{}-{}-{}".format(
            G.number_of_nodes(),
            G.number_of_edges(),
            keywords_num,
            keywords_pre_need_num
        )
    )

    create_folder(folder_name)
    initial_directory = os.getcwd()
    os.chdir(folder_name)
    nx.write_gml(G, 'G.gml')
    print(folder_name, 'G.gml', 'saved successfully!')
    os.chdir(initial_directory)

def compute_bv_and_ub_sup(node_index, R_MAX: int, N_MAX: int, G: nx.classes.graph.Graph):
    G.nodes[node_index]["Aux"] = [{
        "BV_r": 0,
        "ub_sup_r": 0,
        "ub_inf_r": 0
        # "inf_r": [0] # community_1-hop boundary influence set
    } for _ in range(R_MAX)]

    # TODO: rmax-hop support compute
    # R_MAX in [1-7]
    r_hop_max = nx.ego_graph(G=G, n=node_index, radius=R_MAX, center=True)
    # print(r_hop_max)
    r_hop_max_support = compute_support(graph=r_hop_max)
    # print(r_hop_max_support.edges[0, 1]["ub_sup"])

    for (u, v) in r_hop_max_support.edges:
        if "ub_sup" not in G.edges[u, v]:
            G.edges[u, v]["ub_sup"] = 0
        if G.edges[u, v]["ub_sup"] < r_hop_max_support.edges[u, v]["ub_sup"]:
            G.edges[u, v]["ub_sup"] = r_hop_max_support.edges[u, v]["ub_sup"]
        # print("[{},{}] sup is {}".format(u, v, G.edges[u, v]["ub_sup"]))


def compute_range(node_index, G: nx.classes.graph.Graph, R_MAX: int):
    for r in range(R_MAX):
        r_hop = nx.ego_graph(G=G, n=node_index, radius=r+1, center=True)
        # print(r_hop)
        for node_j in r_hop.nodes:
            # print(type(G.nodes[node_index]["Aux"][r]["BV_r"]))
            # print(type(r_hop.nodes[node_j]["BV"]))
            # print(r_hop.nodes[node_j]["BV"])
            G.nodes[node_index]["Aux"][r]["BV_r"] = G.nodes[node_index]["Aux"][r]["BV_r"] | int(r_hop.nodes[node_j]["BV"])

        for (u, v) in r_hop.edges:
            if u > v and r_hop.edges[u, v]["ub_sup"] > G.nodes[node_index]["Aux"][r]["ub_sup_r"]:
                G.nodes[node_index]["Aux"][r]["ub_sup_r"] = r_hop.edges[u, v]["ub_sup"]

        # TODO: ub_bound_influence

    print("finish {} node".format(node_index))


if __name__ == '__main__':
    dataset_Amazon = "Amazon"
    dataset_DBLP = "DBLP"
    dataset_eu = "Eu"
    path_Amazon = "Dataset/Amazon/com-amazon.ungraph.txt"
    path_DBLP = "Dataset/DBLP/com-dblp.ungraph.txt"
    path_Eu = "Dataset/Eu-core/email-Eu-core.txt"

    keywords_num = 50
    keywords_pre_need_num = 3
    R_MAX = 3
    N_MAX = 100
    number_select_pivots = 5

    # get_dataset(dataset=dataset_Amazon,
    #             path=path_Amazon,
    #             keywords_num=keywords_num,
    #             keywords_pre_need_num=keywords_pre_need_num,
    #             R_MAX=R_MAX,
    #             N_MAX=N_MAX,
    #             number_select_pivots=number_select_pivots)

    get_dataset(dataset=dataset_DBLP,
                path=path_DBLP,
                keywords_num=keywords_num,
                keywords_pre_need_num=keywords_pre_need_num,
                R_MAX=R_MAX,
                N_MAX=N_MAX,
                number_select_pivots=number_select_pivots)

    # get_dataset(dataset=dataset_eu,
    #             path=path_Eu,
    #             keywords_num=keywords_num,
    #             keywords_pre_need_num=keywords_pre_need_num,
    #             R_MAX=R_MAX,
    #             N_MAX=N_MAX,
    #             number_select_pivots=number_select_pivots)

    # dataset = "Facebook"
    # Graph_dataset = open("Dataset/Facebook/facebook_combined.txt", "r")
    # lines = Graph_dataset.readlines()
    # # print(len(lines))
    # for lines in lines:
    #     list = lines.split()
    #     node1, node2 = int(list[0]), int(list[1])
    #     G.add_edge(node1, node2)
    #     # print(list, type(list))
    #
    # start_time = time.time()
    # graphData_build(G=G,
    #                 keywords_num=keywords_num,
    #                 keywords_pre_need_num=keywords_pre_need_num,
    #                 dataset=dataset,
    #                 n=number_select_pivots)
    # print("build Graph base data cost time:{}".format(time.time() - start_time))
    #
    # G = nx.read_gml("Out/pre-compute/Facebook/4039-88234-50-3/G.gml")
    # for node_index in G.nodes:
    #     # print(type(node_index))
    #     compute_bv_and_ub_sup(node_index=node_index, R_MAX=R_MAX, N_MAX=N_MAX, G=G)
    #     compute_range(node_index=node_index, G=G, R_MAX=R_MAX)
    # folder_name = os.path.join(
    #     "Out",
    #     "pre-compute",
    #     dataset,
    #     "{}-{}-{}-{}".format(
    #         G.number_of_nodes(),
    #         G.number_of_edges(),
    #         keywords_num,
    #         keywords_pre_need_num
    #     )
    # )
    #
    # create_folder(folder_name)
    # initial_directory = os.getcwd()
    # os.chdir(folder_name)
    # nx.write_gml(G, 'G.gml')
    # print(folder_name, 'G.gml', 'saved successfully!')
    # os.chdir(initial_directory)
    # print(G)
    # print(G.nodes["1"]["dist"], G.nodes["1"]["keywords"], G.edges["1", "0"]["weight"])
    # compute_bv_and_ub_sup_and_col(node_index=1, R_MAX=3, N_MAX=50, G=G)
    # print("build offline data Aux cost time:{}".format(time.time() - start_time))

    # test of compute influence inf_score(u, v)
    # u = 1  # 101
    # v = 267  # 2089

    # start_time = time.time()
    # max_weight, path = max_weight_path(graph=G, u=u, v=v)
    # print(f"inf_score({u}, {v}): {max_weight}")
    # print(f"inf_score_path({u}, {v}): {' -> '.join(map(str, path))}")
    # print("compute influence inf_score({}, {}) cost time:{}".format(u, v, time.time() - start_time))
    #
    # start_time = time.time()
    # max_product, max_product_path = max_weight_product_path(G, u, v)
    # print(f"inf_score({u}, {v}): {max_product}")
    # print(f"inf_score_path({u}, {v}): {' -> '.join(map(str, max_product_path))}")
    # print("compute influence inf_score({}, {}) cost time:{}".format(u, v, time.time() - start_time))

    # print(G.edges[1, 0]["weight"]*G.edges[0, 2]["weight"])
    # print(G.edges[2, 0]["weight"] * G.edges[0, 1]["weight"])
    # print(G.edges[101, 0]["weight"]
    #       * G.edges[0, 136]["weight"]
    #       * G.edges[136, 1912]["weight"]
    #       * G.edges[1912, 2089]["weight"])
    # start_time = time.time()
    # for node in G.nodes:
    #     compute_bv_and_ub_sup_and_col(node_index=node, R_MAX=3, N_MAX=50, G=G)
    # print("build offline data Aux cost time:{}".format(time.time()-start_time))
    # compute_bv_and_ub_sup(node_index=1, R_MAX=3, N_MAX=50, G=G)
    # start_time = time.time()
    # compute_range(node_index=1, G=G, R_MAX=3)
    # print("test compute_range cost time:{}".format(time.time() - start_time))

    # G = nx.read_gml("Out/pre-compute/Facebook/4039-88234-50-3/G.gml")
    # print(G)
    # for node in G.nodes:
    #     print(G.nodes[node]["BV"])
    #     print(G.nodes[node]["Aux"])