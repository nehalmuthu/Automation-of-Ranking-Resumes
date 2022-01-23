from projectApp.code.convertPDFtoText import convert_pdf_to_txt

from rank_bm25 import BM25Okapi

#https://pypi.org/project/rank-bm25/
#there is a paper her 
#incluse that too


import re
import pandas as pd
import numpy as np

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))


def existing_docs():
    train=pd.read_csv('projectApp/code/main.csv')
    ## Iterate over the data to preprocess by removing stopwords

    lines_without_stopwords=[] 
    for line in train['content'].values: 
        line = line.lower()
        #remove short words
        shortword = re.compile(r'\W*\b\w{1,3}\b')
        line = shortword.sub('', line)
        
        line_by_words = re.findall(r'(?:\w+)', line, flags = re.UNICODE) # remove punctuation ans split
    
        new_line=[]
        for word in line_by_words:
            if word not in stop:
                new_line.append(word)
        lines_without_stopwords.append(new_line)
    texts = lines_without_stopwords
    tokenized_corpus = texts

    bm25 = BM25Okapi(tokenized_corpus)
    return bm25


def queryDocs(docName):
    
    #docName="E:/irpackage/django_Practice/projectName/documentsJD/"+docName
    bm25=existing_docs()
    query=convert_pdf_to_txt(docName)
    line = query.lower()
    #remove short words
    shortword = re.compile(r'\W*\b\w{1,3}\b')
    line = shortword.sub('', line)
    line_by_words = re.findall(r'(?:\w+)', line, flags = re.UNICODE) # remove punctuation ans split
    
    new_line=[]
    for word in line_by_words:
        if word not in stop:
            new_line.append(word)
    query=new_line    

    doc_scores = bm25.get_scores(query)
    # array([0.        , 0.93729472, 0.        ])

    train=pd.read_csv('projectApp/code/main.csv')
    l=bm25.get_top_n(query, train['files'].values, n=5)
    for i in range(len(l)):
        s=l[i].split("\\")
        l[i]=s[len(s)-1]
        
    return l



def queryDocs2(docName):
    
    #docName="E:/irpackage/django_Practice/projectName/documentsJD/"+docName
    docName="E:/irpackage/django_Practice/projectName/tempUploadfiles/"+docName
    bm25=existing_docs()
    d=docName.split('.')
    if d[len(d)-1]=='pdf':
        query=convert_pdf_to_txt(docName)
    else:
        f=open(docName,'r')
        query=f.read()
        
    line = query.lower()
    #remove short words
    shortword = re.compile(r'\W*\b\w{1,3}\b')
    line = shortword.sub('', line)
    line_by_words = re.findall(r'(?:\w+)', line, flags = re.UNICODE) # remove punctuation ans split
    
    new_line=[]
    for word in line_by_words:
        if word not in stop:
            new_line.append(word)
    query=new_line    

    doc_scores = bm25.get_scores(query)
    # array([0.        , 0.93729472, 0.        ])

    train=pd.read_csv('projectApp/code/main.csv')
    l=bm25.get_top_n(query, train['files'].values, n=10)
    for i in range(len(l)):
        s=l[i].split("\\")
        l[i]=s[len(s)-1]
        
    return l

    
    