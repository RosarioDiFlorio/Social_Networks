#!/usr/bin/python

from PageRank import pageRank2
from load_dataset import graph
import timeit

graph = graph()
start_time = timeit.default_timer()
time2, rank2 = pageRank2(graph,0.85,75,0)
elapsed2 = timeit.default_timer() - start_time

print(rank2,elapsed2)
