#!/usr/bin/python
import json
from PageRank import pageRank2
import timeit
from load_dataset import *

def testPageRank(graph, rep = 1):
    
    elapsed_load = 0
    elapsed_dump = 0
    elapsed = 0

    start_time_load = timeit.default_timer()
   # graph = graph()
    elapsed_load += timeit.default_timer() - start_time_load 
    print("---------STARTING ---------")
    for i in range(rep):
            start_time = timeit.default_timer()
            #print("---------STARTING PAGERANK---------")
            time2, rank2 = pageRank2(graph,0.85,1000,1e-4)
            #print("---------FINISHED PAGERANK---------")

            elapsed += timeit.default_timer() - start_time

            start_time_dump = timeit.default_timer()
            #print("---------DUMPING RESULT---------")
            with open('result_PageRank.json','w') as fp:
                    json.dump(rank2,fp)
            #print("---------FINISHED DUMPING---------")
            elapsed_dump += timeit.default_timer() - start_time_dump
    print("---------FINISHED---------")
    print("---------TIMES------------")
    print("Num nodes: " +  str(len(graph.keys())))
    print("Repetitions: " + str(rep))
    print("Steps: " + str(time2))
   # print("Load:\t"+str(float(elapsed_load)/rep))
    print("Algorithm:\t"+str(float(elapsed)/rep))
    print("Dump:\t"+str(float(elapsed_dump)/rep))
    print("--------------------------")


def runner():
    iterations = 1
    gr = graph()
    g = dict()
    j = 0
    for i in gr:
        g[i] = gr[i]
        j = j + 1
        if j % 1000 == 0 and j != 0:
           testPageRank(g,iterations)
           #print(g)
           #print(".\n")
    testPageRank(gr,iterations)
    
runner()