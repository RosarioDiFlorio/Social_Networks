from load_dataset import db
from load_dataset import graph

graph = graph()
db = db()
nodes = graph.keys()
#n = len(nodes)
count = 0
rdb = dict()

for i in nodes:
    print i
    words = db.get(i)
    print words
         
            
    
    