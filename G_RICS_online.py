import heapq
import time
import math
import networkx as nx
import numpy as np

from Tools.collapse_calculate import collapse_calculate
from information_G_RICS import Info
from Tools.inf_score_u_v import max_weight_path, inf_u_Q


class IndexEntry:
    def __init__(self, key, index_N, idx):
        self.key = key  # distance max form query
        self.index_N = index_N
        self.idx = idx

    def __gt__(self, other):
        if self.index_N["L"] == other.index_N["L"]:
            return self.key > other.key
        else:
            return self.index_N["L"] < other.index_N["L"]


def is_pruning_entry(entry: dict, radius: int, Graph, query_bv: int, ub_inf_threshold: float, dist: int, hop_q_inf: float):
    # r = 0
    # synopsis = entry["R"][r]
    # if int(synopsis["BV_r"]) & query_bv == 0:
    #     return False
    # if hop_q_inf * (0.6 ** (dist)) < ub_inf_threshold:
    #     return False
    return True


def max_inf_ub(H, r, query, G, d, hop_q_inf) -> float:
    max_ub_inf = 0
    for id, entry in enumerate(H):
        dist = max([max(abs(entry.index_N["UD"][d_i] - G.nodes[query]["dist"][d_i]),
                        abs(entry.index_N["LD"][d_i] - G.nodes[query]["dist"][d_i])) for d_i in
                    range(d)])
        # r is index, should +1
        max_ub_inf = max(max_ub_inf,  hop_q_inf * (0.6 ** (dist - r - 1)))

    return max_ub_inf


def G_RICS(
        Graph_G: nx.Graph,
        query_keywords_Lq: list,
        radius_max_R: int,
        candidate_N: int,
        query_center_q: int,
        index_root: list,
        d: int,
        info: Info
) -> list:
    print(candidate_N)
    # 1. hash all keywords in the query keyword set Lq into a query bit vector Lq.BV
    q_bv = 0
    for keyword in query_keywords_Lq:
        q_bv = q_bv | (1 << keyword)

    # 2. obtain the Target community Q with keywords
    query_q = str(query_center_q)
    Q = nx.ego_graph(Graph_G, query_q, radius=radius_max_R, center=True)
    # Flag = True
    remove_list = []
    for v in Q.nodes(data=True):
        if q_bv & v[1]["BV"] == 0:
            remove_list.append(v[0])
    for node in remove_list:
        Q.remove_node(node)
    largest = max(nx.connected_components(Q), key=len)
    acc_Q = Q.subgraph(largest)
    size_Q = acc_Q.number_of_nodes()
    if size_Q == 0:
        print("Invalid query, no target community exists!")
    radius_index = radius_max_R - 1  # G-RICS
    hop_q_inf = Graph_G.nodes[query_q]["Aux"][radius_index]["ub_inf_r"]

    res = []
    res_inf = []
    mid = []
    min_max_inf_so_far = 0
    max_inf_all = 0

    min_heap_H = []
    for idx, entry in enumerate(index_root):
        min_dist = max([max(abs(entry["UD"][d_i] - Graph_G.nodes[query_q]["dist"][d_i]),
                            abs(entry["LD"][d_i] - Graph_G.nodes[query_q]["dist"][d_i])) for d_i in
                        range(d)])
        heapq.heappush(min_heap_H,
                       IndexEntry(key=min_dist,
                                  index_N=entry,
                                  idx=idx))

    vertex_pruning_counter = 0
    leaf_node_visit_counter = 0
    entry_pruning_counter = 0
    refine_number = 0
    given_number = 1
    shortest_dist = float('inf')

    # index traversal
    while len(min_heap_H) > 0:
        start_time = time.time()
        now_entry = heapq.heappop(min_heap_H)
        heapq.heapify(min_heap_H)
        # print(min_heap_H)
        info.select_greatest_entry_in_H_time += (time.time()-start_time)
        # print(min_heap_H)

        # if min_max_inf_so_far >= max_inf_ub(min_heap_H, radius_index, query_q, Graph_G, d, hop_q_inf):
        #     print("early termination")
        #     print("min_max_inf_so_far:{}".format(min_max_inf_so_far))
        #     break
        for child_entry in now_entry.index_N["P"]:
            if child_entry["T"]:

                leaf_node_visit_counter += 1
                leaf_node_start_timestamp = time.time()

                if int(Graph_G.nodes[child_entry["P"]]["BV"]) & q_bv == 0:
                    info.keyword_pruning_counter += 1
                    continue

                if child_entry["P"] in acc_Q.nodes():
                    info.dist_pruning_counter += 1
                    continue

                _dist = nx.shortest_path_length(Graph_G, query_q, child_entry["P"])

                if is_pruning_entry(entry=child_entry, radius=radius_index, Graph=Graph_G,
                                    query_bv=q_bv, ub_inf_threshold=min_max_inf_so_far, dist=_dist, hop_q_inf=hop_q_inf):
                    vertex_pruning_counter += 1
                    if refine_number < given_number:
                        traversal_compute_influence_start_time = time.time()
                        inf_score_C_Q = inf_u_Q(Graph_G, child_entry["P"], acc_Q)
                        info.traversal_compute_influential_score_time += (
                                    time.time() - traversal_compute_influence_start_time)
                        info.compute_inf_count_traversal += 1

                        res.append(child_entry["P"])
                        res_inf.append(inf_score_C_Q)
                        # print("first res: {}".format(res))
                        max_inf_all += inf_score_C_Q
                        min_max_inf_so_far = min(res_inf)

                        refine_number += 1
                        shortest_dist = min(_dist, shortest_dist)

                    else:
                        now_inf_ub = hop_q_inf * (0.6 ** (_dist - radius_index - 1))
                        ls = len(res)
                        if ls < candidate_N:
                            if _dist <= shortest_dist:
                                shortest_dist = _dist

                                compute_influence_start_time = time.time()
                                inf_score_C_Q = inf_u_Q(Graph_G, child_entry["P"], acc_Q)
                                info.compute_inf_count_mid += 1
                                info.traversal_compute_influential_score_time += (
                                        time.time() - compute_influence_start_time)

                                res.append(child_entry["P"])
                                # print("second res: {}".format(res))
                                res_inf.append(inf_score_C_Q)
                                max_inf_all += inf_score_C_Q
                                min_max_inf_so_far = min(res_inf)

                            else:
                                # if now_inf_ub > min(res_inf):
                                mid.extend([(child_entry["P"],
                                             now_inf_ub)])

                        else:
                            # if now_inf_ub > min(res_inf):
                            mid.extend([(child_entry["P"],
                                         now_inf_ub)])
                info.leaf_node_traverse_time += (time.time()-leaf_node_start_timestamp)
            else:

                min_dist = max([max(abs(child_entry["UD"][d_i] - Graph_G.nodes[query_q]["dist"][d_i]),
                                    abs(child_entry["LD"][d_i] - Graph_G.nodes[query_q]["dist"][d_i])) for d_i in
                                range(d)])

                info.entry_node_visit_counter += 1
                non_leaf_node_start_time = time.time()
                if is_pruning_entry(entry=child_entry, radius=radius_index, Graph=Graph_G, query_bv=q_bv,
                                    ub_inf_threshold=min_max_inf_so_far, dist=min_dist, hop_q_inf=hop_q_inf):
                    heapq.heappush(min_heap_H, IndexEntry(key=min_dist,
                                                          index_N=child_entry,
                                                          idx=None))

                else:
                    entry_pruning_counter += 1
                info.non_leaf_node_traverse_time += (time.time()-non_leaf_node_start_time)

    # print(f"now min max inf so far is : {min_max_inf_so_far}")
    M_sorted = sorted(mid, key=lambda x: x[1], reverse=True)
    # # print(M_sorted)
    for i in range(len(M_sorted)):
        item = M_sorted[i]
        if len(res) < candidate_N:
            compute_influence_start_time = time.time()
            inf_score_C_Q = inf_u_Q(Graph_G, item[0], acc_Q)
            info.compute_inf_count_mid += 1
            info.traversal_compute_influential_score_time += (
                    time.time() - compute_influence_start_time)
            res.append(item[0])
            res_inf.append(inf_score_C_Q)
            max_inf_all += inf_score_C_Q
            min_max_inf_so_far = min(res_inf)
        else:
            if min_max_inf_so_far >= item[1]:
                print("early terminal by refine")
                print(min_max_inf_so_far)
                break
            compute_influence_start_time = time.time()
            inf_score_C_Q = inf_u_Q(Graph_G, item[0], acc_Q)
            info.compute_inf_count_mid += 1
            info.traversal_compute_influential_score_time += (
                    time.time() - compute_influence_start_time)
            if inf_score_C_Q > min_max_inf_so_far:
                max_inf_all -= min_max_inf_so_far
                max_so_far_index = res_inf.index(min_max_inf_so_far)
                res_inf[max_so_far_index] = inf_score_C_Q
                res[max_so_far_index] = item[0]
                max_inf_all += inf_score_C_Q
                min_max_inf_so_far = min(res_inf)

    # print(res)
    # print(res_inf)
    print(len(res))
    info.vertex_pruning_counter = (Graph_G.number_of_nodes()-vertex_pruning_counter)
    info.entry_pruning_counter = entry_pruning_counter
    info.leaf_node_visit_counter = leaf_node_visit_counter
    info.influence_score_result = max_inf_all

    return res