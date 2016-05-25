#!/usr/bin/python

from GSP import *

#Slots' clickthrough rates
slot_ctrs=dict()
slot_ctrs["id1"] = 10
slot_ctrs["id2"] = 4

#Advertisers' values
adv_values=dict()
adv_values["x"] = 10
adv_values["y"] = 11
adv_values["z"] = 12

#Advertisers' bots
adv_bots=dict()
adv_bots["x"] = best_response_competitive
adv_bots["y"] = best_response_competitive
adv_bots["z"] = best_response_competitive

step=0
history=[]
adv_bids=dict()

done=False
max_step=100

#We repeat the auctions as long as an equilibrium has not been reached.
#(This mean that advertisers submit the same bids in any successive repetition.)
#If an equilibrium is not reached in short time, then we stop after max_step steps
while not done and step < max_step:
        
        done = True
        for i in adv_values.keys():
            #Invoke the bots for computing the bids for each advertiser
            adv_bids[i] = adv_bots[i](i,adv_values[i],slot_ctrs,history)
            #If it is the first step or there is at least one advertiser whose bid is different from the bid submitted in the previous step,
            #then we need another iteration, otherwise we can stop
            
            if step == 0 or adv_bids[i] != history[step-1]["adv_bids"][i]:
                done=False
            
                
        if done:
            break
        
        #Execute the GSP auction with the bids computed above
        adv_slots, adv_pays = gsp(slot_ctrs,adv_bids)
        
        #Update the history
        history.append(dict())
        history[step]["adv_bids"]=dict(adv_bids)
        history[step]["adv_slots"]=dict(adv_slots)
        history[step]["adv_pays"]=dict(adv_pays)
        
        print(step, history[step])
        
        step += 1