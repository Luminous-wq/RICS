import networkx as nx
from Tools.inf_score_u_v import max_weight_path


def collapse_calculate(G: nx.Graph, hop_G: nx.Graph, neighbor_nodes_set: list, type: str)-> list:
    # return boundary influence set
    inf_score_boundary = [0]*len(neighbor_nodes_set)
    i = 0

    if type == "target":
        for boundary_node in neighbor_nodes_set:
            temp_sum_inf_i = 0
            for hop_node in hop_G.nodes:
                inf_bn_hn, _ = max_weight_path(G, boundary_node, hop_node)
                temp_sum_inf_i = temp_sum_inf_i + inf_bn_hn
            inf_score_boundary[i] = temp_sum_inf_i
            i = i + 1
    elif type == "seed":
        for boundary_node in neighbor_nodes_set:
            temp_sum_inf_i = 0
            for hop_node in hop_G.nodes:
                inf_bn_hn, _ = max_weight_path(G, hop_node, boundary_node)
                temp_sum_inf_i = temp_sum_inf_i + inf_bn_hn
            inf_score_boundary[i] = temp_sum_inf_i
            i = i + 1
    return inf_score_boundary
