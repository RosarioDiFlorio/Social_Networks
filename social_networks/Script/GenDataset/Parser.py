#!/usr/bin/python

from re import findall, sub, compile

from CSS2 import CSS
from STOPWORD import STOPWORD
#Find all links in a web page
def read_links(html):
    #The function findall returns an array of all the occurrence of the searched element in the string given as second parameter
    #The searched element is given as a regular expression (this is indicated by the 'r' written in front of the first parameter)
    #The regular expression that we wrote returns the content of the href parameter of an html anchor
    return findall(r'<a .*?href=[\',\"](.*?)[\',\"].*?>',html)

def clean_text(text):
    #[a-zA-Z]*=\".*\"|[a-zA-Z]*\[.*\]|\"|
    #|.*:\/\/|:\/\/.*|.*#|#.*|
    
    regex = compile(".*:?url\(.*|.*[0-9]*\.?[0-9]*(em|px)|\{.*\}|.*=\".*|[a-zA-Z]*\[.*\]|.*--.*|:&.*|&.*|<.*|.*>|#([A-Fa-f0-9]{6}|[A-Fa-f0-9]{3})|\/\*.*|.*\*\/")
    regex2 = compile(".*;\/.*|.*{|\..*|.*=\'.*|\(-?.*-.*:.*\)|.*#|#.*|{.*|.*}")
    regex3 = compile("\||-|\\|\.|\:|\/|\"|\'|,|;|_|\*|@|\(|\)|\[|\]|{|}|!|\?|&|%|=|#|\+")
    regex4 = compile(".*href=.*|.*:(relative|none|link|visited|top|bottom|left|right)(;|:|\.)?")
    
    toret = []
    for x in text:
        if not regex.match(x) and not regex4.match(x) and not regex3.match(x) and  not regex2.match(x) and x not in STOPWORD:
            
            css = sub(':|;','',x)
            if css not in CSS:
                x = sub('\|\"|\'|,|:|;|_|\(|\)|\[|\]|{|}|!|\?|#','',x)
                x = sub(r'\.$|:$|-|\"|\'','',x)
                
                if x not in STOPWORD:
                    #print x
                    toret.append(x)
    return toret


#Find all the text in an html page that is not within tags
def read_content(html):
    #The function sub substitues any occurrence of the first parameter in the string given as third parameter with an occurrence of the second parameter
    #The first parameter here is given as a regular expression and consists of any html tag
    
    text = sub(r'<.*>',' ',html)
    #text = sub(r'<.*',' ',html)
    text = text.lower()
    text = text.split()
    #print text[:20]
    toret = clean_text(text)
    return toret

#This function removes from the given graph all the edges towards undefined pages
def sanitizer(graph):
    for i in graph.keys():
        neighbors=graph[i].copy()
        for j in neighbors:
            if j not in graph.keys():
                graph[i].remove(j)
    return graph

#This function reads a wibbi file and returns the resulting graph and the resulting database
#(to be processed by the ranking algorithm and the matching algorithm, respectively)
def read_wibbi(filename):
    infile = open(filename,"r")
    delim=infile.readline().strip() #It will contain the string that wibbi uses a separator
    nl = infile.readline().strip()
    if nl != "0": #The line after the separator will be either the url of the page or "0" if no more pages are present
        url = nl.split()[1]
        
    html=''
    copy=False
    graph=dict()
    db=dict()
    
    
    while True:
        line = infile.readline()
        if not line: 
            break
        if line.strip() == delim: #If we find the separator, we have copied the entire html
            copy=False
            
            #We parse the html with the above functions
            graph[url]=set(read_links(html))
            db[url]=read_content(html)
            
            
            #We start by reading the url of the next page, if any
            nl = infile.readline().strip()
            if nl != "0":
                url = nl.split()[1]
                
            html=''
            
        #We start to read only when we find the tag "<html"
        ls=line.split()
        if len(ls) > 0 and ls[0] == '<html':
            copy=True
            
        if copy is True:
            html+=line
            
    graph=sanitizer(graph)
    return graph, db
