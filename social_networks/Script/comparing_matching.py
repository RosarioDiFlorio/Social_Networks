from load_dataset import *
from collections import OrderedDict
import operator
import xlwt

confidence = ["0.0001",
              "1e-05",
              "1e-06",
              "1e-07"
              ]

for c in confidence:

    result_match = get_match_res()
    result_opt_match = get_match_opt_res()

    PageRank = get_PageRank_confidence(c)
    HITS = get_HITS_confidence(c)

    seturl = dict()
    
    for w in result_match:
        seturl[w] = dict()
        seturl[w].update(result_match[w])
        seturl[w].update(result_opt_match[w])
        seturl[w] = OrderedDict(sorted(seturl[w].items(), key = operator.itemgetter(1),reverse = True ))
    '''
    for w in seturl:
        print w
        for l in seturl[w]:
            print seturl[w][l]
    '''    
        
        
        
        
            

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
    filename = "risultati_matching_w_"+c+".xls"
    sheet = "result_matching"

    book = xlwt.Workbook(encoding="utf-8")
    sheet1 = book.add_sheet(sheet)

    URL = 0
    score= 1
    BM = 2
    BMOPT = 3
    pagerankBM = 4
    hitsBM = 5

    pagerankBMOPT = 6
    hitsBMOPT = 7
    

    sheet1.write(0,URL,"Document")
    sheet1.write(0,BM ,"BM")
    sheet1.write(0,BMOPT,"BMOPT")
    sheet1.write(0,pagerankBM,"PageRank BM")
    sheet1.write(0,pagerankBMOPT,"PageRank BMOPT")
    sheet1.write(0,hitsBM, "Hits BM")
    sheet1.write(0,hitsBMOPT, "Hits BMOPT")
    sheet1.write(0,score, "Score")
    row = 1
    for i in seturl:
        #print i
        for k in seturl[i]:
            sheet1.write(row,URL, str(k))
            sheet1.write(row,score,str(seturl[i][k]))
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




        




