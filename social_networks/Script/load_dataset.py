import json
import ast
from StringIO import StringIO
from collections import OrderedDict

def load():
    with open('GenDataset/dataset.json') as file:
        stri = file.read()
        data = json.loads(stri, encoding='utf-8')
    return data

def load_reverse_db():
    with open('GenDataset/reverse_db.json') as file:
        stri = file.read()
        data = json.loads(stri,encoding='utf-8')
    return data
    
    
    
def graph():
    all_graph = dict()
    data = load()
    
    print("LOAD FILE COMPLETE")
    print(type(data))
    print(str(data)[:50])
    for name in data.keys():
        print("READING "+name)
        graph = data[name]["graph"]
        all_graph.update(graph)

    return all_graph

def get_fullgraph():
	with open('full_graph.json') as file:
			stri = file.read()
			fullgraph = json.loads(stri, encoding='utf-8')
	return fullgraph

def nodi_entranti(graph,name):
	toret = []
	for g in graph.keys():
		if not type(graph[g]) == float:
			if name in graph[g]:
				toret.append(g)

	return toret
    
def calcola_fullgraph(graph):
	incoming = []
	full_graph = dict()
	i=0
	for g in graph.keys():
		if not i%1000:
			print (i)
		incoming = nodi_entranti(graph,g)
		full_graph[g] = {"incoming": incoming, "outgoing": graph[g]}
		i += 1

	return full_graph
    
    
def dump_full_graph():
	graph_mid = graph()
	print("------CALCULATING FULLGRAPH------")
	full_graph = calcola_fullgraph(graph_mid)
	print("------FINISHED FULLGRAPH-----")
	print("------START DUMPING-----")
	with open('full_graph.json', 'w') as fp:
					stri = json.dumps(full_graph, ensure_ascii=False)
					fp.write(stri)
	print("------DONE-----")




def db():
   
   all_db = dict()
   data = load()
   for name in data:
       
       db = data[name]["db"]
       all_db.update(db)

   return all_db


def reverse_db():
    all_reverse_db = dict()
    data = load_reverse_db()
    for name in data:
        
        db = data[name]
        all_reverse_db[name] = db
        
    
    return all_reverse_db

def ordered_reverse_db():
    all_reverse_db = dict()
    data = load_ordered_reverse_db()
    for name in data:
        
        db = data[name]
        all_reverse_db[name] = db
        
    
    return all_reverse_db


def load_ordered_reverse_db():
    with open('GenDataset/ordered_reverse_db.json') as file:
        stri = file.read()
        data = json.loads(stri,encoding='utf-8',object_pairs_hook=OrderedDict)
    return data
