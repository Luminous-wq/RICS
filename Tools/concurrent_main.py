# import concurrent.futures
#
# def calculate(node):
#     # 在这里执行对单个节点的计算
#     result = node * 2
#     return result
#
# def process_node(node):
#     result = calculate(node)
#     # 将结果写入文件，可以根据需要修改文件格式
#     with open(f'result_{node}.txt', 'w') as file:
#         file.write(str(result))
#         print()
#
# def main():
#     # 假设你的社交网络节点存储在一个列表中
#     social_network_nodes = [1, 2, 3, 4, 5]
#
#     # 使用ProcessPoolExecutor来实现并行计算
#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         # 提交每个节点的计算任务
#         futures = [executor.submit(process_node, node) for node in social_network_nodes]
#
#         # 等待所有任务完成
#         concurrent.futures.wait(futures)
#
# if __name__ == "__main__":
#     main()

import concurrent.futures
import threading

import networkx as nx
from Tools.collapse_calculate import collapse_calculate

def calculate(node, G, R_MAX, N_MAX):
    # 在这里执行对单个节点的计算
    res = []
    for r in range(R_MAX):
        hop = nx.ego_graph(G=G, n=node, radius=r+1, center=True)
        if hop.number_of_nodes() < N_MAX:
            res.append([0])
        else:
            r_hop_boundary_nodes = []
            for node in hop.nodes():
                neighbors = set(G.neighbors(node))
                # print(neighbors)
                for neighbor in neighbors:
                    if neighbor not in hop.nodes():
                        if neighbor not in r_hop_boundary_nodes:
                            r_hop_boundary_nodes.append(neighbor)

            vi_B = collapse_calculate(G, hop, r_hop_boundary_nodes, "seed")
            res.append(vi_B)
    return res

def process_node(node, lock, output_file, G, R_MAX, N_MAX):
    result = calculate(node, G, R_MAX, N_MAX)

    # 使用锁确保写入操作的同步
    # with lock:
        # 将结果追加到同一个文件
    with open(output_file, 'a') as file:
        file.write(f"Node {node}: {result}\n")

    return f"Node {node} calculation completed."

def main():
    # 假设你的社交网络节点存储在一个列表中
    G = nx.read_gml("../Out/pre-compute/Facebook/4039-88234-20-2/G.gml")

    social_network_nodes = G.nodes
    output_file = '../Useless/results.txt'
    R_MAX = 3
    N_MAX = 100
    # 使用ThreadPoolExecutor来实现并行计算
    with concurrent.futures.ThreadPoolExecutor() as executor:
        # 使用锁确保写入操作的同步
        lock = threading.Lock()

        # 提交每个节点的计算任务
        futures = [executor.submit(process_node, node, lock, output_file, G, R_MAX, N_MAX) for node in social_network_nodes]

        # 等待所有任务完成
        concurrent.futures.wait(futures)

        # 获取任务结果并输出提示
        for future in futures:
            try:
                result = future.result()
                print(result)
            except Exception as e:
                print(f"Error: {e}")

if __name__ == "__main__":
    main()
