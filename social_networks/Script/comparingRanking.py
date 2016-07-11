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

for d in HITS:
	tmp_a[d] = HITS[d]["a"]
	tmp_h[d] = HITS[d]["h"]
	tmp_tot[d] = HITS[d]["a"] + HITS[d]["h"]

HITS_A = OrderedDict(sorted(tmp_a.items(), key = operator.itemgetter(1), reverse=True))
HITS_H = OrderedDict(sorted(tmp_h.items(), key = operator.itemgetter(1), reverse=True))
HITS_tot = OrderedDict(sorted(tmp_tot.items(), key = operator.itemgetter(1), reverse=True))


PageRank_key = list(PageRank.keys())
HITS_A_key = list(HITS_A.keys())
HITS_H_key = list(HITS_H.keys())
HITS_tot_key = list(HITS_tot.keys())


#code for write in a xlsx file
filename = "risultati_Rank2.xlsx"
sheet = "result_ranking"

book = xlwt.Workbook(encoding="utf-8")
sheet1 = book.add_sheet(sheet)

vertex = 0
colPagerankValue = 1
colHitsTOTValue = 2

sheet1.write(0,vertex, "vertex")
sheet1.write(0,colPagerankValue, "PageRank Value")
sheet1.write(0,colHitsTOTValue, "Hits TOT Value")

valMax = len(PageRank)
valtmp = valMax
#print(valMax)

pr = dict()
hits = dict()

for i,k in enumerate(PageRank_key):
        
	j_t = HITS_tot_key.index(k)
        pr[i] = float(valtmp)/valMax
	hits[j_t] = float(valtmp)/valMax
	
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
        sheet1.write(row, colHitsTOTValue, hits[arr_shuffle[i]])
    
        row += 1
        
book.save(filename)