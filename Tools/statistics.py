import networkx as nx

# Facebook
G = nx.read_gml("../Out/pre-compute/Facebook/4039-88234-20-2/G.gml")

all_degree = 0
for node in G.nodes:
    all_degree = all_degree + G.degree(node)

avg_degree = all_degree/len(G.nodes)
print(avg_degree)
print(G)
for r in range(3):
    all = 0
    for node in G.nodes:
        r_hop = nx.ego_graph(G, node, r+1, "True")
        all = all + r_hop.number_of_nodes()
    print("avg_{}_hop size: {}".format(r+1, all/G.number_of_nodes()))


# Amazon
G2 = nx.Graph()
Graph_dataset = open("../Dataset/Amazon/com-amazon.ungraph.txt", "r")
lines = Graph_dataset.readlines()
# print(len(lines))
for lines in lines:
    list = lines.split()
    node1, node2 = int(list[0]), int(list[1])
    G2.add_edge(node1, node2)
all_degree = 0
for node in G2.nodes:
    all_degree = all_degree + G2.degree(node)

avg_degree = all_degree/len(G2.nodes)
print(G2)
print(avg_degree)
for r in range(3):
    all = 0
    for node in G2.nodes:
        r_hop = nx.ego_graph(G2, node, r+1, "True")
        all = all + r_hop.number_of_nodes()
    print("avg_{}_hop size: {}".format(r+1, all/G2.number_of_nodes()))


# DBLP
G3 = nx.Graph()
Graph_dataset = open("../Dataset/DBLP/com-dblp.ungraph.txt", "r")
lines = Graph_dataset.readlines()
# print(len(lines))
for lines in lines:
    list = lines.split()
    node1, node2 = int(list[0]), int(list[1])
    G3.add_edge(node1, node2)
all_degree = 0
for node in G3.nodes:
    all_degree = all_degree + G3.degree(node)

avg_degree = all_degree/len(G3.nodes)
print(G3)
print(avg_degree)
for r in range(3):
    all = 0
    for node in G3.nodes:
        r_hop = nx.ego_graph(G3, node, r+1, "True")
        all = all + r_hop.number_of_nodes()
    print("avg_{}_hop size: {}".format(r+1, all/G3.number_of_nodes()))