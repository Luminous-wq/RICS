import networkx as nx

def facebook():
    # Facebook
    G = nx.read_gml("../Out/pre-compute/Facebook/4039-88234-20-3/G_Aux_new.gml")

    # all_degree = 0
    # for node in G.nodes:
    #     all_degree = all_degree + G.degree(node)

    # avg_degree = all_degree / len(G.nodes)
    # print(avg_degree)
    # print(G)
    # for r in range(3):
    #     all = 0
    #     for node in G.nodes:
    #         r_hop = nx.ego_graph(G, node, r + 1, "True")
    #         all = all + r_hop.number_of_nodes()
    #     print("avg_{}_hop size: {}".format(r + 1, all / G.number_of_nodes()))
    query_keywords_Lq = [16, 3, 13, 10, 6]
    q_bv = 0
    for keyword in query_keywords_Lq:
        q_bv = q_bv | (1 << keyword)
    keyword_pruning = 0
    support_pruning = 0
    # r = 2-1
    # k = 4
    # for node in G.nodes(data=True):
    #     if int(node[1]["Aux"][r]["BV_r"]) & q_bv == 0:
    #         keyword_pruning += 1
    #     if int(node[1]["Aux"][r]["ub_sup_r"]) < k-2:
    #         support_pruning += 1
    # print(keyword_pruning, support_pruning)
    # 0 0
    for node in G.nodes(data=True):
        if int(node[1]["BV"]) & q_bv == 0:
            keyword_pruning += 1
    print(keyword_pruning)
def amazon():
    # G2 = nx.Graph()
    # Graph_dataset = open("../Dataset/Amazon/com-amazon.ungraph.txt", "r")
    # lines = Graph_dataset.readlines()
    # # print(len(lines))
    # for lines in lines:
    #     list = lines.split()
    #     node1, node2 = int(list[0]), int(list[1])
    #     G2.add_edge(node1, node2)
    # all_degree = 0
    # for node in G2.nodes:
    #     all_degree = all_degree + G2.degree(node)
    #
    # avg_degree = all_degree/len(G2.nodes)
    # print(G2)
    # print(avg_degree)
    # for r in range(3):
    #     all = 0
    #     for node in G2.nodes:
    #         r_hop = nx.ego_graph(G2, node, r+1, "True")
    #         all = all + r_hop.number_of_nodes()
    #     print("avg_{}_hop size: {}".format(r+1, all/G2.number_of_nodes()))

    G = nx.read_gml("../Out/pre-compute/Amazon/334863-925872-20-3/G_Aux.gml")
    query_keywords_Lq = [16, 3, 13, 10, 6]
    q_bv = 0
    for keyword in query_keywords_Lq:
        q_bv = q_bv | (1 << keyword)
    keyword_pruning = 0
    # support_pruning = 0
    # r = 2 - 1
    # k = 4
    # for node in G.nodes(data=True):
    #     if int(node[1]["Aux"][r]["BV_r"]) & q_bv == 0:
    #         keyword_pruning += 1
    #     if int(node[1]["Aux"][r]["ub_sup_r"]) < k - 2:
    #         support_pruning += 1
    # print(keyword_pruning, support_pruning)
    # 6711 15661

    for node in G.nodes(data=True):
        if int(node[1]["BV"]) & q_bv == 0:
            keyword_pruning += 1

    print(keyword_pruning)

def dblp():
    # G3 = nx.Graph()
    # Graph_dataset = open("../Dataset/DBLP/com-dblp.ungraph.txt", "r")
    # lines = Graph_dataset.readlines()
    # # print(len(lines))
    # for lines in lines:
    #     list = lines.split()
    #     node1, node2 = int(list[0]), int(list[1])
    #     G3.add_edge(node1, node2)
    # all_degree = 0
    # for node in G3.nodes:
    #     all_degree = all_degree + G3.degree(node)
    #
    # avg_degree = all_degree / len(G3.nodes)
    # print(G3)
    # print(avg_degree)
    # for r in range(3):
    #     all = 0
    #     for node in G3.nodes:
    #         r_hop = nx.ego_graph(G3, node, r + 1, "True")
    #         all = all + r_hop.number_of_nodes()
    #     print("avg_{}_hop size: {}".format(r + 1, all / G3.number_of_nodes()))
    G = nx.read_gml("../Out/pre-compute/DBLP/317080-1049866-20-3/G_Aux.gml")
    query_keywords_Lq = [16, 3, 13, 10, 6]
    q_bv = 0
    for keyword in query_keywords_Lq:
        q_bv = q_bv | (1 << keyword)
    keyword_pruning = 0
    support_pruning = 0
    r = 2 - 1
    k = 4
    for node in G.nodes(data=True):
        if int(node[1]["Aux"][r]["BV_r"]) & q_bv == 0:
            keyword_pruning += 1
        if int(node[1]["Aux"][r]["ub_sup_r"]) < k - 2:
            support_pruning += 1
    print(keyword_pruning, support_pruning)
    # 6003 13068

def eucore():
    G4 = nx.Graph()
    Graph_dataset = open("../Dataset/Eu-core/email-Eu-core.txt", "r")
    lines = Graph_dataset.readlines()
    # print(len(lines))
    for lines in lines:
        list = lines.split()
        node1, node2 = int(list[0]), int(list[1])
        G4.add_edge(node1, node2)
    all_degree = 0
    for node in G4.nodes:
        all_degree = all_degree + G4.degree(node)

    avg_degree = all_degree / len(G4.nodes)
    print(G4)
    print(avg_degree)
    for r in range(3):
        all = 0
        for node in G4.nodes:
            r_hop = nx.ego_graph(G4, node, r + 1, "True")
            all = all + r_hop.number_of_nodes()
        print("avg_{}_hop size: {}".format(r + 1, all / G4.number_of_nodes()))

def synthetic(dataset_synthetic_uni):
    # dataset_synthetic_uni = "../Out/pre-compute/synthetic/10000-25032-50-3/G.gml"
    # G = nx.read_gml(dataset_synthetic_uni)
    #
    # print("diameter:{}".format(nx.diameter(G)))
    # all_degree = 0
    # max_deg = G.degree("0")
    # min_deg = G.degree("0")
    # for node in G.nodes:
    #     all_degree = all_degree + G.degree(node)
    #     if max_deg < G.degree(node):
    #         max_deg = G.degree(node)
    #     if min_deg > G.degree(node):
    #         min_deg = G.degree(node)
    #
    # avg_degree = all_degree / len(G.nodes)
    # print(G)
    # print(f"avg_degree: {avg_degree}")
    # print(f"min_degree: {min_deg}")
    # print(f"max_degree: {max_deg}")
    # for r in range(3):
    #     all = 0
    #     for node in G.nodes:
    #         r_hop = nx.ego_graph(G, node, r + 1, "True")
    #         all = all + r_hop.number_of_nodes()
    #     print("avg_{}_hop size: {}".format(r + 1, all / G.number_of_nodes()))
    G = nx.read_gml("../Out/precompute/synthetic/50000-125106-20-3/uni/G_Aux.gml")
    query_keywords_Lq = [16, 3, 13, 10, 6]
    q_bv = 0
    for keyword in query_keywords_Lq:
        q_bv = q_bv | (1 << keyword)
    keyword_pruning = 0
    support_pruning = 0
    r = 2 - 1
    k = 4
    for node in G.nodes(data=True):
        if int(node[1]["Aux"][r]["BV_r"]) & q_bv == 0:
            keyword_pruning += 1
        if int(node[1]["Aux"][r]["ub_sup_r"]) < k - 2:
            support_pruning += 1
    print(keyword_pruning, support_pruning)

    G = nx.read_gml("../Out/precompute/synthetic/50000-125106-20-3/gauss/G_Aux.gml")
    query_keywords_Lq = [16, 3, 13, 10, 6]
    q_bv = 0
    for keyword in query_keywords_Lq:
        q_bv = q_bv | (1 << keyword)
    keyword_pruning = 0
    support_pruning = 0
    r = 2 - 1
    k = 4
    for node in G.nodes(data=True):
        if int(node[1]["Aux"][r]["BV_r"]) & q_bv == 0:
            keyword_pruning += 1
        if int(node[1]["Aux"][r]["ub_sup_r"]) < k - 2:
            support_pruning += 1
    print(keyword_pruning, support_pruning)


    G = nx.read_gml("../Out/precompute/synthetic/50000-125106-20-3/zipf/G_Aux.gml")
    query_keywords_Lq = [16, 3, 13, 10, 6]
    q_bv = 0
    for keyword in query_keywords_Lq:
        q_bv = q_bv | (1 << keyword)
    keyword_pruning = 0
    support_pruning = 0
    r = 2 - 1
    k = 4
    for node in G.nodes(data=True):
        if int(node[1]["Aux"][r]["BV_r"]) & q_bv == 0:
            keyword_pruning += 1
        if int(node[1]["Aux"][r]["ub_sup_r"]) < k - 2:
            support_pruning += 1
    print(keyword_pruning, support_pruning)

if __name__ == '__main__':
    # path = "../Out/pre-compute/DBLP/317080-1049866-50-3/G+.gml"
    # G = nx.read_gml(path)
    # Q_node = ['389977', '344983', '29901', '99003', '334556', '383148', '68784', '305619', '155747', '355053', '144399',
    #           '19906', '356042', '348091', '322489', '267607', '361536', '54690', '56257', '11364']
    # query_node = []
    # # print(nx.ego_graph(G, '6273', 6, True))
    # for t_node in Q_node:
    #     Q_lb_hop = nx.ego_graph(G, t_node, 4, True)
    #     Q_ub_hop = nx.ego_graph(G, t_node, 6, True)
    #     # print(Q_ub_hop)
    #     for ub_node in Q_ub_hop.nodes:
    #         if ub_node not in Q_lb_hop.nodes:
    #             if ub_node not in query_node:
    #                 query_node.append(ub_node)
    #
    # print(len(query_node))
    # path = "../Out/pre-compute/synthetic/50000-124797-50-3/G.gml"
    # path = "../Out/pre-compute/synthetic/useless/1000-2479-50-3/G.gml"
    # synthetic(path)
    facebook()
    # amazon()
    # dblp()
    # synthetic("1")