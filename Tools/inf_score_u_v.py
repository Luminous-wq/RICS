import heapq
import time

import networkx as nx
from matplotlib import pyplot as plt


def max_weight_path(graph, u, v):
    # 使用动态规划来计算两点之间的最大权重路径
    dp = {u: 1.0}  # 存储从起点到每个节点的最大权重
    predecessor = {u: None}  # 存储每个节点的前驱节点

    for node in nx.dfs_preorder_nodes(graph, source=u):

        for neighbor in graph.neighbors(node):
            edge_weight = graph[node][neighbor]['weight']
            weight_product = dp[node] * edge_weight

            # 更新最大权重和前驱节点
            if neighbor not in dp or weight_product > dp[neighbor]:
                dp[neighbor] = weight_product
                predecessor[neighbor] = node

    # 通过前驱节点回溯找到最大权重路径
    max_weight = dp[v]
    path = [v]
    while v != u:
        v = predecessor[v]
        path.insert(0, v)

    return max_weight, path


def inf_u_Q(graph, u, Q):
    dp = {u: 1.0}  # 存储从起点到每个节点的最大权重
    predecessor = {u: None}  # 存储每个节点的前驱节点

    for node in nx.dfs_preorder_nodes(graph, source=u):

        for neighbor in graph.neighbors(node):
            edge_weight = graph[node][neighbor]['weight']
            weight_product = dp[node] * edge_weight

            # 更新最大权重和前驱节点
            if neighbor not in dp or weight_product > dp[neighbor]:
                dp[neighbor] = weight_product
                predecessor[neighbor] = node

    ans = 0
    for q in Q.nodes():
        ans += dp[q]
    return ans

# G = nx.DiGraph()
# # G.add_edge('A', 'B', weight=0.8)
# # G.add_edge('B', 'C', weight=0.7)
# # G.add_edge('A', 'D', weight=0.9)
# # G.add_edge('D', 'C', weight=0.85)
# G.add_edge('A', 'B', weight=0.5)
# G.add_edge('B', 'C', weight=0.7)
# G.add_edge('C', 'D', weight=0.3)
# G.add_edge('A', 'D', weight=0.8)
# # 设置起点和终点
# start_node = 'A'
# end_node = 'C'
#
# # 计算最大权重路径
# max_weight, path = max_weight_path(G, start_node, end_node)
#
# # 输出结果
# print(f"最大权重路径的权重: {max_weight}")
# print(f"最大权重路径: {' -> '.join(path)}")

if __name__ == '__main__':
    # path_uni = "../Out/pre-compute/synthetic/10000-25032-50-3/G+.gml"
    path_uni = "../Out/pre-compute/Amazon/334863-925872-50-3/G_Aux+.gml"
    t = time.time()
    G = nx.read_gml(path_uni)
    print(time.time() - t)
    t = time.time()
    print(max_weight_path(G, "449464", "383110"))
    print(time.time()-t)
    # print(nx.shortest_path_length(G, "1", "2000"))

    # t = time.time()
    # print(max_weight_path3(G, "1", "2000"))
    # print(time.time() - t)
