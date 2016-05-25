#!/usr/bin/python

#Consider the following setting:
#1) For each query there is exactly one slot with clickthrough rate 1.
#2) Each advertisers can have bids for only a subset of queries and has a budget.
#3) Once an advertiser is assigned to a slot for the given query he pays exactly his bid (first price auction).
#4) The sequence of the queries is known in advance.
#Compute the assignment that maximizes the revenue of the auctioneer (of Google) in this setting,

#IF ADVERTISERS HAVE THE SAME BIDS FOR ALL QUERIES
#(BUT DIFFERENT ADVERTISERS MAY HAVE DIFFERENT BIDS),
#THEN THE PROBLEM CAN BE REDUCED TO FINDING A MAXIMUM b-MATCHING IN A BIPARTITE GRAPH.
#WE BUILD A BIPARTITE GRAPH AS FOLLOWS:
#    -ON THE LEFT SIDE THERE IS A VERTEX FOR EACH ADVERTISER
#    -ON THE RIGHT SIDE THERE IS A VERTEX FOR EACH QUERY IN THE QUERY SEQUENCE
#    -THERE IS AN EDGE BETWEEN AN ADVERTISER AND A QUERY ONLY IF THE ADVERTISER HAS A BID FOR THAT QUERY
#    -FOR EACH ADVERTISER i WE SET b_i = BUDGET / BID
#    -FOR EACH QUERY i WE SET b_i = 1
#THE GOAL IS TO FIND A MATCHING IN WHICH EACH NODE i APPEAR AT MOST b_i TIMES.
#ALGORITHMS SOLVING THIS PROBLEM ARE WELL KNOWN,
#AND SOME OF THESE CAN BE ALREADY IMPLEMENTED IN PYTHON.

#and evaluate how worse is the revenue returned by the balance algorithm in this setting.
#(Recall that the balance algorithm is online. Thus, it does not use the fact that the sequence of queries is known in advance.)

from math import factorial,exp
from Balance import balance
from random import random

n = 6 #Number of possible keywords
queries=[] 
for i in range(n):
    queries.append(i) #Each keyword is a number from 0 to n-1
    
slot_ctrs=dict()
adv_bids=dict()
for i in range(n):
    slot_ctrs[i]=dict()
    slot_ctrs[i]["id1"] = 1 #Each keyword has a single slot whose clickthrough rate is 1
    
    adv_bids[i]=dict()
    #Keyword i has i+1 advertisers bidding on it. We name these advertisers with number from 0 to i
    #Note that this implies there are n advertisers named whose name is a number from 0 to n-1
    #Advertiser 0 wants to appear on every query
    #Advertiser 1 wants to appear on every query except query 0
    #Advertiser n-1 wants to appear only on query n-1
    for j in range(i+1):
        adv_bids[i][j]=1 #Each advertiser has a bid of 1 for this query
        
#The budget of each advertiser is n!
adv_budgets=dict()
for i in range(n):
    adv_budgets[i]=factorial(n)
    
#The sequence of queries consists of n*n! queries.
#In particolar, the sequence consists of n rounds.
#At round i, there are n! occurrences of the query n-i-1.
#Thus, at round 0 there are n! occurrences of query n-1 (on which each advertiser would like to appear),
#at round 1 there are n! occurrences of query n-2 (on which only advertisers 0,...,n-2 would like to appear),
#at round n-1 there are n! occurrences of query 0 (on which only advertiser 0 would like to appear)
num_query=n*factorial(n)
query_sequence=[]
for i in range(n):
    for j in range(factorial(n)):
        query_sequence.append(queries[n-i-1])
        
#Next is the simulation of the auction    
adv_cbudgets=adv_budgets.copy() #The current budgets of advertisers
revenue=0 #The current revenue of the auctioneer

for i in range(num_query):
    #For each query we use the balance algorithm for evaluating the assignment and the payments
    query_winners, query_pay = balance(slot_ctrs, adv_bids, adv_budgets, adv_cbudgets, query_sequence[i])
    
    for j in query_winners.keys():
        #We now simulate an user clicking on the ad with a probability that is equivalent to the slot's clickthrough rate
        p = random() # A number chosen uniformly at random between 0 and 1
        if p <= slot_ctrs[query_sequence[i]][j]: #This event occurrs with probability that is exactly slot_ctrs[query_sequence[i]][j]
            adv_cbudgets[query_winners[j]] -= query_pay[query_winners[j]]
            revenue += query_pay[query_winners[j]]

print("Competitive Ratio:",float(revenue)/(n*factorial(n)))
print("Worst Competitive Ratio:",1-exp(-1))





