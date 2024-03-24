import heapq
import time
import math
import networkx as nx

from Tools.collapse_calculate import collapse_calculate
from information import Info
from Tools.inf_score_u_v import max_weight_path

class IndexEntry:
    def __init__(self, key, index_N, idx):
        self.key = key # influence score so far
        self.index_N = index_N
        self.idx = idx

    def __gt__(self, other):
        if self.index_N["L"] == other.index_N["L"]:
            return self.key > other.key
        else:
            return self.index_N["L"] < other.index_N["L"]


def max_inf_ub(H, r, N)->float:
    max_ub_inf = 0
    # print()
    for id, entry in enumerate(H):
        # print(id, entry)
        max_ub_inf = max(max_ub_inf, entry.index_N["R"][r]["ub_inf_r"])
        # print(entry.index_N["R"][r]["ub_inf_r"])

    return max_ub_inf*N

def calculate_influence(Graph, size_, BIS_max, vc, vq)->float:
    inf_vc_vq,_ = max_weight_path(Graph, vc, vq)
    inf = size_ * inf_vc_vq * BIS_max
    return inf

def is_pruning_entry(entry: dict, radius: int, query_bv: int, query_support: int, ub_inf_threshold: float):
    synopsis = entry["R"][radius]
    # print(type(synopsis["BV_r"]))
    # print(type(synopsis["ub_sup_r"]))
    # print(type(synopsis["ub_inf_r"]))
    if int(synopsis["BV_r"]) & query_bv == 0:
        return False
    if synopsis["ub_sup_r"] < query_support:
        return False
    if synopsis["ub_inf_r"] < ub_inf_threshold:
        return False
    return True

def compute_r_BIS(Graph_G, Q, type):
    r_hop_boundary_nodes = []
    for hop_node in Q.nodes():
        neighbors = set(Graph_G.neighbors(hop_node))
        for neighbor in neighbors:
            if neighbor not in Q.nodes():
                if neighbor not in r_hop_boundary_nodes:
                    r_hop_boundary_nodes.append(neighbor)
    vq_BIS = collapse_calculate(Graph_G, Q, r_hop_boundary_nodes, type)
    return max(vq_BIS)

def RICS(
        Graph_G: nx.Graph,
        query_keywords_Lq: list,
        radius_max_R: int,
        query_support_k: int,
        seed_number_N: int,
        query_center_q: int,
        index_root: list,
        d: int,
        info: Info
) -> list:
    # 1. hash all keywords in the query keyword set 𝐿𝑞 into a query bit vector 𝐿𝑞.𝐵𝑉
    q_bv = 0
    for keyword in query_keywords_Lq:
        q_bv = q_bv | (1 << keyword)
    # 2. obtain the Target community Q
    Q = nx.ego_graph(Graph_G, str(query_center_q), radius=radius_max_R, center=True)
    # 3. virtual collapse
    # compute_r_hop_start_timestamp = time.time()

    # info.compute_r_hop_time += (time.time()-compute_r_hop_start_timestamp)
    size_Q = Q.number_of_nodes()

    result_set_S = set()
    mid = []
    max_inf_so_far = 0

    query_q = str(query_center_q)
    radius_index = radius_max_R-1
    min_heap_H = []
    for idx, entry in enumerate(index_root):
        # print(min([abs(entry["LD"][d_i] - Graph_G.nodes[query_q]["dist"][d_i]) for d_i in range(d)]))
        heapq.heappush(min_heap_H,
                       IndexEntry(key=min([abs(entry["LD"][d_i] - Graph_G.nodes[query_q]["dist"][d_i]) for d_i in range(d)]),
                                  index_N=entry,
                                  idx=idx))
    # print(max_inf_ub(min_heap_H, radius_max_R, seed_number_N))

    vertex_pruning_counter = 0
    leaf_node_visit_counter = 0
    entry_pruning_counter = 0
    max_influential_score_cost = 0

    # index traversal
    while len(min_heap_H) > 0:
        start_time = time.time()
        now_entry = heapq.heappop(min_heap_H)
        heapq.heapify(min_heap_H)
        # print(min_heap_H)
        info.select_greatest_entry_in_H_time += (time.time()-start_time)
        # print(min_heap_H)

        if max_inf_so_far >= max_inf_ub(min_heap_H, radius_index, seed_number_N):
            print("early termination")
            print("max_inf_so_far:{}".format(max_inf_so_far))
            break
        for child_entry in now_entry.index_N["P"]:
            if child_entry["T"]:
                leaf_node_start_timestamp = time.time()
                if is_pruning_entry(entry=child_entry, radius=radius_index,
                                    query_bv=q_bv, query_support=query_support_k-2,
                                    ub_inf_threshold=max_inf_so_far):
                    vertex_pruning_counter += 1
                    C = nx.ego_graph(Graph_G, child_entry["P"], radius=radius_max_R, center=True)
                    if C.number_of_nodes() <= seed_number_N:
                        compute_influence_start_time = time.time()
                        # BIS_max = compute_r_BIS(Graph_G, C, "seed")
                        inf_score_C_Q = calculate_influence(Graph=Graph_G, size_=size_Q,
                                                            BIS_max=child_entry["R"][radius_index]["ub_inf_r"],
                                                            vc=child_entry["P"], vq=query_q)
                        info.compute_inf_count += 1
                        info.compute_influential_score_time += (time.time()-compute_influence_start_time)
                        if inf_score_C_Q > max_inf_so_far:
                            max_inf_so_far = inf_score_C_Q
                            result_set_S.clear()
                            result_set_S.update(C.nodes())
                    else:
                        if child_entry["R"][radius_index]["ub_inf_r"] > max_inf_so_far:
                            mid.extend([(child_entry["P"], child_entry["R"][radius_index]["ub_inf_r"], C)])
                            # mid.append(child_entry["P"])
                info.leaf_node_traverse_time += (time.time()-leaf_node_start_timestamp)
            else:
                non_leaf_node_start_time = time.time()
                if is_pruning_entry(entry=child_entry, radius=radius_index, query_bv=q_bv, query_support=query_support_k-2, ub_inf_threshold=max_inf_so_far):
                    heapq.heappush(min_heap_H, IndexEntry(key=min([abs(child_entry["LD"][d_i]-Graph_G.nodes[query_q]["dist"][d_i]) for d_i in range(d)]),index_N=child_entry, idx=None))
                    # print(min_heap_H)
                    if len(child_entry["P"]) == 0 or child_entry["T"]:
                        leaf_node_visit_counter += 1
                else:
                    entry_pruning_counter += 1
                info.non_leaf_node_traverse_time += (time.time()-non_leaf_node_start_time)

    # refinement of mid
    modify_result_set_start_time = time.time()
    M_sorted = sorted(mid, key=lambda x: x[1], reverse=True)
    # print(M_sorted)
    # for vc, ub_inf_r, C in enumerate(M_sorted):
    for item in M_sorted:
        if max_inf_so_far > item[1]:
            print("early terminal by refinement")
            break
        subgraph_nodes = list(item[2].nodes)[:seed_number_N]
        subgraph_C = item[2].subgraph(subgraph_nodes)
        compute_influence_start_time = time.time()
        inf_score_sC_Q = calculate_influence(Graph=Graph_G, size_=size_Q,
                                             BIS_max=compute_r_BIS(Graph_G, subgraph_C, "seed"),
                                             vc=item[0], vq=query_q)
        info.compute_inf_count += 1
        info.compute_inf_count_mid += 1
        info.compute_influential_score_time += (time.time() - compute_influence_start_time)
        if inf_score_sC_Q > max_inf_so_far:
            max_inf_so_far = inf_score_sC_Q
            result_set_S.clear()
            result_set_S.update(subgraph_nodes)

    info.modify_result_set_time = (time.time()-modify_result_set_start_time)
    info.vertex_pruning_counter = (Graph_G.number_of_nodes()-vertex_pruning_counter)
    info.entry_pruning_counter = entry_pruning_counter
    info.leaf_node_visit_counter = leaf_node_visit_counter
    info.influence_score_result = max_inf_so_far
    return list(result_set_S)


