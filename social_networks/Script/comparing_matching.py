from load_dataset import *
from collections import OrderedDict
import operator


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

        #print(match_ranked[w]["PageRank"][l])
    for l in result_opt_match[w]:
        #print(l)
        match_ranked[w]["HITS"][l] = HITS[l]
        match_ranked[w]["HITS"] = OrderedDict(sorted(match_ranked[w]["HITS"].items(), key = operator.itemgetter(1), reverse = True))

 
newd = OrderedDict()
for  q in sorted( match_ranked, key = lambda x:len(match_ranked[x]["PageRank"]), reverse = True ):
    newd[q] = match_ranked[q]







        




