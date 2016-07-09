#!/usr/bin/python
import json
from PageRank import pageRank2
import timeit
from load_dataset import *

rep = 1
elapsed_load = 0
elapsed_dump = 0
elapsed = 0

start_time_load = timeit.default_timer()
graph = graph()
elapsed_load += timeit.default_timer() - start_time_load 
print("---------STARTING ---------")
for i in range(rep):
	start_time = timeit.default_timer()
	#print("---------STARTING PAGERANK---------")
	time2, rank2 = pageRank2(graph,0.85,75,1e-4)
	#print("---------FINISHED PAGERANK---------")

	elapsed += timeit.default_timer() - start_time

	start_time_dump = timeit.default_timer()
	#print("---------DUMPING RESULT---------")
	with open('result_PageRank.json','w') as fp:
		json.dump(rank2,fp)
	#print("---------FINISHED DUMPING---------")
	elapsed_dump += timeit.default_timer() - start_time_dump
print("---------FINISHED---------")
print("Load:\t"+str(float(elapsed_load)/rep))
print("Algorithn:\t"+str(float(elapsed)/rep))
print("Dump:\t"+str(float(elapsed_dump)/rep))