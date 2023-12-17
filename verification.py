import networkx as nx
import os
import matplotlib as plt
from Tools.collapse_calculate import collapse_calculate

if __name__ == '__main__':
    G = nx.Graph()
    path_dblp = "Out/pre-compute/DBLP/317080-1049866-50-3/G+.gml"
    G = nx.read_gml(path_dblp)

    print(nx.neighbors(G, "208494"))
