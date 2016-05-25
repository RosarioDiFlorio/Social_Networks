#!/usr/bin/python

from re import sub
from Parser import read_wibbi
import json
import random
import os

def set_default(obj):
	if isinstance(obj,set):
		return list(obj)
	raise TypeError

def create_link(dataset):
    for name1 in dataset:
        for name2 in dataset:
           if name1!=name2:

               U = random.sample(dataset[name1]["graph"].keys(),10)
               V = random.sample(dataset[name2]["graph"].keys(),10)

               for i in range(len(U)):
                   if V[i] not in dataset[name1]["graph"][U[i]]: 
                       dataset[name1]["graph"][U[i]].add(V[i])
 




pathdataset = os.getcwd()+'/dataset/'
pathdataset = sub("/Script/GenDataset","",pathdataset)
#pathdataset = os.getcwd()
print pathdataset


dataset = dict()
for name in os.listdir(os.path.dirname(pathdataset)):
   if name.endswith(".pages"): 
       
	print("Parsing: " + name)
	graph,db = read_wibbi(pathdataset+"/"+name)
	dataset[name] = {"graph":graph,"db":db}
	print("----------------")

print("------FINISHED PARSING-----")


print("------CREATING FAKE LINK -----")
create_link(dataset)
print("------FINISHED CREATING-------")

print("------START DUMPING-----")
with open('dataset_new.json', 'w') as fp:
        stri = json.dumps(dataset, ensure_ascii=False, encoding="utf-8", default = set_default)
        fp.write(stri)
print("------DONE-----")




