import heapq

import networkx as nx

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

def max_weight_product_path(graph, source, target):
    # 用于存储到达每个节点的最大权重乘积和路径
    max_product = {node: -1 for node in graph.nodes}
    max_product[source] = 1

    # 用于存储最短路径
    predecessors = {node: None for node in graph.nodes}

    # 优先队列，用于存储节点及其对应的最大权重乘积
    priority_queue = [(1, source)]

    while priority_queue:
        current_product, current_node = heapq.heappop(priority_queue)

        # 遍历邻居节点
        for neighbor, edge_data in graph[current_node].items():
            weight = edge_data['weight']
            product = current_product * weight

            # 如果发现更大的权重乘积，更新信息
            if product > max_product[neighbor]:
                max_product[neighbor] = product
                predecessors[neighbor] = current_node
                heapq.heappush(priority_queue, (product, neighbor))

    # 从目标节点反向构建路径
    path = []
    current = target
    while current is not None:
        path.insert(0, current)
        current = predecessors[current]

    return max_product[target], path

# # 创建带权重的社交网络图
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
