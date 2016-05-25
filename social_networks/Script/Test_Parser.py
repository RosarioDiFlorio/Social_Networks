#!/usr/bin/python

from Parser import read_wibbi
import json

siti = ["ARTS","BUSINESS","COMPUTERS","GAMES","HEALTH","HOME","KIDSANDTEENS","NEWS","RECREATION","REFERENCE","REGIONAL",
"SCIENCE","SHOPPING","SOCIETY","SPORTS"]

dataset = dict()
for name in siti:
	graph,db = read_wibbi(name+".pages")
	dataset[name] = {"graph":graph,"db":db}

with open('dataset.json', 'w') as fp:
    json.dump(dataset, fp)