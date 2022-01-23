from pdfToDocs import bulkConvert
from collections import Counter
import numpy as np
import pandas as pd
#create index,posting list from filenames and bag of words
# d is dictionatonary : key is words value is the docs in which it is present
def index(files,bag):
    d=dict()
    for i in range(len(files)):
        for w in bag[i]:
            if w in d:
                d[w].add(files[i])
            else:
                d[w]=set()
                d[w].add(files[i])
    return d    
                     
path='E:\irpackage\data\subset'
#files -> names of all docs
#bag -> contains bag of words corresponding to each doc
files,bag=bulkConvert(path)  
#d is the indexed dictionary,posting list
d=index(files,bag)


words=list(d.keys())
words.sort()
#files*words matrix
mat=[[0 for i in range(len(d))] for j in range(len(files))]
#weights are tfidf values
for i in range(len(files)):
    tfd=Counter(bag[i])
    #for normalizing tf term
    mxtf=tfd.most_common(1)[0][1]
    for j in range(len(words)):
        if words[j] in bag[i]:
            #normalize tf 
            tf=tfd[words[j]]/mxtf
            #idf -> (tot docs )/(docss in which word is present)
            idf=np.log10(len(files))/len(d[words[j]])
            mat[i][j]=tf*idf
            
            
            
df=pd.DataFrame(mat)
df.to_csv('matrix.csv',encoding='utf-8')
