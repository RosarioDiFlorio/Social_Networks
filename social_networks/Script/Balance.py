#!/usr/bin/python

from math import exp 

#Computes the winners when advertisers have a budget.
#It takes in input:
#- the slots' clickthrough rates
#- the advertisers' bids
#- the advertisers' starting budgets
#- the advertisers' current budgets
#- the current query
def balance(slot_ctrs, adv_bids, adv_sbudgets, adv_cbudgets, query):
    query_winners=dict()
    query_pay=dict()
    
    psi=dict()
    
    #Only consider advertisers that have a bid for this query
    for advs in adv_bids[query].keys():
        #Only consider advertisers that have enough budget to pay this bid
        if adv_cbudgets[advs] >= adv_bids[query][advs]:
            #The weight assigned to each advertiser is a tradeoff between his bid and the fraction of budget that is still available
            psi[advs] = adv_bids[query][advs]*(1-exp(-adv_cbudgets[advs]/adv_sbudgets[advs]))
            
    #Slots are assigned to advertisers in order of weight (and not simply in order of bid)
    sorted_slot = sorted(slot_ctrs[query].keys(), key=slot_ctrs[query].__getitem__, reverse=True)
    sorted_advs = sorted(psi.keys(), key=psi.__getitem__, reverse = True)
    
    for i in range(min(len(sorted_slot),len(sorted_advs))):
        query_winners[sorted_slot[i]] = sorted_advs[i]
        query_pay[sorted_advs[i]] = adv_bids[query][sorted_advs[i]] #Here, we use first price auction: winner advertisers pay exactly their bid
    
    return query_winners, query_pay