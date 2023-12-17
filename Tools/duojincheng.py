import concurrent.futures
import multiprocessing
import networkx as nx
from Tools.collapse_calculate import collapse_calculate

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
    return f"Node {node}: {res}"

def process_nodes(nodes, G, R_MAX, N_MAX):
    results = []
    for node in nodes:
        result = calculate(node, G, R_MAX, N_MAX)
        results.append(result)
    return results

def write_to_file(results, output_file, lock):
    # 使用锁确保写入操作的同步
    with lock:
        # 将结果追加到同一个文件
        with open(output_file, 'a') as file:
            for result in results:
                file.write(result + '\n')

def main():
    G = nx.read_gml("../Out/pre-compute/Facebook/4039-88234-20-2/G.gml")
    R_MAX = 3
    N_MAX = 100

    # 获取CPU核心数，用于设置进程池大小
    num_processes = multiprocessing.cpu_count()-9
    print(num_processes)
    node_list = list(G.nodes)
    # 对节点列表进行切片，将不同的切片分配给不同的进程
    node_slices = [list(chunk) for chunk in chunks(node_list, num_processes)]

    print(node_slices)

    # 使用ProcessPoolExecutor来实现多进程并行计算
    with concurrent.futures.ProcessPoolExecutor(max_workers=num_processes) as executor:
        # 提交每个进程处理节点的计算任务
        futures = [executor.submit(process_nodes, node_slice, G, R_MAX, N_MAX) for node_slice in node_slices]

        # 等待所有任务完成
        concurrent.futures.wait(futures)

        # 使用锁确保写入操作的同步
        lock = multiprocessing.Lock()

        # 获取任务结果并输出提示
        for future in futures:
            try:
                results = future.result()
                for result in results:
                    print(result)
                # 写入结果到文件
                write_to_file(results, 'output_collapse.txt', lock)
            except Exception as e:
                print(f"Error: {e}")

def chunks(lst, n):
    """Yield successive n-sized chunks from lst."""
    for i in range(0, len(lst), n):
        yield lst[i:i + n]

if __name__ == "__main__":
    main()
