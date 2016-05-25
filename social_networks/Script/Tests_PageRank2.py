#!/usr/bin/python

import timeit
from PageRank import *

# Graph is represented with its transition matrix
simple = ([0, 1/2, 1, 0], [1/3, 0, 0, 1/2], [1/3, 0, 0, 1/2], [1/3, 1/2, 0, 0])

start_time = timeit.default_timer()
time1, rank1 = pageRank1(simple,0.85,75,0)
elapsed1 = timeit.default_timer() - start_time

print(rank1, time1, elapsed1)

# Graph is represented with its adjacecy lists
simple = dict()
simple[0] = {1,2,3}
simple[1] = {0,3}
simple[2] = {0}
simple[3] = {1,2}

start_time = timeit.default_timer()
time2, rank2 = pageRank2(simple,0.85,75,0)
elapsed2 = timeit.default_timer() - start_time

print(rank2, time2, elapsed2)