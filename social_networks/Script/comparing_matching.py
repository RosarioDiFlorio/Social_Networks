from load_dataset import *
from collections import OrderedDict
import operator
import xlwt

result_match = get_match_res()
result_opt_match = get_match_opt_res()

PageRank = get_PageRank_graph()
HITS = get_HITS_graph()





match_ranked = dict()
for w in result_match:
    
    
    match_ranked[w] = dict()
    match_ranked[w]["PageRank"] = dict()
    match_ranked[w]["HITS"] = dict()
    for l in result_match[w]:
        #print(l)
        match_ranked[w]["PageRank"][l] = PageRank[l] 
        match_ranked[w]["PageRank"] = OrderedDict(sorted(match_ranked[w]["PageRank"].items(), key = operator.itemgetter(1), reverse = True))
        ahits = HITS[l]["a"]
        hhits = HITS[l]["h"]
        thits = float(ahits * 0.6) + hhits * 0.4
        
        match_ranked[w]["HITS"][l] = thits
       
        match_ranked[w]["HITS"] = OrderedDict(sorted(match_ranked[w]["HITS"].items(), key = operator.itemgetter(1), reverse = True))
        #print(match_ranked[w]["PageRank"][l])

match_ranked_opt = dict()
for w in result_opt_match:
    
    
    match_ranked_opt[w] = dict()
    match_ranked_opt[w]["PageRank"] = dict()
    match_ranked_opt[w]["HITS"] = dict()
    for l in result_opt_match[w]:
        #print(l)
        match_ranked_opt[w]["PageRank"][l] = PageRank[l] 
        match_ranked_opt[w]["PageRank"] = OrderedDict(sorted(match_ranked_opt[w]["PageRank"].items(), key = operator.itemgetter(1), reverse = True))
        ahits = HITS[l]["a"]
        hhits = HITS[l]["h"]
        thits = float(ahits * 0.6) + hhits * 0.4
        
        match_ranked_opt[w]["HITS"][l] = thits
       
        match_ranked_opt[w]["HITS"] = OrderedDict(sorted(match_ranked_opt[w]["HITS"].items(), key = operator.itemgetter(1), reverse = True))
        #print(match_ranked[w]["PageRank"][l])
 
newd = OrderedDict()
for  q in sorted( match_ranked, key = lambda x:len(match_ranked[x]["PageRank"]), reverse = True ):
    newd[q] = match_ranked[q]
    
newd_opt = OrderedDict()
for  q in sorted( match_ranked_opt, key = lambda x:len(match_ranked_opt[x]["PageRank"]), reverse = True ):
    newd_opt[q] = match_ranked_opt[q]

         

dictUrl = dict()

count = 0
for doc in newd:
    dictUrl[doc] = set()
    for l in newd[doc]["PageRank"]:
        dictUrl[doc].add(l)
    
    for l in newd[doc]["HITS"]:
        dictUrl[doc].add(l)

    for l in newd_opt[doc]["PageRank"]:
        dictUrl[doc].add(l)
    
    for l in newd_opt[doc]["HITS"]:
        dictUrl[doc].add(l)
    if count > 50:break
    #break
    count += 1
    



#code for write in a xlsx file
filename = "risultati_matching_w.xls"
sheet = "result_matching"

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet(sheet)

URL = 0
BM = 1
BMOPT = 2
pagerankBM = 3
hitsBM = 4

pagerankBMOPT = 5
hitsBMOPT = 6

sheet1.write(0,URL,"Document")
sheet1.write(0,BM ,"BM")
sheet1.write(0,BMOPT,"BMOPT")
sheet1.write(0,pagerankBM,"PageRank BM")
sheet1.write(0,pagerankBMOPT,"PageRank BMOPT")
sheet1.write(0,hitsBM, "Hits BM")
sheet1.write(0,hitsBMOPT, "Hits BMOPT")
    

row = 1
for i in dictUrl:
    for k in dictUrl[i]:
        sheet1.write(row,URL, str(k))
        if k in newd[i]["PageRank"]:
            sheet1.write(row,BM, "Y")
        else:
            sheet1.write(row,BM, "N")
        if k in newd_opt[i]["PageRank"]:
            sheet1.write(row,BMOPT, "Y")
        else:
            sheet1.write(row,BMOPT, "N")
        pos = 1
        for j in newd[i]["PageRank"]:
            if k == j:
               sheet1.write(row,pagerankBM, str(pos))
            pos +=1
        
        pos = 1
        for j in newd[i]["HITS"]:
            if k == j:
               sheet1.write(row,hitsBM, str(pos))
            pos +=1
        
        pos = 1
        for j in newd_opt[i]["PageRank"]:
            if k == j:
               sheet1.write(row,pagerankBMOPT, str(pos))
            pos +=1
        
        pos = 1
        for j in newd_opt[i]["HITS"]:
            if k == j:
               sheet1.write(row,hitsBMOPT, str(pos))
            pos +=1
        
        
        
        row += 1
    sheet1.write(row,URL, " ")
    row += 1
book.save(filename)




        




