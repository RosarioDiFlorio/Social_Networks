#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from load_dataset import get_fullgraph

def HITS1(graph,step,confidence=1.0e-6):
  n = len(graph)
  nodes = range(n)
  done = 0
  time = 0
  
  #Initialization
  h = np.ones((n,1))
  L = np.matrix(graph)
  a = np.zeros((n,1))

  lastA = np.zeros((n,1))
  lastH = np.zeros((n,1))
    
  while not done and time < step:
    print("Step: " + str(time)+"/"+str(step))
    time += 1

    a = np.dot(L.transpose(),h)

    maxA = np.amax(a)
    a/=maxA

    h = np.dot(L,a)
    maxH = np.amax(h)
    h /=maxH

    diffa = np.abs(a - lastA).sum()
    diffh = np.abs(h - lastH).sum()
    lastA = a
    lastH = h
    
    if diffa <= confidence or diffh < confidence:
      done = 1
    
  return time, a.flatten().tolist(), h.flatten().tolist()

def HITS2(graph,step,confidence=1.0e-6):

  print("-----START LOADING FULLGRAPH------")
  grafo = get_fullgraph()
  graph = grafo
  print("-----FINISHED LOADING FULLGRAPH------")

  nodes=graph.keys()
  n=len(nodes)
  done = 0
  time = 0
  
  #Initialization
  a = dict()
  h = dict()
  lastA = dict()
  lastH = dict()
  for i in nodes:
    a[i] = 0.0
    lastA[i] = 0.0
    h[i] = 1.0 
    lastH[i] = 0.0


  
  while not done and time < step:
    print("Step: " + str(time)+"/"+str(step))
    time += 1
    
    maxA = -1


    for n in nodes:
      incoming = graph[n]["incoming"]
      a[n] = 0
      for i in incoming:
          a[n] += h[i]
      if a[n] > maxA:
        maxA = a[n]  
 
    for n in nodes:
      #print(a[n])
      a[n]/=maxA
      #print(a[n])

    maxH = -1 
    for n in nodes:
      outgoing = graph[n]["outgoing"]
      h[n] = 0
      if type(outgoing) == float:
        outgoing=[]
      for o in outgoing:
        h[n] += a[o]
      if h[n] > maxH:
        maxH = h[n]

    for n in nodes:
      h[n]/=maxH

    #print("A: " +str(a))
    #print("H: " +str(h))
    #raw_input()

    #Computes the distance between the old rank vector and the new rank vector in L_1 norm

    npa = np.array(list(a.values()))
    nph = np.array(list(h.values()))
    nplastA = np.array(list(lastA.values()))
    nplastH = np.array(list(lastH.values()))

    diffa = np.abs(npa - nplastA).sum()
    diffh = np.abs(nph - nplastH).sum()
    lastA = a.copy()
    lastH = h.copy()
    
    if diffa <= confidence or diffh < confidence:
      done = 1

    #print("Iteration: " + str(time) + " diff1: " + str(diffa) + " diffh " + str(diffh))
    
  return time, a , h