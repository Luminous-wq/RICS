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

# offline预计算数据

rand_seed = 2023
random.seed(rand_seed)
np.random.seed(rand_seed)

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
        print(r_hop)
        for node_j in r_hop.nodes:
            # print(type(G.nodes[node_index]["Aux"][r]["BV_r"]))
            # print(type(r_hop.nodes[node_j]["BV"]))
            # print(r_hop.nodes[node_j]["BV"])
            G.nodes[node_index]["Aux"][r]["BV_r"] = G.nodes[node_index]["Aux"][r]["BV_r"] | int(r_hop.nodes[node_j]["BV"])

        for (u, v) in r_hop.edges:
            if u > v and r_hop.edges[u, v]["ub_sup"] > G.nodes[node_index]["Aux"][r]["ub_sup_r"]:
                G.nodes[node_index]["Aux"][r]["ub_sup_r"] = r_hop.edges[u, v]["ub_sup"]
    print("finish {} node".format(node_index))

def graphData_build(G: nx.classes.graph.Graph, keywords_num: int,
                    keywords_pre_need_num: int, dataset: str, n: int,
                    R_MAX: int, N_MAX: int):
    average_degree = sum(d for v, d in nx.degree(G)) / G.number_of_nodes()
    print("Average degree: {}".format(average_degree))
    print("Max degree: {}".format(max(d for v, d in nx.degree(G))))
    print("Min degree: {}".format(min(d for v, d in nx.degree(G))))

    for node in G.nodes:
        bv = 0
        for keyword in G.nodes[node]["keywords"]:
            bv |= (1 << keyword)
        # print(G_data.nodes[node_index]['keywords'])
        # print(bin(bv))
        G.nodes[node]["BV"] = bv

    pivots = random.sample(G.nodes, n)
    print("randomly select pivots: {}".format(pivots))

    for node in G.nodes:
        dist = [0] * n
        for i in range(n):
            dist[i] = compute_distance(G, node, pivots[i])
        G.nodes[node]["dist"] = dist

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
        # ,
        # "zipf"
    )

    create_folder(folder_name)
    initial_directory = os.getcwd()
    os.chdir(folder_name)
    nx.write_gml(G, 'G+.gml')
    print(folder_name, 'G+.gml', 'saved successfully!')
    os.chdir(initial_directory)

def get_boundary_ub_inf(data_path, file_path):
    G = nx.read_gml(data_path)
    ub_inf_data = open(file_path, "r")

    lines = ub_inf_data.readlines()
    for line in lines:
        list = line.split(",")
        print(list)
        if len(list) != 3:
            continue
        node, r, ub_inf = str(list[0]), int(list[1])-1, float(list[2])
        G.nodes[node]["Aux"][r]["ub_inf_r"] = ub_inf

    return G

if __name__ == '__main__':
    path_uni = "Out/pre-compute/synthetic/10000-25032-50-3/G.gml"
    # path_uni_2_5w = "Out/pre-compute/synthetic/25000-62389-50-3/G.gml"
    # path_uni_5w = "Out/pre-compute/synthetic/50000-124797-50-3/zipf/G.gml"
    G = nx.read_gml(path_uni)
    keywords_num = 50
    keywords_pre_need_num = 3
    dataset = "synthetic"
    n = 5 # distance pivots size
    R_MAX = 3
    N_MAX = 100
    #
    start_time = time.time()
    graphData_build(G=G,
                    keywords_num=keywords_num,
                    keywords_pre_need_num=keywords_pre_need_num,
                    dataset=dataset,
                    n=n,
                    R_MAX=R_MAX,
                    N_MAX=N_MAX)
    print("build {} need time: {}".format(path_uni, time.time()-start_time))

    # # path_uni = "Out/pre-compute/synthetic/10000-25032-50-3/G_Aux.gml"
    # path_uni_2_5w = "Out/pre-compute/synthetic/25000-62389-50-3/G.gml"
    # path_uni_5w = "Out/pre-compute/synthetic/50000-124797-50-3/zipf/G+.gml"
    # path_facebook = "Out/pre-compute/Facebook/4039-88234-50-3/G_Aux.gml"
    # path_amazon = "Out/pre-compute/Amazon/334863-925872-50-3/G_Aux.gml"
    # path_dblp = "Out/pre-compute/DBLP/317080-1049866-50-3/G_Aux.gml"
    # # path_1w = "Out/synthetic-10000-ub_inf.txt"
    # path_2w = "Out/out_2_5w.txt"
    # path_5w = "Out/out_5w.txt"
    # path_facebook_inf = "Out/out_facebook.txt"
    # path_amazon_inf = "Out/out_Amazon.txt"
    # path_dblp_inf = "Out/out_dblp.txt"
    # G = get_boundary_ub_inf(data_path=path_dblp, file_path=path_dblp_inf)
    #
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
    # nx.write_gml(G, 'G_Aux+.gml')
    # print(folder_name, 'G_Aux+.gml', 'saved successfully!')
    # os.chdir(initial_directory)


