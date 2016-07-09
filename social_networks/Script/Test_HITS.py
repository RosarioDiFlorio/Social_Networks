from HITS import *
import json
import timeit
from load_dataset import *

if __name__  == "__main__":
    
    rep = 1
    elapsed_load = 0
    elapsed_dump = 0
    elapsed = 0
    print("---------STARTING ---------")
    for i in range(rep):
        start_time_load = timeit.default_timer()
        graph = get_fullgraph()
        elapsed_load += timeit.default_timer() - start_time_load 

        #print("STARTING HITS")
        start_time = timeit.default_timer()
        time , a, h = HITS2(graph,1000)
        elapsed += timeit.default_timer() - start_time
        print("HITS2 elapsed: " + str(elapsed))
        #print("Time:" + str(time))


        result = dict()

        for k in graph:
            result[k] = {"a": a[k], "h": h[k]}

        start_time_dump = timeit.default_timer()
        #print("---------DUMPING RESULT---------")
        with open('result_HITS.json','w') as fp:
            json.dump(result,fp)
        #print("---------FINISHED DUMPING---------")
        elapsed_dump += timeit.default_timer() - start_time_dump

    print("---------FINISHED---------")
    print("Load:\t"+str(float(elapsed_load)/rep))
    print("Algorithm:\t"+str(float(elapsed)/rep))
    print("Dump:\t"+str(float(elapsed_dump)/rep))