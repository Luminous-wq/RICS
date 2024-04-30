## Reverse Influential Community Search Over Social Networks

### 1. Representations

RICS: Reverse Influential Community Search Over Social Networks.

### 2. Requirement

```
Python 3.11.4
networkx 3.1
pymetis 2020.1
```

### 3. Install

```
pip install networkx
pip install pymetis
pip install scipy
pip install numpy
# or
conda install networkx
conda install pymetis
conda install scipy
conda install numpy
# or
pip install - r requirements.txt
```

### 4. Input Data Format

Our input data is `*.gml` format, which is packed by `nx.write_gml()`.

The input data in `gml` file can be read by `nx.read_gml()` as a `nx.Graph`.

You can process the graph by the function in package `networkx`.

### 5. Usage

```
usage: main.py [-h] [-i INPUT] [-DS DATASET] [-Lq KEYWORDS] [-R RADIUS] [-k SUPPORT] [-N NUMBER] [-q QUERY] [-d DISTANCE]

optional arguments:
  -h, --help            show this help message and exit
  -i INPUT, --input INPUT
                        path of graph input file
  -DS DATASET, --dataset DATASET
                        name of dataset
  -Lq KEYWORDS, --keywords KEYWORDS
                        a keywords set of target community
  -R RADIUS, --radius RADIUS
                        an integer, the maximum radius of seed communities
  -k SUPPORT, --support SUPPORT
                        an integer, the support of seed communities
  -N NUMBER, --number NUMBER
                        the maximum user number of seed communities
  -q QUERY, --query QUERY
                        the center node index of query target community
  -d DISTANCE, --distance DISTANCE
                        the number of select distance pivots

```

Some examples are as follows:

```
conda activate RICS

cd ../

# RICS
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 7,10,12,14,15 -R 2 -k 4 -N 10 -q 30807 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 1,4,6,10,12 -R 2 -k 4 -N 10 -q 11908 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 13,14,15,17,18 -R 2 -k 4 -N 10 -q 47727 -d 5
python main.py -i Out/precompute/synthetic/50000-125106-20-3/uni -DS synthetic -Lq 10,13,16,17,19 -R 2 -k 4 -N 10 -q 37902 -d 5

# G-RICS
python main_G_RICS.py -i Out/pre-compute/Facebook/4039-88234-20-3 -DS facebook -Lq 16,3,13,10,6 -R 2 -k 4 -N 10 -q 4010 -d 5
python main_G_RICS.py -i Out/pre-compute/Facebook/4039-88234-20-3 -DS facebook -Lq 16,3,13,10,6 -R 2 -k 4 -N 10 -q 396 -d 5
python main_G_RICS.py -i Out/pre-compute/Facebook/4039-88234-20-3 -DS facebook -Lq 16,3,13,10,6 -R 2 -k 4 -N 10 -q 399 -d 5
```

### 6. Reference

[pymetis](https://github.com/inducer/pymetis), [networkx](https://networkx.org/).

