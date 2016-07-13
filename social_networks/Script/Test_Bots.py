#!/usr/bin/python
from run_auction import *
import Bots

#All possible queries
queries=["prova"]
tp = "fpa"
#For each query, lists the available slots and their clickthrough rate
slot_ctrs=dict()
slot_ctrs["prova"]=dict()
slot_ctrs["prova"]["id1"] = 1
slot_ctrs["prova"]["id2"] = 1

slot_ctrs["test"]=dict()
slot_ctrs["test"]["id1"] = 0.33
slot_ctrs["test"]["id2"] = 0.30

slot_ctrs["esempio"]=dict()
slot_ctrs["esempio"]["id1"] = 0.25
slot_ctrs["esempio"]["id2"] = 0.30

#For each query, lists the advertisers that have a interest in that query
adv_values=dict()
adv_values["prova"]=dict()
adv_values["prova"]["x"] = 7
adv_values["prova"]["y"] = 7
adv_values["prova"]["z"] = 7

adv_values["test"]=dict()
adv_values["test"]["x"] = 5
adv_values["test"]["y"] = 5
adv_values["test"]["z"] = 5

adv_values["esempio"]=dict()
adv_values["esempio"]["x"] = 9
adv_values["esempio"]["z"] = 9
adv_values["esempio"]["z"] = 9

#The initial budget of each advertisers
adv_budgets=dict()
adv_budgets["x"] = 100000
adv_budgets["y"] = 100000
adv_budgets["z"] = 100000

#Advertisers' bots
adv_bots=dict()

test_name = "x"

#It denotes the lenght of the sequence of queries that we will consider
num_query=1000
threshold = 0

tps = ['gsp', 'fpa']
bots = ['best_response', 'best_response_competitive', 'best_response_altruistic', 'competitor', 'budget_saving', 'random',  'competitor_budget', 'preferential_competitor', 'best_competitor_budget', 'best_preferential_competitor']
for tp in tps:
    for my_bot in bots[1:2]:
        for adv_bot in bots[1:2]:

            print ("AUCTION: " + tp + " I: " + my_bot + " ENEMIES: " + adv_bot)

            adv_bots["x"] = getattr(Bots, my_bot)
            adv_bots["y"] = getattr(Bots, adv_bot)
            adv_bots["z"] = getattr(Bots, adv_bot)

            tot_val = 0
            ut_val = 0
            tot_rev = 0
            rep = 1
            for i in range(rep):
                tmp = run_auction(test_name, num_query, queries, slot_ctrs, adv_values, adv_budgets, adv_bots, threshold ,tp)
                val = tmp[0]
                ut  = tmp[1]
                rev = tmp[2]
                #print(val)
                tot_val += val
                ut_val += ut 
                tot_rev += rev

            print ("Totale Val:\t\t" + str(float(tot_val)/rep))
            print ("Totale Uti:\t\t" + str(float(ut_val)/rep))
            print ("Totale Rev:\t\t" + str(float(tot_rev)/rep))



