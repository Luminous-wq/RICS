import multiprocessing
import os

import networkx as nx
import numpy as np

from Tools.aid import create_folder
from Tools.collapse_calculate import collapse_calculate


def calculate(node, G, R_MAX):
    hop = nx.ego_graph(G=G, n=node, radius=R_MAX, center=True)
    r_hop_boundary_nodes = []
    for hop_node in hop.nodes():
        neighbors = set(G.neighbors(hop_node))
        for neighbor in neighbors:
            if neighbor not in hop.nodes():
                if neighbor not in r_hop_boundary_nodes:
                    r_hop_boundary_nodes.append(neighbor)

    vi_BIS = collapse_calculate(G, hop, r_hop_boundary_nodes, "seed")
    print("{} {}-hop successful finish! {}, next one ------------------------------".format(node, R_MAX, max(vi_BIS)))
    # with open("out_2_5w.txt", "a") as file:
    #     file.write(f"{node}, {R_MAX},{max(vi_BIS)}\n")
    # with open("out_1w.txt", "a") as file:
    #     file.write(f"Node: {node}, Result: {res}\n")

    with open("Out/pre-compute/DBLP/317080-1049866-20-3/out_all.txt", "a") as f:
    # with open("Out/pre-compute/Facebook/4039-88234-20-3/out.txt", "a") as f:
        f.write(f"{node}, {R_MAX},{max(vi_BIS)}\n")
    return max(vi_BIS)

def worker_init(graph, r_max):
    global G, R_MAX
    # manager = multiprocessing.Manager()
    # G = manager.dict(graph)
    G = graph
    R_MAX = r_max


def process_nodes(nodes):
    results = []
    for node in nodes:
        result = calculate(node, G, R_MAX)
        results.append(result)
    return results

def main():
    path = "Out/pre-compute/DBLP/317080-1049866-20-3/G_Aux.gml"
    G = nx.read_gml(path)
    query_node = (np.load("dblp_ground_need_new.npy")).tolist()

    nodes = query_node
    R_MAX = 2

    num_processes = multiprocessing.cpu_count()
    if len(nodes) < num_processes:
        num_processes = len(nodes)
    # print(num_processes)
    # num_processes = 7
    chunk_size = len(nodes) // num_processes
    print(chunk_size)
    node_chunks = [nodes[i:i + chunk_size] for i in range(0, len(nodes), chunk_size)]
    # all_nodes = len(nodes)

    with multiprocessing.Pool(processes=num_processes, initializer=worker_init, initargs=(G, R_MAX)) as pool:
        # finished_nodes = 0
        pool.map(process_nodes, node_chunks)

    print("JIAYOU, ok!")

if __name__ == "__main__":
    main()
