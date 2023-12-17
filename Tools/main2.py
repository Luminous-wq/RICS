import concurrent.futures
import os
import threading

import networkx as nx
from Tools.collapse_calculate import collapse_calculate
from Tools.aid import create_folder

def calculate(node, G, R_MAX, N_MAX):
    # 在这里执行对单个节点的计算
    res = []
    for r in range(R_MAX):
        hop = nx.ego_graph(G=G, n=node, radius=r + 1, center=True)
        if hop.number_of_nodes() > N_MAX:
            res.append([0])
            print("{} {}-hop not satisfy N_MAX!".format(node, r+1))
        elif hop.number_of_nodes() <= N_MAX:
            r_hop_boundary_nodes = []
            for hop_node in hop.nodes():
                neighbors = set(G.neighbors(hop_node))
                for neighbor in neighbors:
                    if neighbor not in hop.nodes():
                        if neighbor not in r_hop_boundary_nodes:
                            r_hop_boundary_nodes.append(neighbor)

            vi_B = collapse_calculate(G, hop, r_hop_boundary_nodes, "seed")
            print("{} {}-hop successful finish! {}".format(node, r+1, vi_B))
            res.append(vi_B)
        G.nodes[node]["Aux"][r]["ub_inf_r"] = max(res[r])
    return f"Node {node}: {res}"


def process_node(node, lock, output_file, G, R_MAX, N_MAX):
    result = calculate(node, G, R_MAX, N_MAX)

    # 使用锁确保写入操作的同步
    with lock:
        # 将结果追加到同一个文件
        with open(output_file, 'a') as file:
            file.write(f"Node {node}: {result}\n")

    return f"Node {node} calculation completed."


def main():
    G = nx.read_gml("../Out/pre-compute/Amazon/334863-925872-50-3/G+.gml")
    social_network_nodes = G.nodes
    output_file = 'results_amazon.txt'
    dataset_Amazon = "Amazon"
    dataset_DBLP = "DBLP"
    path_Amazon = "Dataset/Amazon/com-amazon.ungraph.txt"
    path_DBLP = "Dataset/DBLP/com-dblp.ungraph.txt"
    keywords_num = 50
    keywords_pre_need_num = 3
    R_MAX = 3
    N_MAX = 100
    number_select_pivots = 5
    # 使用ThreadPoolExecutor来实现并行计算

    node_list = list(G.nodes)
    # 对节点列表进行切片，将不同的切片分配给不同的进程
    node_slices = [list(chunk) for chunk in chunks(node_list, 64)]

    with concurrent.futures.ThreadPoolExecutor(max_workers=64) as executor:
        # Lock Confirmation: Multi-threaded Write Synchronization
        lock = threading.Lock()

        # submit
        futures = [executor.submit(process_node, node_slice, lock, output_file, G, R_MAX, N_MAX) for node_slice in node_slices]


        # thread_count = threading.active_count()
        # print(f"tread's number：{thread_count}")

        concurrent.futures.wait(futures)

        # note
        for future in futures:
            try:
                result = future.result()
                print(result)
            except Exception as e:
                print(f"Error: {e}")

        folder_name = os.path.join(
            "Out",
            "pre-compute",
            dataset_Amazon,
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
        nx.write_gml(G, 'G++.gml')
        print(folder_name, 'G++.gml', 'saved successfully!')
        os.chdir(initial_directory)

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

if __name__ == "__main__":
    main()

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