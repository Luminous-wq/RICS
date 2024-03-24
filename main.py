import os
import time

import networkx as nx

from argparser import args_parser
from information import Info
from offline_construct_index import load_index_from_json
from online_RICS_process import RICS
from Tools.aid import info_file_save
if __name__ == '__main__':
    args = args_parser()
    # print(args.keywords)
    info = Info(
        input_file_folder=args.input,
        query_keywords_Lq=[int(keyword) for keyword in args.keywords.split(",")],
        radius_max_R=args.radius,
        query_support_k=args.support,
        seed_number_N=args.number,
        query_center_q=args.query,
        d=args.distance,
    )
    data_graph = nx.read_gml(info.input_file_name)
    index_root = load_index_from_json(info.index_file_name)
    info.start_time = time.time()
    result = RICS(
        Graph_G=data_graph,
        query_keywords_Lq=info.query_keywords_Lq,
        radius_max_R=args.radius,
        query_support_k=args.support,
        seed_number_N=args.number,
        query_center_q=args.query,
        index_root=index_root,
        d=args.distance,
        info=info,
    )
    info.finish_time = time.time()
    info.RICS_result = result
    info_file_save(info, args.input)
    # print(info.get_RICS_result())
    # [27, 48, 30, 23, 37]
    # python main.py -i Out/pre-compute/Facebook/4039-88234-50-3 -Lq 15,14,13,11,4 -R 2 -k 4 -N 100 -q 1 -d 5
    # python main.py -i Out/pre-compute/synthetic/10000-25032-50-3 -Lq 27,48,30,23,37 -R 2 -k 4 -N 50 -q 6273 -d 5
    # python main.py -i Out/pre-compute/DBLP/317080-1049866-50-3 -Lq 24,44,28,20,39 -R 2 -k 4 -N 50 -q 389977 -d 5
    # python main.py -i Out/pre-compute/DBLP/317080-1049866-50-3 -Lq 30,35,26,46,27 -R 2 -k 4 -N 50 -q 389977 -d 5
    # python main.py -i Out/pre-compute/Facebook/4039-88234-50-3 -Lq 24,44,28,20,39 -R 2 -k 4 -N 50 -q 396 -d 5
