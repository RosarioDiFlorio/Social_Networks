#!/usr/bin/python

from run_auction import *
import Bots
import xlwt
import random

def testBots(bots,queries,slot_ctrs,adv_values,adv_budgets,main_bot = "x",num_query = 1,threshold = 0,allequals = True,rep = 1,randomTest=False):
  
    #Advertisers' bots
    adv_bots=dict()

    tps = ['gsp', 'fpa']
    
    returnValue = dict()
    if not allequals:
        for tp in tps:
            returnValue[tp] = dict()
            for my_bot in bots[1:len(bots)]:
                if(my_bot == "random"):
                    continue
                returnValue[tp][my_bot] = dict()
                for adv_bot in bots[1:len(bots)]:

                    #print ("AUCTION: " + tp + " I: " + my_bot + " ENEMIES: " + adv_bot)

                    adv_bots["x"] = getattr(Bots, my_bot)
                    adv_bots["y"] = getattr(Bots, adv_bot)
                    adv_bots["z"] = getattr(Bots, adv_bot)

                    ut_val = 0
                    tot_rev = 0
                    
                    
                    for i in range(rep):
                        
                        if(randomTest):
                            slot_ctrs["query1"]=dict()
                            slot_ctrs["query1"]["id1"] = float("{0:.2f}".format(random.uniform(0, 1)))
                            slot_ctrs["query1"]["id2"] = float("{0:.2f}".format(random.uniform(0, 1)))

                            slot_ctrs["query2"]=dict()
                            slot_ctrs["query2"]["id1"] = float("{0:.2f}".format(random.uniform(0, 1)))
                            slot_ctrs["query2"]["id2"] = float("{0:.2f}".format(random.uniform(0, 1)))

                            slot_ctrs["query3"]=dict()
                            slot_ctrs["query3"]["id1"] = float("{0:.2f}".format(random.uniform(0, 1)))
                            slot_ctrs["query3"]["id2"] = float("{0:.2f}".format(random.uniform(0, 1)))

                            #print "slot_ctrs" + str(slot_ctrs)

                            #For each query, lists the advertisers that have a interest in that query

                            adv_values["query1"]=dict()
                            adv_values["query1"]["x"] = random.randint(0,10)
                            adv_values["query1"]["y"] = random.randint(0,10)
                            adv_values["query1"]["z"] = random.randint(0,10)

                            adv_values["query2"]=dict()
                            adv_values["query2"]["x"] = random.randint(0,10)
                            adv_values["query2"]["y"] = random.randint(0,10)
                            adv_values["query2"]["z"] = random.randint(0,10)

                            adv_values["query3"]=dict()
                            adv_values["query3"]["x"] = random.randint(0,10)
                            adv_values["query3"]["y"] = random.randint(0,10)
                            adv_values["query3"]["z"] = random.randint(0,10)

                            #print "adv_values" + str(adv_values)

                            #The initial budget of each advertisers

                            adv_budgets["x"] = random.randint(50,500)
                            adv_budgets["y"] = random.randint(50,500)
                            adv_budgets["z"] = random.randint(50,500)

                            #print "adv_budgets" + str(adv_budgets)
                        
                        tmp = run_auction(main_bot, num_query, queries, slot_ctrs, adv_values, adv_budgets, adv_bots, threshold ,tp)
                        ut  = tmp[0]
                        rev = tmp[1]
                        
                        ut_val += ut 
                        tot_rev += rev
                    #print ("Bot selezionato: " + str(main_bot))
                    #print ("Totale Uti:\t\t" + str(float(ut_val)/rep))
                    #print ("Totale Rev:\t\t" + str(float(tot_rev)/rep))
                    
                    #debug
                    #raw_input("Press Enter to continue...")
                    returnValue[tp][my_bot][adv_bot] = dict()
                    returnValue[tp][my_bot][adv_bot]['util'] = str(float(ut_val)/rep)
                    returnValue[tp][my_bot][adv_bot]['rev'] = str(float(tot_rev)/rep)
                    
    else:
       
        for tp in tps:
                returnValue[tp] = dict()
                for adv_bot in bots[1:len(bots)]:
                    my_bot = adv_bot
                    
                    #print ("AUCTION: " + tp + " I: ALL PLAYER USE: " + adv_bot)

                    adv_bots["x"] = getattr(Bots, my_bot)
                    adv_bots["y"] = getattr(Bots, adv_bot)
                    adv_bots["z"] = getattr(Bots, adv_bot)

                    ut_val = 0
                    tot_rev = 0
                    
                    
                    for i in range(rep):
                        if(randomTest):
                            slot_ctrs["query1"]=dict()
                            slot_ctrs["query1"]["id1"] = float("{0:.2f}".format(random.uniform(0, 1)))
                            slot_ctrs["query1"]["id2"] = float("{0:.2f}".format(random.uniform(0, 1)))

                            slot_ctrs["query2"]=dict()
                            slot_ctrs["query2"]["id1"] = float("{0:.2f}".format(random.uniform(0, 1)))
                            slot_ctrs["query2"]["id2"] = float("{0:.2f}".format(random.uniform(0, 1)))

                            slot_ctrs["query3"]=dict()
                            slot_ctrs["query3"]["id1"] = float("{0:.2f}".format(random.uniform(0, 1)))
                            slot_ctrs["query3"]["id2"] = float("{0:.2f}".format(random.uniform(0, 1)))

                            #print "slot_ctrs" + str(slot_ctrs)

                            #For each query, lists the advertisers that have a interest in that query

                            adv_values["query1"]=dict()
                            adv_values["query1"]["x"] = random.randint(0,10)
                            adv_values["query1"]["y"] = random.randint(0,10)
                            adv_values["query1"]["z"] = random.randint(0,10)

                            adv_values["query2"]=dict()
                            adv_values["query2"]["x"] = random.randint(0,10)
                            adv_values["query2"]["y"] = random.randint(0,10)
                            adv_values["query2"]["z"] = random.randint(0,10)

                            adv_values["query3"]=dict()
                            adv_values["query3"]["x"] = random.randint(0,10)
                            adv_values["query3"]["y"] = random.randint(0,10)
                            adv_values["query3"]["z"] = random.randint(0,10)

                            #print "adv_values" + str(adv_values)

                            #The initial budget of each advertisers

                            adv_budgets["x"] = random.randint(50,500)
                            adv_budgets["y"] = random.randint(50,500)
                            adv_budgets["z"] = random.randint(50,500)

                            #print "adv_budgets" + str(adv_budgets)
                        tmp = run_auction(main_bot, num_query, queries, slot_ctrs, adv_values, adv_budgets, adv_bots, threshold ,tp)
                        ut  = tmp[0]
                        rev = tmp[1]
                        
                        ut_val += ut 
                        tot_rev += rev
                    #print ("Bot selezionato: " + str(main_bot))
                    #print ("Totale Uti:\t\t" + str(float(ut_val)/rep))
                    #print ("Totale Rev:\t\t" + str(float(tot_rev)/rep))
                    
                    #debug
                    #raw_input("Press Enter to continue...")
                    returnValue[tp][my_bot] = dict()
                    returnValue[tp][my_bot][adv_bot] = dict()
                    returnValue[tp][my_bot][adv_bot]['util'] = str(float(ut_val)/rep)
                    returnValue[tp][my_bot][adv_bot]['rev'] = str(float(tot_rev)/rep)
    return returnValue
    




bots = [
            'best_response', 
            'best_response_competitive',
            'best_response_altruistic', 
            'competitor', 
            'budget_saving',
            'random', 
            'threshold_budget',
            'preferential_budget', 
            'altruistic_budget', 
            'competitor_budget'
            ]



#####################TEST STATICO#########################
#All possible queries
queries=["query1"]

slot_ctrs = dict()

#For each query, lists the available slots and their clickthrough rate
slot_ctrs["query1"]=dict()
slot_ctrs["query1"]["id1"] = 1
slot_ctrs["query1"]["id2"] = 0.80

slot_ctrs["query2"]=dict()
slot_ctrs["query2"]["id1"] = 0.50
slot_ctrs["query2"]["id2"] = 0.30

slot_ctrs["query3"]=dict()
slot_ctrs["query3"]["id1"] = 0.70
slot_ctrs["query3"]["id2"] = 0.30

#For each query, lists the advertisers that have a interest in that query
adv_values=dict()
adv_values["query1"]=dict()
adv_values["query1"]["x"] = 10
adv_values["query1"]["y"] = 10
adv_values["query1"]["z"] = 10

adv_values["query2"]=dict()
adv_values["query2"]["x"] = 5
adv_values["query2"]["y"] = 5
adv_values["query2"]["z"] = 5

adv_values["query3"]=dict()
adv_values["query3"]["x"] = 9
adv_values["query3"]["z"] = 9
adv_values["query3"]["z"] = 9

#The initial budget of each advertisers
adv_budgets=dict()
adv_budgets["x"] = 100
adv_budgets["y"] = 100
adv_budgets["z"] = 100

main_bot = "x"
iterations = 500

#lenght of the sequence of queries that we will consider
num_query= 1
threshold = 0



#write result in xls file
filename = "risultati_bots_test_statico.xls"
sheetgsp = "gsp"
sheetfpa = "fpa"
book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet(sheetgsp)
sheet2 = book.add_sheet(sheetfpa)


colBehavior = 2
colAu = 3
colUtil = 4
colRev = 5
colEnemies = 6
flagName = True


tmp = testBots(bots,queries,slot_ctrs,adv_values,adv_budgets,main_bot,num_query,threshold,False,iterations,False)
#print("RIPETIZIONI: " + str(i))
row = 0
if flagName:
    sheet1.write(row,colBehavior,"Player")
    sheet1.write(row,colAu,"tipo asta")
sheet1.write(row,colUtil,"utility")
sheet1.write(row,colRev,"revenue")
sheet1.write(row,colEnemies,"enemies")
#debug
#raw_input("Press Enter to continue...")



row += 1
for tp in tmp:
    #print(tmp[tp])
    for be in tmp[tp]:
        for en in tmp[tp][be]:
            sheetToWrite = sheet1
            if tp == "gsp":
                sheetToWrite = sheet1
            else:
                sheetToWrite = sheet2
            if flagName:
                sheetToWrite.write(row,colBehavior,str(be))
                sheetToWrite.write(row,colAu,str(tp))
            sheetToWrite.write(row,colUtil,float(tmp[tp][be][en]["util"]))
            sheetToWrite.write(row,colRev,float(tmp[tp][be][en]["rev"]))
            sheetToWrite.write(row,colEnemies,str(en))
            
            
            row +=1
flagName = False

colBehavior += 5
colAu += 5
colUtil += 5
colRev += 5
colEnemies += 5





flagName = False

book.save(filename) 



#####################TEST DINAMICO#########################


print("----------ASTA--------------")

#write result in xls file
filename = "risultati_bots_test_dinamico.xls"
sheetgsp = "gsp"
sheetfpa = "fpa"

book = xlwt.Workbook(encoding="utf-8")

sheet1 = book.add_sheet(sheetgsp)
sheet2 = book.add_sheet(sheetfpa)



#All possible queries
queries=["query1", "query2" , "query3"]



#For each query, lists the available slots and their clickthrough rate
slot_ctrs=dict()

#For each query, lists the advertisers that have a interest in that query
adv_values=dict()

#The initial budget of each advertisers
adv_budgets=dict()




main_bot = "x"
iterations = 500

#lenght of the sequence of queries that we will consider
num_query= 10
threshold = 0

colBehavior = 2
colAu = 3
colUtil = 4
colRev = 5
colEnemies = 6
flagName = True




#print("RIPETIZIONI: " + str(i))

#For each query, lists the available slots and their clickthrough rate

slot_ctrs["query1"]=dict()
slot_ctrs["query1"]["id1"] = float("{0:.2f}".format(random.uniform(0, 1)))
slot_ctrs["query1"]["id2"] = float("{0:.2f}".format(random.uniform(0, 1)))

slot_ctrs["query2"]=dict()
slot_ctrs["query2"]["id1"] = float("{0:.2f}".format(random.uniform(0, 1)))
slot_ctrs["query2"]["id2"] = float("{0:.2f}".format(random.uniform(0, 1)))

slot_ctrs["query3"]=dict()
slot_ctrs["query3"]["id1"] = float("{0:.2f}".format(random.uniform(0, 1)))
slot_ctrs["query3"]["id2"] = float("{0:.2f}".format(random.uniform(0, 1)))

#print "slot_ctrs" + str(slot_ctrs)

#For each query, lists the advertisers that have a interest in that query

adv_values["query1"]=dict()
adv_values["query1"]["x"] = random.randint(0,10)
adv_values["query1"]["y"] = random.randint(0,10)
adv_values["query1"]["z"] = random.randint(0,10)

adv_values["query2"]=dict()
adv_values["query2"]["x"] = random.randint(0,10)
adv_values["query2"]["y"] = random.randint(0,10)
adv_values["query2"]["z"] = random.randint(0,10)

adv_values["query3"]=dict()
adv_values["query3"]["x"] = random.randint(0,10)
adv_values["query3"]["y"] = random.randint(0,10)
adv_values["query3"]["z"] = random.randint(0,10)

#print "adv_values" + str(adv_values)

#The initial budget of each advertisers

adv_budgets["x"] = random.randint(50,500)
adv_budgets["y"] = random.randint(50,500)
adv_budgets["z"] = random.randint(50,500)

#print "adv_budgets" + str(adv_budgets)

tmp = testBots(bots,queries,slot_ctrs,adv_values,adv_budgets,main_bot,num_query,threshold,False,iterations,False)
row = 0
if flagName:
    sheet1.write(row,colBehavior,"Player")
    sheet1.write(row,colAu,"tipo asta")
sheet1.write(row,colUtil,"utility")
sheet1.write(row,colRev,"revenue")
sheet1.write(row,colEnemies,"enemies")
#debug
#raw_input("Press Enter to continue...")

            
row += 1
for tp in tmp:
    #print(tmp[tp])
    for be in tmp[tp]:
        for en in tmp[tp][be]:
            sheetToWrite = sheet1
            if tp == "gsp":
                sheetToWrite = sheet1
            else:
                sheetToWrite = sheet2
            if flagName:
                sheetToWrite.write(row,colBehavior,str(be))
                sheetToWrite.write(row,colAu,str(tp))
            sheetToWrite.write(row,colUtil,float(tmp[tp][be][en]["util"]))
            sheetToWrite.write(row,colRev,float(tmp[tp][be][en]["rev"]))
            sheetToWrite.write(row,colEnemies,str(en))
            
            row +=1
flagName = False
colBehavior += 5
colAu += 5
colUtil += 5
colRev += 5
colEnemies += 5



flagName = False


book.save(filename)

print("------------FINE---------------")