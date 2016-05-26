#!/usr/bin/python
from load_dataset import *
from Dataset_Matching import *

db_normal = db()
total_len_docs = len(db_normal.keys())
print total_len_docs
inverted_db = ordered_reverse_db()
query = "game differenziata"
print("QUERY: "+query)

result = best_match_opt(query, 0.02, inverted_db,total_len_docs)
print("BEST MATCH: "+str(result))
print "len: " + str(len(result))


'''
result2 = improved_best_match(query, inverted_db)
print("IMPROVED BEST MATCH: "+str(result2))
'''
