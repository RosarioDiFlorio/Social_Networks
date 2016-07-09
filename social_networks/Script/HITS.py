#!/usr/bin/python
# -*- coding: utf-8 -*-

import numpy as np
from load_dataset import get_fullgraph

def HITS2(graph,step,confidence=1.0e-6):

  nodes=graph.keys()
  n=len(nodes)
  done = 0
  time = 0
  
  #Initialization
  a = dict()
  h = dict()
  lastA = dict()
  lastH = dict()
  olddiffa = 0
  olddiffh = 0
  for i in nodes:
    a[i] = 0.0
    lastA[i] = 0.0
    h[i] = 1.0 
    lastH[i] = 0.0

  

  
  while not done and time < step:
    #print("Step: " + str(time)+"/"+str(step))
    time += 1
    
    maxA = -1
    for n in nodes:
      incoming = graph[n]["incoming"]
      a[n] = 0
      if type(incoming) == float:
        incoming=[]
      for i in incoming:
          if i in h:
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
        if o in a:
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
    
    #suma = np.sum(npa)
    #sumLastA = np.sum(nplastA)
    #diffa = np.abs(suma - sumLastA)
    #sumh = np.sum(nph)
    #sumLastH = np.sum(nplastH)
    #diffh = np.abs(sumh - sumLastH)
    
   
    diffa = 0 
    diffh = 0
    
    for i in a:
        diffa += abs(a[i]-lastA[i])
   
    for i in h:
        diffh += abs(h[i]-lastH[i])
    
    
    lastA = a.copy()
    lastH = h.copy()

    #print(float(olddiffa)-diffa)
    
    if diffa <= confidence or diffh < confidence:
        done = 1
       # print("exit at step " + str(time))
         
    
    #print("Iteration: " + str(time) +"/" +str(step) + " diffa: " + str(diffa) + " diffh " + str(diffh))
    
  return time, a, h