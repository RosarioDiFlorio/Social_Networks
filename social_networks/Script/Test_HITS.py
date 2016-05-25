from HITS import *
import timeit

graph = dict()
graph['x'] = {'y','z','w'}
graph['y'] = {'x','w'}
graph['z'] = {'k'}
graph['w'] = {'y','z'}
graph['k'] = {}


print("STARTING HITS")
start_time = timeit.default_timer()
time , a, h = HITS2(graph,1000,0.001)
elapsed= timeit.default_timer() - start_time
print("HITS2 elapsed: " + str(elapsed))
print("Time:" + str(time))
print ("A: " + str(a))
print ("H: "+ str(h))