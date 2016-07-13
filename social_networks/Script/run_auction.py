from random import randint, random, uniform
from Balance import *

def run_auction(test_name, num_query, queries, slot_ctrs, adv_values, adv_budgets, adv_bots, threshold, tp):
    history=[]
    adv_bids=dict()
    adv_bids_h = -1
    #Generate a random sequence of num_query queries, with each query selected from the list queries
    query_sequence=[]
    tot_ut = 0
    for i in range(num_query):
        #query_sequence.append("prova")
        query_sequence.append(queries[randint(0,len(queries)-1)])
                              
    #print(query_sequence)

    adv_cbudgets=adv_budgets.copy() #The current budgets of advertisers
    revenue=0 #The current revenue of the auctioneer

    test_name_val = 0

    for i in range(num_query):
        done = True
        current_query = query_sequence[i]
        
        adv_bids[current_query]=dict()
        for adv in adv_values[current_query]:
            if adv != test_name:
                returns = adv_bots[adv](adv, adv_values[current_query][adv], threshold, adv_budgets[adv], adv_cbudgets[adv], slot_ctrs, history, current_query, tp)
                adv_bids[current_query][adv] = returns[1]

            returns = adv_bots[test_name](test_name, adv_values[current_query][test_name], threshold, adv_budgets[test_name], adv_cbudgets[test_name], slot_ctrs, history, current_query, tp)
            adv_bids[current_query][test_name] = returns[1]

            '''
            print "Bid of ", adv, '{0:.16f}'.format(adv_bids[current_query][adv])
            if i != 0:
                print "History of ", adv, '{0:.16f}'.format(history[i-1][current_query]["adv_bids"][current_query][adv])
            '''

            for s in range(1, i+1):
                if current_query in history[i-s]:
                    adv_bids_h = history[i-s][current_query]["adv_bids"][current_query][adv]
                    break
                if i-s == 0:
                    adv_bids_h = -1

            if i == 0 or adv_bids[current_query][adv] != adv_bids_h:
                done = False

        #For each query we use the balance algorithm for evaluating the assignment and the payments
        #query_winners, query_pay = balance_fpa(slot_ctrs, adv_bids, adv_budgets, adv_cbudgets, query_sequence[i])
        if tp ==  "gsp":
            query_winners, query_pay = balance_gsp(slot_ctrs, adv_bids, adv_budgets, adv_cbudgets, current_query)
        elif tp == "fpa":
            query_winners, query_pay = balance_fpa(slot_ctrs, adv_bids, adv_budgets, adv_cbudgets, current_query)


        #print(query_winners)

        #print(returns[0]["slot"])
        pref_id = returns[0]["slot"]
        obt_id = "id1000"
        for n in query_winners:
            if query_winners[n] == test_name:
                obt_id = n
        if pref_id == "none":
            pref_id = "id1000"

        pref_id_num = int(pref_id.replace("id", ""))
        obt_id_num = int(obt_id.replace("id", ""))

        if obt_id_num != 1000:
            tot_ut += slot_ctrs[current_query][obt_id]*(adv_values[current_query][test_name] - query_pay[test_name])

        #print(pref_id_num, obt_id_num)
        if pref_id_num > obt_id_num:
           #print("he got better")
           test_name_val += 2
        elif pref_id_num < obt_id_num:
           #print("he got worst")
           test_name_val -= 1
        else:
           #print("go what he wants")
           test_name_val += 1

            #print test_name_val
        
        '''
        print("------Current Query------")
        print ("\t\t" + str(current_query))
        print("------Query Winners------")
        print ("\t\t" + str(query_winners))
        print("------Query Pay------")
        print ("\t\t" + str(query_pay))
        print("------Current Budget------")
        print ("\t\t" + str(adv_cbudgets))
        '''

        #Update the history
        history.append(dict())
        history[i][current_query]=dict()
        history[i][current_query]["adv_bids"]=dict(adv_bids)
        history[i][current_query]["adv_slots"]=dict(query_winners)
        history[i][current_query]["adv_pays"]=dict(query_pay)
        

        for j in query_winners.keys():
            #We now simulate an user clicking on the ad with a probability that is equivalent to the slot's clickthrough rate
            #p = random() # A number chosen uniformly at random between 0 and 1
            p = uniform(0, 1)
            if p < slot_ctrs[query_sequence[i]][j]: #This event occurrs with probability that is exactly slot_ctrs[query_sequence[i]][j]
                adv_cbudgets[query_winners[j]] -= query_pay[query_winners[j]]
                revenue += query_pay[query_winners[j]]

        if done:
            print i
            print history[i]
            return float(test_name_val)/i, tot_ut, revenue
        #print(current_query, query_winners, query_pay, adv_cbudgets)
        
    print i
    print history[i-1]
    print history[i]
    return float(test_name_val)/i, tot_ut, revenue