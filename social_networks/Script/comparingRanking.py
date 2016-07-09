from load_dataset import * 
from collections import OrderedDict
import operator

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


for i,k in enumerate(PageRank_key):

	j_a = HITS_A_key.index(k)
	j_h = HITS_H_key.index(k)
	j_t = HITS_tot_key.index(k)
	print(i,j_a)
	print(i,j_h)
	print(i,j_t)
