#!/usr/bin/python
from load_dataset import *
from Dataset_Matching import *
import timeit


def set_default(obj):
	if isinstance(obj,set):
		return list(obj)
	raise TypeError

def test_time_matching():
    db_normal = db()
    total_len_docs = len(db_normal.keys())


    inverted_db = ordered_reverse_db()

    nquery = 0
    elapsed = 0
    elapsed_opt = 0
    elapsed_global = 0
    elapsed_opt_global= 0
    niter = 10


    result = list()
    result_opt = list()

    files = ["query_l2.txt",
            "query_l3.txt",
            "query_l4.txt",
            "query_l5.txt",
            "query_l6.txt"
            ]
    for f in files:
        with open(f) as file:
            print("---------STARTING ---------")
            nquery = 0
            while True:
                query = file.readline()
                #print (" Num Query -> "+ str(nquery) + " Iterations -> " + str(niter))
                if query == "": break
                for i in range(niter):
                    
                    start_time = timeit.default_timer()
                    result = best_match(query, 0.02, inverted_db)
                    elapsed += timeit.default_timer() - start_time
                    
                    start_time = timeit.default_timer()
                    result_opt = best_match_opt(query, 0.02, inverted_db,total_len_docs)
                    elapsed_opt += timeit.default_timer() - start_time
                    
                elapsed_global += float(elapsed/niter)
                
                elapsed_opt_global += float(elapsed_opt/niter)
                
                elapsed = 0
                elapsed_opt = 0
                
                
                nquery += 1
                
            
            print("---------FINISHED---------")
            print("---------TIMES "+ f +"------------")
            print ("Num Iterations -> "+ str(niter))
            print ("Num Query -> " +str(nquery))
            print ("Time best_match -> "+ str(float(elapsed_global/nquery)))
            print ("Time best_match_opt -> "+ str(float(elapsed_opt_global/nquery)))
            print("--------------------------")

def test_result_matching():
    db_normal = db()
    total_len_docs = len(db_normal.keys())
    inverted_db = ordered_reverse_db()
    
    result_dict = dict()
    result_opt_dict = dict()
    
    result = dict()
    result_opt = dict()
    nquery = 0
    
    f = "query_adhoc.txt"
    print("---------STARTING ---------")
    with open(f) as file:
        while True:
            query = file.readline()
            query = str.lower(query)
            #print (" Query -> "+ query)
            if query == "": break
    
            result = best_match(query, 0.02, inverted_db)
            result_opt = best_match_opt(query, 0.02, inverted_db,total_len_docs)
            result_dict[query] = result
            result_opt_dict[query] = result_opt
            nquery += 1
    
    print("---------FINISHED---------")
    print("---------DUMP RESULT DOCUMENTS-------------")
    with open('result_match.json', 'w') as fp:
            stri = json.dumps(result_dict, ensure_ascii=False, encoding="utf-8", default = set_default)
            fp.write(stri)
    with open('result_opt_match.json', 'w') as fp:
            stri = json.dumps(result_opt_dict, ensure_ascii=False, encoding="utf-8", default = set_default)
            fp.write(stri)
    print("---------END DUMP-------------")
    

test_result_matching()



