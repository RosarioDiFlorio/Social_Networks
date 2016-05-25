import re


namefile = "stopwords.txt"
namepy = "STOPWORD.py"


infile = open(namefile,"rb")
outfile = open(namepy,"w")
array = 'STOPWORD=["'
corpo = ""
for line in infile:
    corpo = corpo + line + '","'



corpo = re.sub("\n|\t","",corpo)
towrite = array+corpo+"]"
towrite = re.sub(',"]',']',towrite)
outfile.write(towrite)