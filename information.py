import os


class Info:
    def __init__(
            self,
            input_file_folder: str,
            query_keywords_Lq: list,
            radius_max_R: int,
            query_support_k: int,
            seed_number_N: int,
            query_center_q: int,
            d: int
    ) -> None:
        self.input_file_name = os.path.join(input_file_folder, "G_Aux+.gml")
        self.index_file_name = os.path.join(input_file_folder, "index_dblp.json")
        self.output_info_file_name = os.path.join(input_file_folder, "information.txt")

        self.RICS_result = []
        input_info = input_file_folder.split('/')[-1].split('-')
        self.nodes_num = input_info[0]
        self.edges_num = input_info[1]
        self.all_keyword_num = input_info[2]
        self.keywords_pre_vertex = input_info[3]
        self.d = d
        self.distribution = "uniform"

        self.query_keywords_Lq = query_keywords_Lq
        self.radius_max_R = radius_max_R
        self.query_support_k = query_support_k
        self.seed_number_N = seed_number_N
        self.query_center_q = str(query_center_q)

        self.start_time = 0
        self.finish_time = 0

        self.select_greatest_entry_in_H_time = 0
        self.leaf_node_traverse_time = 0
        self.non_leaf_node_traverse_time = 0
        self.compute_r_hop_time = 0
        self.compute_k_truss_time = 0
        self.compute_influential_score_time = 0
        self.modify_result_set_time = 0

        self.vertex_pruning_counter = 0
        self.entry_pruning_counter = 0
        self.leaf_node_counter = 0
        self.leaf_node_visit_counter = 0

        self.compute_inf_count = 0
        self.compute_inf_count_mid = 0

        self.influence_score_result = 0
    def get_RICS_result(self) -> str:
        result = ""
        result += "INFORMATION RESULTS\n"
        result += "------------------FILE INFO------------------\n"
        result += "Input File: {}\n".format(self.input_file_name)
        result += "Index File: {}\n".format(self.index_file_name)
        result += "Output Info File: {}\n".format(self.output_info_file_name)
        result += "\n"
        result += "------------------ANSWER INFO------------------\n"
        result += "Top1 RICS Result: {}\n".format(self.RICS_result)
        result += "Total Nodes Number: {}\n".format(self.nodes_num)
        result += "Total Edges Number: {}\n".format(self.edges_num)
        result += "All Keywords: {}\n".format(self.all_keyword_num)
        result += "Keywords Per Vertex: {}\n".format(self.keywords_pre_vertex)
        result += "Distribution: {}\n".format(self.distribution)
        result += "Influence score: {}\n".format(self.influence_score_result)
        result += "\n"
        result += "------------------QUERY INFO------------------\n"
        result += "Query Center: {}\n".format(self.query_center_q)
        result += "Query Keywords: {}\n".format(self.query_keywords_Lq)
        result += "Query Support: {}\n".format(self.query_support_k)
        result += "Query Radius: {}\n".format(self.radius_max_R)
        result += "Query Distance Pivots Number: {}\n".format(self.d)
        result += "\n"
        result += "------------------PRUNING INFO------------------\n"
        result += "Pruning Vertices: {}\n".format(self.vertex_pruning_counter)
        result += "Pruning Entries: {}\n".format(self.entry_pruning_counter)
        result += "Leaf Nodes: {}\n".format(self.leaf_node_counter)
        result += "Pruning Leaf Nodes: {}\n".format(self.leaf_node_counter - self.leaf_node_visit_counter)
        result += "\n"
        result += "------------------TIME INFO------------------\n"
        result += "Started at: {} \tFinished at: {}\n".format(self.start_time, self.finish_time)
        result += "Total time: {}\n".format(self.finish_time - self.start_time)
        result += "Select Greatest Entry in Heap time: {}\n".format(self.select_greatest_entry_in_H_time)
        result += "Leaf Node Traverse time: {}\n".format(self.leaf_node_traverse_time)
        result += "NonLeaf Node Traverse time: {}\n".format(self.non_leaf_node_traverse_time)
        result += "Compute Target R-Hop time: {}\n".format(self.compute_r_hop_time)
        result += "Compute K-Truss time: {}\n".format(self.compute_k_truss_time)
        result += "Compute Influential Score time: {}\n".format(self.compute_influential_score_time)
        result += "Modify Result Set time: {}\n".format(self.modify_result_set_time)
        result += "------------------Count INFO------------------\n"
        result += "Influential count: {}\n".format(self.compute_inf_count)
        result += "Influential count mid: {}\n".format(self.compute_inf_count_mid)
        return result
