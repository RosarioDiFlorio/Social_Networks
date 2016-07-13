from HITS import *
import json
import timeit
from load_dataset import *
import random
import xlwt

def testHits(graph,rep = 1,conf = 0):
    
    elapsed_load = 0
    elapsed_dump = 0
    elapsed = 0
    print("---------STARTING ---------")
    for i in range(rep):
        start_time_load = timeit.default_timer()
        #graph = get_fullgraph()
        elapsed_load += timeit.default_timer() - start_time_load 

        #print("STARTING HITS")
        start_time = timeit.default_timer()
        time , a, h = HITS2(graph,1000,conf)
        elapsed += timeit.default_timer() - start_time
        #print("HITS2 elapsed: " + str(elapsed))
        #print("Time:" + str(time))

        
        result = dict()

        for k in graph:
            result[k] = {"a": a[k], "h": h[k]}

        start_time_dump = timeit.default_timer()
        #print("---------DUMPING RESULT---------")
        with open('result_HITS.json','w') as fp:
            json.dump(result,fp)
        #print("---------FINISHED DUMPING---------")
        elapsed_dump += timeit.default_timer() - start_time_dump
        #print(i)
    print("---------FINISHED---------")
    print("---------TIMES------------")
    print("Num nodes: " +  str(len(graph.keys())))
    print("Repetitions: " + str(rep))
    print("Steps: " + str(time))
   # print("Load:\t"+str(float(elapsed_load)/rep))
    print("Algorithm:\t"+str(float(elapsed)/rep))
    print("Dump:\t"+str(float(elapsed_dump)/rep))
    print("--------------------------")
    return  str(len(graph.keys())), str(float(elapsed)/rep)
    
def runner():
    iterations = 1

    graph = get_fullgraph()
    g = dict()
    j = 0
     #code for write in a xlsx file
    filename = "risultati_hits.xls"
    sheet = "result"

    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet(sheet)
    confidence = [1e-2,1e-3,1e-4,1e-5,1e-6]
    #confidence = [1e-4,1e-5]
    
    
    colNodes = 1
    colTime = 2
    for c in confidence:
        row = 0
        sheet1.write(row,colTime,"confidence: " + str(c))
        row += 1
        j = 0
        for i in graph:
            g[i] = graph[i]
            j = j + 1
            if j % 1000 == 0 and j != 0:
                nodes,time = testHits(g,iterations,c)
                sheet1.write(row,colTime,nodes)
                sheet1.write(row,colNodes,time)
                row += 1
            #print(g)
            #print(".\n")
        g.clear()
        nodes,time = testHits(graph,iterations,c)
        sheet1.write(row,colTime,nodes)
        sheet1.write(row,colNodes,time)
        colTime += 2
        colNodes += 2
        
    book.save(filename)
    
runner()