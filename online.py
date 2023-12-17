import random
import networkx as nx
import matplotlib as plt
import os
import numpy as np
from Tools.collapse_calculate import collapse_calculate


def cal_online(G:nx.Graph, Lq:list, r:int, k:int, N:int, vq:int, index:list)-> float:
    cost_time = 0.0
    Lq_BV = 0
    for keyword in Lq:
        Lq_BV |= (1 << keyword)

    Q = nx.ego_graph(G=G, n=vq, radius=r)

    r_hop_boundary_nodes = []
    for hop_node in Q.nodes():
        neighbors = set(G.neighbors(hop_node))
        for neighbor in neighbors:
            if neighbor not in Q.nodes():
                if neighbor not in r_hop_boundary_nodes:
                    r_hop_boundary_nodes.append(neighbor)
    vq_BIS = collapse_calculate(G, Q, r_hop_boundary_nodes, "target")
    print(f"boundary influence set : {vq_BIS}")
    # vq_BIS = [2.626392297980118, 2.0193207219918112, 2.1650416285618137, 1.8146262722187474, 1.088775909731142, 1.6820498656023501, 2.0709517811153084, 2.129963621401913, 2.38625338647087, 1.776169808255972, 1.6472607127926597, 1.5712566002273298, 0.9166289922713956, 2.0164691486961903, 1.8568948224331645, 1.8028633720191662, 1.4806217751695807, 1.5561341625550806, 1.595422228072652, 1.6665699140116919, 1.4192412581526463, 1.5287412193691252]

    L = []
    distances = []
    for node in index[1][vq]:
        L.append(node)
        distances.append()
    sorted_pairs = sorted(zip(distances, L))
    return cost_time

if __name__ == '__main__':
    path = "Out/pre-compute/synthetic/10000-25032-50-3/G+.gml"
    # path = "Out/pre-compute/synthetic/10000-25032-50-3/G_Aux.gml"
    G = nx.read_gml(path)

    Lq_size = 5  # 2 3 5 8 10
    r = 2  # 1 2 3
    k = 4  # 3 4 5
    N = 50  # 10 30 50 80 100
    keywords_num = 50  # 10 20 50 80 100

    seed = 2023
    random.seed(seed)
    np.random.seed(seed)

    vq = random.choice(list(G.nodes))
    print(f"query node : {vq}")
    # vq = 6273
    keywords_set = range(0, keywords_num)
    Lq = random.sample(keywords_set, Lq_size)
    print(f"query keywords : {Lq}")
    # Lq = [44, 28, 24, 20, 39]
    index = [[]]

    cost_time = cal_online(G, Lq, r, k, N, vq, index)

