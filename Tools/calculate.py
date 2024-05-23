import networkx as nx


def compute_distance(G: nx.classes.graph.Graph, u: int, v: int):
    if nx.has_path(G, u, v):
        distance = nx.shortest_path_length(G, u, v)
        # print("({},{})'s distance is {}-hop".format(u, v, distance))
        return distance
    else:
        print("There is no path between ({},{})".format(u, v))
        return None

# Compute maximum support in graph
def compute_support(graph: nx.classes.graph.Graph) -> nx.classes.graph.Graph:
    return_graph = graph.copy()
    seen = set()
    for node_u in return_graph.nodes:
        u_neighbors_set = set(return_graph.neighbors(node_u))
        seen.add(node_u)
        u_neighbors_filtered = [v for v in u_neighbors_set if v not in seen]
        for node_v in u_neighbors_filtered:
            return_graph.edges[node_u, node_v]["ub_sup"] = len(u_neighbors_set & set(return_graph.neighbors(node_v)))
    return return_graph