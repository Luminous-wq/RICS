import heapq
import time
import math
import networkx as nx
import numpy as np

from Tools.collapse_calculate import collapse_calculate
from information import Info
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


def is_pruning_entry(entry: dict, radius: int, query_bv: int, query_support: int, ub_inf_threshold: float, size_Q: int, dist: int):
    synopsis = entry["R"][radius]
    # print(type(synopsis["BV_r"]))
    # print(type(synopsis["ub_sup_r"]))
    # print(type(synopsis["ub_inf_r"]))
    if int(synopsis["BV_r"]) & query_bv == 0:
        return False
    if synopsis["ub_sup_r"] < query_support:
        return False
    if synopsis["ub_inf_r"] * size_Q * (0.6 ** (dist-radius)) < ub_inf_threshold:
    # if synopsis["ub_inf_r"] < ub_inf_threshold:
        return False
    return True


def max_inf_ub(H, r, N, query, G, d) -> float:
    max_ub_inf = 0
    for id, entry in enumerate(H):
        dist = max([max(abs(entry.index_N["UD"][d_i] - G.nodes[query]["dist"][d_i]),
                        abs(entry.index_N["LD"][d_i] - G.nodes[query]["dist"][d_i])) for d_i in
                    range(d)])
        # dist = max([abs(entry.index_N["UD"][d_i] + G.nodes[query]["dist"][d_i]) for d_i in range(d)])
        max_ub_inf = max(max_ub_inf, entry.index_N["R"][r]["ub_inf_r"] * (0.6 ** (dist - (2*(r+1)+1))))

    max_ub_inf = max_ub_inf*N
    return max_ub_inf


def mid_ub_inf_(ub_inf_r, max_dist, size_, r):
    return ub_inf_r * (0.6 ** (max_dist-r)) * size_


# def cal_truth_inf(G, Q, C):
#     ans = 0
#     for node_q in Q.nodes():
#         for node_c in C.nodes():
#             inf, _ = max_weight_path(G, node_c, node_q)
#             ans += inf
#     return ans

def cal_truth_inf(G, Q, C):
    ans = 0
    for node_c in C.nodes():
        inf = inf_u_Q(G, node_c, Q)
        ans += inf
    return ans


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
    print(acc_Q)

    result_set_S = []
    mid = []
    max_inf_so_far = 0
    radius_index = radius_max_R-1
    min_heap_H = []
    for idx, entry in enumerate(index_root):
        # partition upper bound distance sum of the two sides
        min_dist = max([abs(entry["LD"][d_i] + Graph_G.nodes[query_q]["dist"][d_i]) for d_i in range(d)])
        # partition lower bound distance difference in the two sides
        # min_dist = max([max(abs(entry["UD"][d_i] - Graph_G.nodes[query_q]["dist"][d_i]),
        #                     abs(entry["LD"][d_i] - Graph_G.nodes[query_q]["dist"][d_i])) for d_i in
        #                 range(d)])
        # min_dist = max([abs(entry["UD"][d_i] - Graph_G.nodes[query_q]["dist"][d_i]) for d_i in range(d)])
        if min_dist > 2*radius_max_R:
            heapq.heappush(min_heap_H,
                           IndexEntry(key=min_dist,
                                      index_N=entry,
                                      idx=idx))
    # print(max_inf_ub(min_heap_H, radius_index, size_Q, query_q, Graph_G, d))

    vertex_pruning_counter = 0
    leaf_node_visit_counter = 0
    entry_pruning_counter = 0
    refine_number = 0
    M = 1
    dist_size_refine = 10
    dist_size = 0
    dist_size_refine_set = []
    shortest_dist = 0
    max_size = 0
    max_node = None
    # index traversal
    while len(min_heap_H) > 0:
        start_time = time.time()
        now_entry = heapq.heappop(min_heap_H)
        heapq.heapify(min_heap_H)
        # print(min_heap_H)
        info.select_greatest_entry_in_H_time += (time.time()-start_time)
        # print(min_heap_H)

        if max_inf_so_far >= max_inf_ub(min_heap_H, radius_index, size_Q, query_q, Graph_G, d):
            # print(max_inf_ub(min_heap_H, radius_index, size_Q, query_q, Graph_G, d))
            print("early termination")
            print("max_inf_so_far:{}".format(max_inf_so_far))
            break
        for child_entry in now_entry.index_N["P"]:
            if child_entry["T"]:
                _dist = nx.shortest_path_length(Graph_G, query_q, child_entry["P"])
                leaf_node_visit_counter += 1
                if _dist <= 2*radius_max_R:
                    continue

                leaf_node_start_timestamp = time.time()
                if is_pruning_entry(entry=child_entry, radius=radius_index,
                                    query_bv=q_bv, query_support=query_support_k-2,
                                    ub_inf_threshold=max_inf_so_far, size_Q=size_Q, dist=_dist):
                    vertex_pruning_counter += 1
                    C = nx.ego_graph(Graph_G, child_entry["P"], radius=radius_max_R, center=True)
                    # print("C:{}, node: {}".format(C, child_entry["P"]))
                    # C_nodes = C.number_of_nodes()
                    remove_list = []
                    for v in C.nodes(data=True):
                        if q_bv & v[1]["BV"] == 0:
                            remove_list.append(v[0])
                    for node_c in remove_list:
                        C.remove_node(node_c)
                    largest = max(nx.connected_components(C), key=len)
                    lar_C = C.subgraph(largest)
                    t = time.time()
                    C_truss = nx.k_truss(lar_C, query_support_k)

                    t = time.time()
                    # C_truss = nx.k_truss(G=C, k=query_support_k)
                    # print(C)
                    # print("C_truss:{}, node: {}".format(C_truss, child_entry["P"]))
                    C_truss_number = C_truss.number_of_nodes()
                    info.compute_k_truss_time += (time.time() - t)
                    if C_truss_number == 0:
                        # print("oh no")
                        continue
                    # f = True
                    # for vertex in C_truss.nodes(data=True):
                    #     if q_bv & int(vertex[1]["BV"]) == 0:
                    #         f = False
                    #         break
                    # if not f:
                    #     # print("{}'s vector keyword pruning".format(child_entry["P"]))
                    #     continue
                    if refine_number < M:
                        if C_truss_number <= seed_number_N:
                            traversal_compute_influence_start_time = time.time()
                            inf_score_C_Q = cal_truth_inf(Graph_G, acc_Q, C_truss)
                            info.traversal_compute_influential_score_time += (
                                        time.time() - traversal_compute_influence_start_time)
                            info.compute_inf_count_traversal += 1
                            if inf_score_C_Q > max_inf_so_far:
                                max_inf_so_far = inf_score_C_Q
                                # result_set_S.clear()
                                # result_set_S.update(C_truss.nodes())
                                result_set_S.append(C_truss.nodes())
                                info.result_center = child_entry["P"]
                                refine_number += 1
                        else:
                            t = time.time()
                            while C_truss_number > seed_number_N:
                                temp = nx.k_truss(G=C_truss, k=query_support_k)
                                if temp.number_of_nodes() == C_truss_number:
                                    min_degree_node = None
                                    min_degree = float('inf')
                                    for node in C_truss.nodes():
                                        degree = C_truss.degree(node)
                                        if degree < min_degree:
                                            min_degree = degree
                                            min_degree_node = node
                                    temp.remove_node(min_degree_node)
                                    # largest = max(nx.connected_components(temp), key=len)
                                    C_truss = nx.k_truss(temp, query_support_k)
                                    C_truss_number = C_truss.number_of_nodes()
                                    # print(f"hh:{C_truss}")
                                else:
                                    C_truss = temp
                                    C_truss_number = C_truss.number_of_nodes()
                            if C_truss_number == 0:
                                continue
                            info.compute_k_truss_time += (time.time() - t)
                            compute_influence_start_time = time.time()
                            inf_score_sC_Q = cal_truth_inf(Graph_G, acc_Q, C_truss)
                            info.traversal_compute_influential_score_time += (
                                        time.time() - compute_influence_start_time)
                            info.compute_inf_count_mid += 1
                            if inf_score_sC_Q > max_inf_so_far:
                                max_inf_so_far = inf_score_sC_Q
                                # result_set_S.clear()
                                # result_set_S.update(C_truss.nodes())
                                result_set_S.append(C_truss.nodes())
                                info.result_center = child_entry["P"]
                                refine_number += 1

                        shortest_dist = max(_dist, shortest_dist)
                        max_size = max(C_truss_number, max_size)
                        max_node = child_entry["P"]
                    else:
                        while C_truss_number > seed_number_N:
                            temp = nx.k_truss(G=C_truss, k=query_support_k)
                            if temp.number_of_nodes() == C_truss_number:
                                min_degree_node = None
                                min_degree = float('inf')
                                for node in C_truss.nodes():
                                    degree = C_truss.degree(node)
                                    if degree < min_degree:
                                        min_degree = degree
                                        min_degree_node = node
                                temp.remove_node(min_degree_node)
                                # largest = max(nx.connected_components(temp), key=len)
                                C_truss = nx.k_truss(temp, query_support_k)
                                C_truss_number = C_truss.number_of_nodes()
                                # print(f"hh:{C_truss}")
                            else:
                                C_truss = temp
                                C_truss_number = C_truss.number_of_nodes()
                        if C_truss_number == 0:
                            continue
                        else:

                            now_inf_ub = child_entry["R"][radius_index]["ub_inf_r"] * (0.6 ** (_dist - (2*radius_max_R+1))) * size_Q
                            if dist_size < dist_size_refine:
                                if _dist < shortest_dist:
                                    # dist_size_refine_set.extend([(child_entry["P"], C_truss)])
                                    dist_size += 1
                                    shortest_dist = _dist
                                    max_size = C_truss_number
                                    max_node = child_entry["P"]
                                    compute_influence_start_time = time.time()
                                    inf_score_C_Q = cal_truth_inf(Graph_G, acc_Q, C_truss)
                                    info.compute_inf_count_mid += 1
                                    info.traversal_compute_influential_score_time += (
                                            time.time() - compute_influence_start_time)
                                    if inf_score_C_Q > max_inf_so_far:
                                        max_inf_so_far = inf_score_C_Q
                                        result_set_S.clear()
                                        result_set_S.update(C_truss.nodes())
                                        info.result_center = child_entry["P"]

                                elif _dist == shortest_dist:
                                    if C_truss_number > max_size:
                                        dist_size_refine_set.extend([(child_entry["P"], C_truss)])
                                        dist_size += 1
                                        max_size = C_truss_number
                                        max_node = child_entry["P"]
                                        compute_influence_start_time = time.time()
                                        inf_score_C_Q = cal_truth_inf(Graph_G, acc_Q, C_truss)
                                        info.compute_inf_count_mid += 1
                                        info.traversal_compute_influential_score_time += (
                                                time.time() - compute_influence_start_time)
                                        if inf_score_C_Q > max_inf_so_far:
                                            max_inf_so_far = inf_score_C_Q
                                            result_set_S.clear()
                                            result_set_S.update(C_truss.nodes())
                                            info.result_center = child_entry["P"]
                                    elif C_truss_number == max_size:
                                        if child_entry["R"][radius_index]["ub_inf_r"] > Graph_G.nodes[max_node]["Aux"][radius_index]["ub_inf_r"]:
                                            dist_size_refine_set.extend([(child_entry["P"], C_truss)])
                                            dist_size += 1
                                            max_node = child_entry["P"]
                                            compute_influence_start_time = time.time()
                                            inf_score_C_Q = cal_truth_inf(Graph_G, acc_Q, C_truss)
                                            info.compute_inf_count_mid += 1
                                            info.traversal_compute_influential_score_time += (
                                                    time.time() - compute_influence_start_time)
                                            if inf_score_C_Q > max_inf_so_far:
                                                max_inf_so_far = inf_score_C_Q
                                                result_set_S.clear()
                                                result_set_S.update(C_truss.nodes())
                                                info.result_center = child_entry["P"]
                                        else:
                                            if now_inf_ub > max_inf_so_far:
                                                mid.extend([(child_entry["P"],
                                                             now_inf_ub, C_truss)])
                                    else:
                                        if now_inf_ub > max_inf_so_far:
                                            mid.extend([(child_entry["P"],
                                                         now_inf_ub, C_truss)])
                                else:
                                    if now_inf_ub > max_inf_so_far:
                                        mid.extend([(child_entry["P"],
                                                     now_inf_ub, C_truss)])

                            else:
                                if now_inf_ub > max_inf_so_far:
                                    mid.extend([(child_entry["P"],
                                                 now_inf_ub, C_truss)])
                                # mid.append(child_entry["P"])
                info.leaf_node_traverse_time += (time.time()-leaf_node_start_timestamp)
            else:
                # min_dist = max([max(abs(child_entry["UD"][d_i] - Graph_G.nodes[query_q]["dist"][d_i]),
                #                     abs(child_entry["LD"][d_i] - Graph_G.nodes[query_q]["dist"][d_i])) for d_i in
                #                 range(d)])
                min_dist = max([abs(child_entry["UD"][d_i] + Graph_G.nodes[query_q]["dist"][d_i]) for d_i in range(d)])

                info.entry_node_visit_counter += 1
                non_leaf_node_start_time = time.time()
                if is_pruning_entry(entry=child_entry, radius=radius_index, query_bv=q_bv,
                                    query_support=query_support_k-2,
                                    ub_inf_threshold=max_inf_so_far, size_Q=size_Q, dist=min_dist):
                    if min_dist > 2*radius_max_R:
                        heapq.heappush(min_heap_H, IndexEntry(key=min_dist,
                                                              index_N=child_entry,
                                                              idx=None))
                    # print(min_heap_H)

                else:
                    entry_pruning_counter += 1
                info.non_leaf_node_traverse_time += (time.time()-non_leaf_node_start_time)

    # refinement
    # for item in dist_size_refine_set:
    #     compute_influence_start_time = time.time()
    #     inf_score_C_Q = cal_truth_inf(Graph_G, acc_Q, item[1])
    #     info.compute_inf_count_mid += 1
    #     info.traversal_compute_influential_score_time += (
    #             time.time() - compute_influence_start_time)
    #     if inf_score_C_Q > max_inf_so_far:
    #         max_inf_so_far = inf_score_C_Q
    #         result_set_S.clear()
    #         result_set_S.update(item[1].nodes())
    #         info.result_center = item[0]
    print(f"now max inf so far is : {max_inf_so_far}")

    M_sorted = sorted(mid, key=lambda x: x[1], reverse=True)
    # # print(M_sorted)
    for i in range(len(M_sorted)):
        item = M_sorted[i]
        if max_inf_so_far >= item[1]:
            print("early terminal by refine")
            print(max_inf_so_far)
            break
        # else:
        compute_influence_start_time = time.time()
        inf_score_C_Q = cal_truth_inf(Graph_G, acc_Q, item[2])
        info.compute_inf_count_mid += 1
        info.traversal_compute_influential_score_time += (
                time.time() - compute_influence_start_time)

        if inf_score_C_Q > max_inf_so_far:
            max_inf_so_far = inf_score_C_Q
            result_set_S.clear()
            result_set_S.update(item[2].nodes())
            info.result_center = item[0]
            # print("early terminal by refine")
            # break

    # info.modify_result_set_time = (time.time()-modify_result_set_start_time)
    info.vertex_pruning_counter = (Graph_G.number_of_nodes()-vertex_pruning_counter)
    info.entry_pruning_counter = entry_pruning_counter
    info.leaf_node_visit_counter = leaf_node_visit_counter
    info.influence_score_result = max_inf_so_far

    return list(result_set_S)


