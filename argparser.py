import argparse


def args_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument("-i", "--input", type=str, help="path of graph input file")
    parser.add_argument("-Lq", "--keywords", type=str, help="a keywords set of target community")
    parser.add_argument("-R", "--radius", type=int, help="an integer, the maximum radius of seed communities")
    parser.add_argument("-k", "--support", type=int, help="an integer, the support of seed communities")
    parser.add_argument("-N", "--number", type=int, help="the maximum user number of seed communities")
    parser.add_argument("-q", "--query", type=int, help="the center node index of query target community")
    parser.add_argument("-d", "--distance", type=int, help="the number of select distance pivots")
    args = parser.parse_args()

    return args
