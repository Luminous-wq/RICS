
import os
import time
import networkx as nx
from argparser_topM import args_parser
from information_topM import Info
from offline_construct_index import load_index_from_json
from online_topM_RICS import TopM_RICS
from Tools.aid import info_file_save

if __name__ == '__main__':
    args = args_parser()
    # print(args.keywords)
    info = Info(
        input_file_folder=args.input,
        dataset_name=args.dataset,
        query_keywords_Lq=[int(keyword) for keyword in args.keywords.split(",")],
        radius_max_R=args.radius,
        # query_core_k=args.support,
        query_support_k=args.support,
        seed_number_N=args.number,
        query_center_q=args.query,
        M=args.TopM,
        d=args.distance,
    )
    data_graph = nx.read_gml(info.input_file_name)
    index_root = load_index_from_json(info.index_file_name)
    print("Begin query.")
    info.start_time = time.time()
    result = TopM_RICS(
        Graph_G=data_graph,
        query_keywords_Lq=info.query_keywords_Lq,
        radius_max_R=args.radius,
        # query_core_k=args.support,
        query_support_k=args.support,
        seed_number_N=args.number,
        query_center_q=args.query,
        index_root=index_root,
        d=args.distance,
        M=args.TopM,
        info=info,
    )
    info.finish_time = time.time()
    info.RICS_result = result
    info_file_save(info, args.input)
    print(info.get_RICS_result())
