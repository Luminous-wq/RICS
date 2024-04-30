import os
import random
import numpy as np
import networkx as nx
from scipy.stats import zipf
from Tools.calculate import compute_distance, compute_support
from Tools.aid import create_folder


def replace_distance(dataset: str, distribution: str, n: int):
    # Set seed
    seed = 2022
    random.seed(seed)
    np.random.seed(seed)

    # Set path
    input_file_path = os.path.join("../Out", "precompute", "synthetic", dataset, distribution, 'G_Aux.gml')
    # Load graph
    target_graph = nx.read_gml(input_file_path)

    pivots = random.sample(target_graph.nodes, n)
    print("randomly select pivots: {}".format(pivots))

    for node in target_graph.nodes:
        dist = [0] * n
        for i in range(n):
            dist[i] = compute_distance(target_graph, node, pivots[i])
        target_graph.nodes[node]["dist"] = dist

    folder_name = os.path.join("../Out", "precompute", "synthetic", dataset, distribution)

    # create_folder(folder_name)
    initial_directory = os.getcwd()
    os.chdir(folder_name)
    nx.write_gml(target_graph, 'G_Aux_dist_'+str(n)+'.gml')
    print(folder_name, 'G_Aux_dist_'+str(n)+'.gml', 'saved successfully!')
    os.chdir(initial_directory)

if __name__ == "__main__":

    dataset1 = "50000-125106-20-3"
    # n = 3  # 3 5 8 10
    datasets = [dataset1]
    for dataset in datasets:
        replace_distance(
            dataset=dataset,
            distribution="uni",
            n = 3  # 3 5 8 10
        )
        replace_distance(
            dataset=dataset,
            distribution="gauss",
            n = 3  # 3 5 8 10
        )
        replace_distance(
            dataset=dataset,
            distribution="zipf",
            n = 3  # 3 5 8 10
        )
        replace_distance(
            dataset=dataset,
            distribution="uni",
            n=8  # 3 5 8 10
        )
        replace_distance(
            dataset=dataset,
            distribution="gauss",
            n=8  # 3 5 8 10
        )
        replace_distance(
            dataset=dataset,
            distribution="zipf",
            n=8  # 3 5 8 10
        )
        replace_distance(
            dataset=dataset,
            distribution="uni",
            n=10  # 3 5 8 10
        )
        replace_distance(
            dataset=dataset,
            distribution="gauss",
            n=10  # 3 5 8 10
        )
        replace_distance(
            dataset=dataset,
            distribution="zipf",
            n=10  # 3 5 8 10
        )
