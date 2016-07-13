from load_dataset import * 
from collections import OrderedDict
import operator
import xlwt
import random

PageRank = get_PageRank_graph()
HITS = get_HITS_graph()

PageRank = OrderedDict(sorted(PageRank.items(), key = operator.itemgetter(1), reverse=True))

tmp_a = dict()
tmp_h = dict()
tmp_tot = dict()
tmp_weighted = dict() 

for d in HITS:
	tmp_a[d] = HITS[d]["a"]
	tmp_h[d] = HITS[d]["h"]
	tmp_tot[d] = HITS[d]["a"] + HITS[d]["h"]
        tmp_weighted[d] = float(HITS[d]["a"] * 0.6) + HITS[d]["h"] * 0.4
        
HITS_A = OrderedDict(sorted(tmp_a.items(), key = operator.itemgetter(1), reverse=True))
HITS_H = OrderedDict(sorted(tmp_h.items(), key = operator.itemgetter(1), reverse=True))
HITS_tot = OrderedDict(sorted(tmp_tot.items(), key = operator.itemgetter(1), reverse=True))
HITS_W = OrderedDict(sorted(tmp_weighted.items(), key = operator.itemgetter(1), reverse=True))

PageRank_key = list(PageRank.keys())
HITS_A_key = list(HITS_A.keys())
HITS_H_key = list(HITS_H.keys())
HITS_tot_key = list(HITS_tot.keys())
HITS_W_key = list(HITS_W.keys())

#code for write in a xlsx file
filename = "risultati_Rank_weighted.xlsx"
sheet = "result_ranking"

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet(sheet)

vertex = 0
colPagerankValue = 1
colHitsAValue = 2
colHitsHValue = 3
colHitsTOTValue = 4
colHitsWValue = 5

sheet1.write(0,vertex, "vertex")
sheet1.write(0,colPagerankValue, "PageRank Value")
sheet1.write(0,colHitsAValue, "Hits A Value")
sheet1.write(0,colHitsHValue, "Hits H Value")
sheet1.write(0,colHitsTOTValue, "Hits TOT Value")
sheet1.write(0,colHitsWValue, "Hits Weighted Value")

valMax = len(PageRank)
valtmp = valMax
#print(valMax)

pr = dict()
hits_a = dict()
hits_h = dict()
hits_tot = dict()
hits_w = dict()
for i,k in enumerate(PageRank_key):
        
        j_a = HITS_A_key.index(k)
        j_h = HITS_H_key.index(k)
	j_t = HITS_tot_key.index(k)
	j_w = HITS_W_key.index(k)
	
        pr[i] = float(valtmp)/valMax
	hits_a[j_a] = float(valtmp)/valMax
	hits_h[j_h] = float(valtmp)/valMax
	hits_tot[j_t] = float(valtmp)/valMax
	hits_w[j_w] = float(valtmp)/valMax
	
	valtmp -= 1
        

print("shuffle dictionaries")
#shuffle dict for write shuffle nodes in xlsx file

arr_shuffle = dict()
for i in range(len(PageRank)):
    arr_shuffle[i] = i
    
random.shuffle(arr_shuffle)
 
row = 2
print("print in file")
for i in arr_shuffle:
        
        sheet1.write(row, vertex, str(arr_shuffle[i]))
        sheet1.write(row, colPagerankValue,pr[arr_shuffle[i]])
        sheet1.write(row, colHitsAValue, hits_a[arr_shuffle[i]])
        sheet1.write(row, colHitsHValue, hits_h[arr_shuffle[i]])
        sheet1.write(row, colHitsTOTValue, hits_tot[arr_shuffle[i]])
        sheet1.write(row, colHitsWValue, hits_w[arr_shuffle[i]])
    
        row += 1
        
book.save(filename)