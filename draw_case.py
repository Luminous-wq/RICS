import networkx as nx
import matplotlib.pyplot as plt
from matplotlib import rcParams
from matplotlib.cm import ScalarMappable
from matplotlib.colors import LinearSegmentedColormap


def inf_u_Q_with_path(graph, u, Q):
    dp = {u: 1.0}  
    predecessor = {u: None}  

    for node in nx.dfs_preorder_nodes(graph, source=u):
        for neighbor in graph.neighbors(node):
            edge_weight = graph[node][neighbor]['weight']
            weight_product = dp[node] * edge_weight
   
            if neighbor not in dp or weight_product > dp[neighbor]:
                dp[neighbor] = weight_product
                predecessor[neighbor] = node

    ans = 0

    weight = []
    edges = []
    for q in Q.nodes():
        ans += dp[q]
        weight.append(dp[q])
        edges.append([u,q])


    return ans, weight, edges


if __name__ == '__main__':
    rcParams['font.family'] = 'Times New Roman'
    # Graph = nx.read_gml("Out/pre-compute/Facebook/4039-88234-20-3/G_Aux_new.gml")
    Graph = nx.read_gml("Out/pre-compute/DBLP/317080-1049866-20-3/G_Aux.gml")
    query_keywords_Lq = [16, 3, 13, 10, 6]
    R = 2
    # get_influence_score = 0
    # target_nodes = ["2854"]
    # core_nodes = ['3458', '3834', '3845', '3764', '3532', '414', '3736', '3976']
    # # u = '3458'
    # seed_nodes = ['3458', '3834', '3845', '3764', '3532', '414', '3736', '3976']
    # draw_target = nx.ego_graph(Graph, target_node, radius=R)
    # q_bv = 0
    # for keyword in query_keywords_Lq:
    #     q_bv = q_bv | (1 << keyword)
    # remove_list = []
    # for v in draw_target.nodes(data=True):
    #     if q_bv & v[1]["BV"] == 0:
    #         remove_list.append(v[0])
    # for node in remove_list:
    #     draw_target.remove_node(node)
    # largest = max(nx.connected_components(draw_target), key=len)
    # target_graph = draw_target.subgraph(largest)

    seed_nodes = ['152981', '141825', '381804', '259933', '269818', '259934', '146686', '72987']
    target_nodes = ['36868', '137916', '76122', '311316', '88027', '6453', '12603', '154458', '30403', '6990', '43459', '184898', '9084', '326452', '313067', '38529', '73194', '34632', '117888', '34990', '75849', '11983', '18324', '180399', '15852', '9805', '280671', '79279', '107882', '366247', '85680', '119933', '261461', '67679', '154549', '17580', '112153', '149001', '137915', '190309', '33148', '87642', '89200', '60131', '96246', '238868', '21158', '5184', '19906', '38115', '115617', '60495', '95991', '19310', '26144']
    # print(target_nodes)
    core_nodes = ["365155", '359247', '365156', '359248', '290193', '398390', '359246', '113298', '209005']
    seed_graph = Graph.subgraph(seed_nodes)
    target_graph = Graph.subgraph(target_nodes)
    core_graph = Graph.subgraph(core_nodes)

    fig = plt.figure(figsize=(12, 4))
    ax = fig.add_subplot(1, 2, 1)
    whole_nodes = seed_nodes + target_nodes
    whole_graph = nx.subgraph(Graph, whole_nodes)
    new = nx.Graph(whole_graph)
    add_edges = []
    for u in seed_nodes:
        ans, weight, edges = inf_u_Q_with_path(Graph, u, target_graph)
        # print("node : {}, truss weight: {}".format(u, weight))
        # print(ans)
        for i in range(len(weight)):
            new.add_edge(edges[i][0], edges[i][1], weight=weight[i])
            add_edges.append((edges[i][0], edges[i][1]))
    whole_graph = new

    for u, v, data in target_graph.edges(data=True):
        if whole_graph.has_edge(u, v):
            whole_graph[u][v]['weight'] = 0
    for u, v, data in seed_graph.edges(data=True):
        if whole_graph.has_edge(u, v):
            whole_graph[u][v]['weight'] = 0

    # print(add_edges)
    seed_pos = nx.circular_layout(nx.subgraph(whole_graph, seed_nodes))
    target_pos = nx.circular_layout(nx.subgraph(whole_graph, target_nodes))
    for pos in seed_pos.values():
        pos[0] -= 2
    for pos in target_pos.values():
        pos[0] += 2

    all_pos = {}
    all_pos.update(seed_pos)
    all_pos.update(target_pos)
    edges_to_draw = [(u, v) for u, v in whole_graph.edges() if u in all_pos and v in all_pos]
    edges_to_draw_target = [(u, v) for u, v in target_graph.edges() if u in all_pos and v in all_pos]

    # whole_edges = set(whole_graph.edges())
    # target_edges = set(target_graph.edges())
    # seed_edges = set(seed_graph.edges())
    # difference_edges = whole_edges - seed_edges - target_edges
    difference_edges = add_edges
    # print(difference_edges)

    nx.draw_networkx_nodes(whole_graph, pos=all_pos, nodelist=seed_nodes, node_color='blue', node_shape="^",
                           node_size=30)
    nx.draw_networkx_nodes(whole_graph, pos=all_pos, nodelist=target_nodes, node_color='r', node_shape="*",
                           node_size=30)
    nx.draw_networkx_edges(whole_graph, pos=all_pos, edgelist=edges_to_draw, edge_color="black", width=0.2)

    colors = [whole_graph.edges[u, i]['weight'] for u, i in difference_edges]

    max_weight = 0.2

    color_rgb = [(0.8, 0.92, 1), (0, 0.22, 1)]
    # color_rgb = [(117, 180, 216), (8, 48, 106)] 
    cmap_name = 'custom_blue'
    cm = LinearSegmentedColormap.from_list(cmap_name, color_rgb, N=100)

    nx.draw_networkx_edges(whole_graph, all_pos, edgelist=difference_edges, width=1.5, edge_color=colors,
                           edge_cmap=cm, edge_vmin=0, edge_vmax=max_weight, alpha=0.9)
    # ax.set_title('RICS', loc='center')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['bottom'].set_visible(False)
    ax.spines['left'].set_visible(False)

    ax2 = fig.add_subplot(1, 2, 2)
    whole_nodes = core_nodes + target_nodes
    whole_graph = nx.subgraph(Graph, whole_nodes)
    new = nx.Graph(whole_graph)
    add_edges = set()
    for u in core_nodes:
        ans, weight, edges = inf_u_Q_with_path(Graph, u, target_graph)
        # print("node : {}, core weight: {}".format(u, weight))
        # print(ans)
        for i in range(len(weight)):
            new.add_edge(edges[i][0], edges[i][1], weight=weight[i])
            add_edges.add((edges[i][0], edges[i][1]))
    whole_graph = new

    for u, v, data in target_graph.edges(data=True):
        if whole_graph.has_edge(u, v):
            whole_graph[u][v]['weight'] = 0
    for u, v, data in core_graph.edges(data=True):
        if whole_graph.has_edge(u, v):
            whole_graph[u][v]['weight'] = 0

    core_pos = nx.circular_layout(nx.subgraph(whole_graph, core_nodes))
    target_pos = nx.circular_layout(nx.subgraph(whole_graph, target_nodes))
    for pos in core_pos.values():
        pos[0] -= 2
    for pos in target_pos.values():
        pos[0] += 2

    all_pos = {}
    all_pos.update(core_pos)
    all_pos.update(target_pos)
    edges_to_draw = [(u, v) for u, v in whole_graph.edges() if u in all_pos and v in all_pos]
    edges_to_draw_target = [(u, v) for u, v in target_graph.edges() if u in all_pos and v in all_pos]

    # whole_edges = set(whole_graph.edges())
    # target_edges = set(target_graph.edges())
    # core_edges = set(core_graph.edges())
    # difference_edges = whole_edges - core_edges - target_edges
    difference_edges = add_edges
    # print(difference_edges)

    nx.draw_networkx_nodes(whole_graph, pos=all_pos, nodelist=core_nodes, node_color='blue', node_shape="^",
                           node_size=30)
    nx.draw_networkx_nodes(whole_graph, pos=all_pos, nodelist=target_nodes, node_color='r', node_shape="*",
                           node_size=30)
    nx.draw_networkx_edges(whole_graph, pos=all_pos, edgelist=edges_to_draw, edge_color="black", width=0.2)

    colors = [whole_graph.edges[u, i]['weight'] for u, i in difference_edges]
    # print(colors)
    nx.draw_networkx_edges(whole_graph, all_pos, edgelist=difference_edges, width=1.5, edge_color=colors,
                           edge_cmap=cm, edge_vmin=0, edge_vmax=max_weight, alpha=0.9)

    ax2.spines['top'].set_visible(False)
    ax2.spines['right'].set_visible(False)
    ax2.spines['bottom'].set_visible(False)
    ax2.spines['left'].set_visible(False)

    # cmap = plt.cm.Blues
    sm = ScalarMappable(cmap=cm, norm=plt.Normalize(vmin=0, vmax=max_weight))
    sm.set_array([])

    color_bar = plt.colorbar(sm, ax=[ax, ax2], extend='neither', extendrect=True, aspect=20, shrink=0.8)
    # color_bar.ax.tick_params(labelsize=18)
    # plt.tight_layout()

    plt.subplots_adjust(right=0.76, wspace=0.05)
    plt.savefig('Figure/casestudy3.pdf', bbox_inches='tight')
    plt.show()

