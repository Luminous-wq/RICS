import multiprocessing
import os

import networkx as nx

from Tools.aid import create_folder
from Tools.collapse_calculate import collapse_calculate


def calculate(node, G, R_MAX, N_MAX):
    # 在这里执行对单个节点的计算
    res = []
    for r in range(R_MAX):
        hop = nx.ego_graph(G=G, n=node, radius=r + 1, center=True)
        if hop.number_of_nodes() > N_MAX:
            res.append([0])
            print("{} {}-hop not satisfy N_MAX!".format(node, r + 1))
        else:
            r_hop_boundary_nodes = []
            for hop_node in hop.nodes():
                neighbors = set(G.neighbors(hop_node))
                for neighbor in neighbors:
                    if neighbor not in hop.nodes():
                        if neighbor not in r_hop_boundary_nodes:
                            r_hop_boundary_nodes.append(neighbor)

            vi_B = collapse_calculate(G, hop, r_hop_boundary_nodes, "seed")
            print("{} {}-hop successful finish! {}".format(node, r + 1, vi_B))
            res.append(vi_B)
        G.nodes[node]["Aux"][r]["ub_inf_r"] = max(res[r])
    # with open("out.txt", "a") as file:
    #     file.write(f"Node: {node}, Result: {res}\n")
    print("next one ------------------------------")

def worker_init(graph, r_max, n_max):
    # 在每个工作进程中初始化所需的数据
    global G, R_MAX, N_MAX
    G = graph
    R_MAX = r_max
    N_MAX = n_max

def process_nodes(nodes):
    # 这里的函数将用于每个进程计算一组节点
    results = []
    for node in nodes:
        result = calculate(node, G, R_MAX, N_MAX)
        results.append(result)
    return results

def main():
    # 读取图数据，这里假设你已经从GML文件中读取了图数据
    G = nx.read_gml("Out/pre-compute/DBLP/317080-1049866-50-3/G+.gml")

    # 设置参数
    R_MAX = 3
    N_MAX = 50

    # 将节点划分为多个子集，每个子集由一个进程处理
    num_processes = multiprocessing.cpu_count()
    nodes = list(G.nodes())
    chunk_size = len(nodes) // num_processes
    node_chunks = [nodes[i:i + chunk_size] for i in range(0, len(nodes), chunk_size)]

    # 创建进程池
    with multiprocessing.Pool(processes=num_processes, initializer=worker_init, initargs=(G, R_MAX, N_MAX)) as pool:
        for result_chunk in pool.map(process_nodes, node_chunks):
            # 处理每个进程返回的结果
            # 这里可以根据实际情况将结果写入文件或进行其他处理
            with open("out_dblp.txt", "a") as f:
                for result in result_chunk:
                    f.write(f"{result}\n")

    print("compute finished! now save G_Aux!!!!!!!!!!!!!!!!!!!!!!!")
    folder_name = os.path.join(
        "Out",
        "pre-compute",
        "DBLP",
        "{}-{}-{}-{}".format(
            G.number_of_nodes(),
            G.number_of_edges(),
            50,
            3
        )
    )

    create_folder(folder_name)
    initial_directory = os.getcwd()
    os.chdir(folder_name)
    nx.write_gml(G, 'G_Aux.gml')
    print(folder_name, 'G_Aux.gml', 'saved successfully!')
    os.chdir(initial_directory)
    print("ok!")
if __name__ == "__main__":
    main()
