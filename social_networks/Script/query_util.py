#!/usr/bin/python 
import random
from load_dataset import *

#generate a file with all words in reverse_db.json
def generateQueryFromReverseDB():
    db = load_reverse_db()
    words = []
    numQuery = 1000;
    with open('query.txt','w') as fp:
        
        for el in db:
            words.append(el);
        
            
    
        for i in range(numQuery):
            numWord = random.randint(2,6);
            query = random.sample(words,numWord)
            queryStr = ' '.join(query)
            if i > 0:
                fp.write("\n")
            fp.write(queryStr)
    
    
    print("-------DONE----------")    
        
        
 
 
        
generateQueryFromReverseDB()