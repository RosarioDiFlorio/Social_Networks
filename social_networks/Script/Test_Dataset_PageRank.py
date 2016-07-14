#!/usr/bin/python
import json
from PageRank import pageRank2
import timeit
from load_dataset import *
import xlwt

def testPageRank(graph, rep = 1,conf = 0,write = True):
    
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
            time2, rank2 = pageRank2(graph,0.85,1000,conf)
            #print("---------FINISHED PAGERANK---------")

            elapsed += timeit.default_timer() - start_time

            #start_time_dump = timeit.default_timer()
            #print("---------DUMPING RESULT---------")
            if write:
                with open('result_PageRank'+ str(conf) +'.json','w') as fp:
                    json.dump(rank2,fp)
            #print("---------FINISHED DUMPING---------")
            #elapsed_dump += timeit.default_timer() - start_time_dump
    print("---------FINISHED---------")
    print("---------TIMES------------")
    print("Num nodes: " +  str(len(graph.keys())))
    print("Repetitions: " + str(rep))
    print("Steps: " + str(time2))
    #print("Load:\t"+str(float(elapsed_load)/rep))
    print("Algorithm:\t"+str(float(elapsed)/rep))
    #print("Dump:\t"+str(float(elapsed_dump)/rep))
    print("--------------------------")
    return  str(len(graph.keys())), str(float(elapsed)/rep),time2



def runner():
    iterations = 1
    gr = graph()
    g = dict()
    j = 0
    
    #code for write in a xlsx file
    filename = "risultati_pagerank.xls"
    sheet = "result"

    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet(sheet)
    confidence = [1e-4,1e-5,1e-6,1e-7]
    #confidence = [1e-4]

    colNodes = 1
    colTime = 2
    colStep = 3
    flagNodes = True
    for c in confidence:
        row = 0
        if flagNodes:
            sheet1.write(row,colNodes,"Num nodes")
        sheet1.write(row,colTime,"time (confidence: " + str(c) + ")")
        sheet1.write(row,colStep,"steps")
        row += 1
        j = 0
        for i in gr:
            g[i] = gr[i]
            j = j + 1
            if j % 1000 == 0 and j != 0:
                nodes,time,step = testPageRank(g,iterations,c,False)
                if flagNodes:
                    sheet1.write(row,colNodes,nodes)
                sheet1.write(row,colTime,time)
                sheet1.write(row,colStep,step)
                row += 1
            #print(g)
            #print(".\n")
        g.clear()
        nodes,time,step = testPageRank(gr,iterations,c,True)
        if flagNodes: #stampo una sola volta la colonna contenente il numero di nodi processati
            sheet1.write(row,colNodes,nodes)
            flagNodes = False
        sheet1.write(row,colTime,time)
        sheet1.write(row,colStep,step)
        colTime += 3
        colNodes += 3
        colStep += 3
    book.save(filename)
    
    
    
runner()