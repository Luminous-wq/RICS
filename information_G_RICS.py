import os


class Info:
    def __init__(
            self,
            input_file_folder: str,
            dataset_name: str,
            query_keywords_Lq: list,
            radius_max_R: int,
            candidate_N: int,
            query_center_q: int,
            d: int
    ) -> None:
        self.input_file_name = os.path.join(input_file_folder, "G_Aux.gml")
        self.index_file_name = os.path.join(input_file_folder, "index_"+dataset_name+".json")
        self.output_info_file_name = os.path.join(input_file_folder, "information.txt")

        self.RICS_result = []
        # input_info = None
        if dataset_name == "synthetic":
            input_info = input_file_folder.split('/')[-2].split('-')
        else:
            input_info = input_file_folder.split('/')[-1].split('-')
        self.nodes_num = input_info[0]
        self.edges_num = input_info[1]
        self.all_keyword_num = input_info[2]
        self.keywords_pre_vertex = input_info[3]
        self.d = d
        self.distribution = "uniform"

        self.query_keywords_Lq = query_keywords_Lq
        self.radius_max_R = radius_max_R
        self.candidate_N = candidate_N
        self.query_center_q = str(query_center_q)

        self.start_time = 0
        self.finish_time = 0
        self.select_greatest_entry_in_H_time = 0
        self.leaf_node_traverse_time = 0
        self.non_leaf_node_traverse_time = 0
        self.traversal_compute_influential_score_time = 0

        self.vertex_pruning_counter = 0
        self.entry_pruning_counter = 0
        self.leaf_node_counter = 0
        self.leaf_node_visit_counter = 0
        self.entry_node_visit_counter = 0
        self.dist_pruning_counter = 0
        self.keyword_pruning_counter = 0
        self.compute_inf_count_traversal = 0
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
        result += "Influence score: {}\n".format(self.influence_score_result)
        result += "Total Nodes Number: {}\n".format(self.nodes_num)
        result += "Total Edges Number: {}\n".format(self.edges_num)
        result += "All Keywords: {}\n".format(self.all_keyword_num)
        result += "Keywords Per Vertex: {}\n".format(self.keywords_pre_vertex)
        result += "Distribution: {}\n".format(self.distribution)
        result += "\n"
        result += "------------------QUERY INFO------------------\n"
        result += "Query Center: {}\n".format(self.query_center_q)
        result += "Query Keywords: {}\n".format(self.query_keywords_Lq)
        result += "Query Radius: {}\n".format(self.radius_max_R)
        result += "Query Distance Pivots Number: {}\n".format(self.d)
        result += "Query Seed Community Size N: {}\n".format(self.candidate_N)
        result += "\n"
        result += "------------------PRUNING INFO------------------\n"
        result += "Pruning Vertices: {}\n".format(self.vertex_pruning_counter)
        result += "Pruning Entries: {}\n".format(self.entry_pruning_counter)
        result += "Pruning Keyword: {}\n".format(self.keyword_pruning_counter)
        result += "Pruning Dist: {}\n".format(self.dist_pruning_counter)
        result += "\n"
        result += "------------------TIME INFO------------------\n"
        result += "Started at: {} \tFinished at: {}\n".format(self.start_time, self.finish_time)
        result += "Total time: {}\n".format(self.finish_time - self.start_time)
        result += "Select Greatest Entry in Heap time: {}\n".format(self.select_greatest_entry_in_H_time)
        result += "Leaf Node Traverse time: {}\n".format(self.leaf_node_traverse_time)
        result += "NonLeaf Node Traverse time: {}\n".format(self.non_leaf_node_traverse_time)
        result += "Traversal Compute Influential Score time: {}\n".format(self.traversal_compute_influential_score_time)
        result += "\n"
        result += "------------------COUNT INFO------------------\n"
        result += "Leaf Nodes Visit: {}\n".format(self.leaf_node_visit_counter)
        result += "Entry Nodes Visit: {}\n".format(self.entry_node_visit_counter)
        result += "Influential count: {}\n".format(self.compute_inf_count_traversal)
        # result += "Influential count traversal: {}\n".format(self.compute_inf_count_traversal)
        result += "Influential count mid: {}\n".format(self.compute_inf_count_mid)
        result += "\n"
        return result
