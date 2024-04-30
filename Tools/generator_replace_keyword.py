import os
import random
import numpy as np
import networkx as nx
from scipy.stats import zipf

from Tools.aid import create_folder


def replace_keywords(dataset: str, distribution: str):
    # Set seed
    seed = 2022
    random.seed(seed)
    np.random.seed(seed)

    # Set path
    [node_num, edge_num, all_keywords_num, per_vertex_keyword] = dataset.split("-")
    node_num = int(node_num)
    edge_num = int(edge_num)
    all_keywords_num = int(all_keywords_num)
    per_vertex_keyword = int(per_vertex_keyword)
    # per_vertex_keyword = 2
    # base_path = os.path.abspath(os.path.dirname(__file__))
    # input_file_path = os.path.join("../Out", "precompute", "synthetic", dataset, distribution, 'G_Aux.gml')
    input_file_path = os.path.join("../Out", "precompute", "synthetic", dataset, 'G.gml')
    # Load graph
    target_graph = nx.read_gml(input_file_path)
    keywords_set = None
    if distribution == "zipf":
        # Zipf
        a = 2  # param
        zipf_dist = zipf(a)
        size = target_graph.number_of_nodes()
        keywords_set = zipf_dist.rvs(size * per_vertex_keyword)
    elif distribution == "gauss":
        # Gaussian
        mean = 10  # 均值
        stddev = 3  # 标准差
        if all_keywords_num == 10:
            mean = 5  # 均值
            stddev = 1.5  # 标准差
        elif all_keywords_num == 20:
            mean = 10  # 均值
            stddev = 3  # 标准差
        elif all_keywords_num == 50:
            mean = 25  # 均值
            stddev = 7.5  # 标准差
        elif all_keywords_num == 80:
            mean = 40  # 均值
            stddev = 12  # 标准差
        size = target_graph.number_of_nodes()
        keywords_set = np.random.normal(mean, stddev, size)
    print("ok")
    keywords_set = np.clip(keywords_set, 0, all_keywords_num-1).astype(int)
    # keywords_set = list(keywords_set)
    # print(keywords_set)
    # print(len(keywords_set))
    label_counter = [0 for _ in range(all_keywords_num)]
    for i, node in enumerate(target_graph):
        keyword_num = np.random.randint(max(per_vertex_keyword - 1, 1),
                                        per_vertex_keyword + 2)  # the num is key_per ± 1

        keywords = np.random.choice(keywords_set, keyword_num)
        while len(set(keywords)) != len(keywords):
            keywords = np.random.choice(keywords_set, keyword_num)
            # print(f"kale:{i}")
        for keyword in keywords:
            label_counter[keyword] += 1
        keywords_int = [int(x) for x in keywords]
        target_graph.nodes[node]['keywords'] = keywords_int

    print([{i: label_counter[i]} for i in range(all_keywords_num)])
    # for i, node in enumerate(target_graph):
    #     # keyword_num = np.random.randint(max(per_vertex_keyword-1, 1), per_vertex_keyword+2)  # the num is key_per ± 1
    #     keyword_num = per_vertex_keyword
    #     keywords = random.sample(keywords_set, keyword_num)
    #     # keywords = np.random.choice(keywords_set, keyword_num)
    #     while len(set(keywords)) != len(keywords):
    #         keywords = random.sample(keywords_set, keyword_num)
    #         # print("aha?")
    #         # keywords = random.sample(keywords_set, keyword_num)
    #     for keyword in keywords:
    #         label_counter[keyword] += 1
    #
    # #     # keywords = keywords.astype(int)
    #     keywords_int = [int(x) for x in keywords]
    #     target_graph.nodes[node]['keywords'] = keywords_int
        # target_graph.nodes[node]['keywords'] = ','.join(map(int, keywords))


    # print(target_graph.nodes["1"]['keywords'])
    # print(type(target_graph.nodes["1"]['keywords'][0]))
    folder_name = os.path.join("../Out", "precompute", "synthetic", dataset, distribution)

    create_folder(folder_name)
    initial_directory = os.getcwd()
    os.chdir(folder_name)
    nx.write_gml(target_graph, 'G_keyword.gml')
    print(folder_name, 'G_keyword.gml', 'saved successfully!')
    os.chdir(initial_directory)

def replace_keywords_and_allkeywords(dataset: str, distribution: str, all_keywords_num: int, per_vertex_keyword: int):
    # Set seed
    seed = 2022
    random.seed(seed)
    np.random.seed(seed)

    # Set path
    input_file_path = os.path.join("../Out", "precompute", "synthetic", dataset, distribution, 'G_Aux.gml')
    # Load graph
    target_graph = nx.read_gml(input_file_path)
    keywords_set = None
    if distribution == "zipf":
        # Zipf
        a = 2  # param
        zipf_dist = zipf(a)
        size = target_graph.number_of_nodes()
        keywords_set = zipf_dist.rvs(size * per_vertex_keyword)
    elif distribution == "gauss":
        # Gaussian
        mean = 10  # 均值
        stddev = 3  # 标准差
        if all_keywords_num == 10:
            mean = 5  # 均值
            stddev = 1.5  # 标准差
        elif all_keywords_num == 20:
            mean = 10  # 均值
            stddev = 3  # 标准差
        elif all_keywords_num == 50:
            mean = 25  # 均值
            stddev = 7.5  # 标准差
        elif all_keywords_num == 80:
            mean = 40  # 均值
            stddev = 12  # 标准差
        size = target_graph.number_of_nodes()
        keywords_set = np.random.normal(mean, stddev, size)
    elif distribution == "uni":
        size = target_graph.number_of_nodes()
        keywords_set = np.random.uniform(0, all_keywords_num, size=size).astype(int)
    print("ok")
    keywords_set = np.clip(keywords_set, 0, all_keywords_num-1).astype(int)
    # keywords_set = list(keywords_set)
    # print(keywords_set)
    # print(len(keywords_set))
    label_counter = [0 for _ in range(all_keywords_num)]
    for i, node in enumerate(target_graph):
        keyword_num = np.random.randint(max(per_vertex_keyword - 1, 1),
                                        per_vertex_keyword + 2)  # the num is key_per ± 1

        keywords = np.random.choice(keywords_set, keyword_num)
        while len(set(keywords)) != len(keywords):
            keywords = np.random.choice(keywords_set, keyword_num)
            # print(f"kale:{i}")
        for keyword in keywords:
            label_counter[keyword] += 1
        keywords_int = [int(x) for x in keywords]
        target_graph.nodes[node]['keywords'] = keywords_int

    print([{i: label_counter[i]} for i in range(all_keywords_num)])
    # for i, node in enumerate(target_graph):
    #     # keyword_num = np.random.randint(max(per_vertex_keyword-1, 1), per_vertex_keyword+2)  # the num is key_per ± 1
    #     keyword_num = per_vertex_keyword
    #     keywords = random.sample(keywords_set, keyword_num)
    #     # keywords = np.random.choice(keywords_set, keyword_num)
    #     while len(set(keywords)) != len(keywords):
    #         keywords = random.sample(keywords_set, keyword_num)
    #         # print("aha?")
    #         # keywords = random.sample(keywords_set, keyword_num)
    #     for keyword in keywords:
    #         label_counter[keyword] += 1
    #
    # #     # keywords = keywords.astype(int)
    #     keywords_int = [int(x) for x in keywords]
    #     target_graph.nodes[node]['keywords'] = keywords_int
        # target_graph.nodes[node]['keywords'] = ','.join(map(int, keywords))


    # print(target_graph.nodes["1"]['keywords'])
    # print(type(target_graph.nodes["1"]['keywords'][0]))
    folder_name = os.path.join("../Out", "precompute", "synthetic", dataset, distribution)

    # create_folder(folder_name)
    initial_directory = os.getcwd()
    os.chdir(folder_name)
    nx.write_gml(target_graph, 'G_Aux_all_'+str(per_vertex_keyword)+'.gml')
    print(folder_name, 'G_Aux_all_'+str(per_vertex_keyword)+'.gml', 'saved successfully!')
    os.chdir(initial_directory)

if __name__ == "__main__":
    # dataset = "10000-25032-20-3"
    # dataset = "25000-62389-20-3"
    # dataset = "50000-124797-20-3"
    # dataset = "50000-124933-20-3"
    # dataset = "50000-145901-20-3"
    # dataset = "50000-145782-20-3"
    # dataset = "50000-155811-20-3"
    # dataset = "50000-166011-20-3"
    # dataset = "50000-178100-20-3"
    # dataset = "50000-174901-20-3"
    # dataset = "100000-249670-20-3"
    # dataset = "250000-624497-20-3"

    dataset1 = "50000-125106-20-3"
    # dataset2 = "250000-625255-20-3"
    # dataset3 = "100000-250168-20-3"
    # dataset4 = "25000-62667-20-3"
    # dataset5 = "10000-25036-20-3"
    datasets = [dataset1]
    for dataset in datasets:
        replace_keywords_and_allkeywords(
            dataset=dataset,
            distribution="uni",
            all_keywords_num=20,
            per_vertex_keyword=5
        )
        replace_keywords_and_allkeywords(
            dataset=dataset,
            distribution="gauss",
            all_keywords_num=20,
            per_vertex_keyword=5
        )
        replace_keywords_and_allkeywords(
            dataset=dataset,
            distribution="zipf",
            all_keywords_num=20,
            per_vertex_keyword=5
        )
        # replace_keywords_and_allkeywords(
        #     dataset=dataset,
        #     distribution="uni",
        #     all_keywords_num=50,
        #     per_vertex_keyword=3
        # )
        # replace_keywords_and_allkeywords(
        #     dataset=dataset,
        #     distribution="gauss",
        #     all_keywords_num=50,
        #     per_vertex_keyword=3
        # )
        # replace_keywords_and_allkeywords(
        #     dataset=dataset,
        #     distribution="zipf",
        #     all_keywords_num=50,
        #     per_vertex_keyword=3
        # )
        # replace_keywords_and_allkeywords(
        #     dataset=dataset,
        #     distribution="uni",
        #     all_keywords_num=80,
        #     per_vertex_keyword=3
        # )
        # replace_keywords_and_allkeywords(
        #     dataset=dataset,
        #     distribution="gauss",
        #     all_keywords_num=80,
        #     per_vertex_keyword=3
        # )
        # replace_keywords_and_allkeywords(
        #     dataset=dataset,
        #     distribution="zipf",
        #     all_keywords_num=80,
        #     per_vertex_keyword=3
        # )
        # replace_keywords(
        #     dataset=dataset,
        #     distribution="gauss"
        # )
        # replace_keywords(
        #     dataset=dataset,
        #     distribution="zipf"
        # )