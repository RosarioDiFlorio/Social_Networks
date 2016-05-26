from load_dataset import *
from collections import OrderedDict 
import operator
import os

def set_default(obj):
	if isinstance(obj,set):
		return list(obj)
	raise TypeError
    
def invert_db(flag):
    
    

    
    if flag:
        new_db = dict()
        db_old = db()
        
        
        i = 0
        for link in db_old.keys():
            pages_words = len(db_old[link])
            
            for word in db_old[link]:

                if word not in new_db:
                    new_db[word]=dict()

                count = db_old[link].count(word)
                new_db[word][link] = float(count)/pages_words
            #print new_db
            if i % 1000 == 0:
                print i
            i += 1
        
        print("------START DUMPING-----")
        with open('reverse_db.json', 'w') as fp:
            stri = json.dumps(new_db, ensure_ascii=False, encoding="utf-8", default = set_default)
            fp.write(stri)
        print("------DONE-----")
        return new_db
    
    else:
        dataset = reverse_db()
        return dataset
    

#data = invert_db(False)

#for w in data.keys():
#    print w



    

    
        
        
        
def ordered_invert_db():
        old_db = reverse_db()
        tmp = sorted(old_db,key = lambda x:old_db[x], reverse = True)
        sorted_db = OrderedDict((x,old_db[x]) for x in tmp)
        print("------START DUMPING-----")
        with open('ordered_reverse_db.json', 'w') as fp:
            stri = json.dumps(sorted_db, ensure_ascii=False, encoding="utf-8", default = set_default)
            fp.write(stri)
        print("------DONE-----")  
        return sorted_db
            
            
            
            
    
ordered_invert_db()
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        

            