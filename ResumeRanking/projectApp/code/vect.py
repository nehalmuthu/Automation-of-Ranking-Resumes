
from convertPDFtoText import convert_pdf_to_txt
import os
import pandas as pd
path="E:\irpackage\django_Practice\projectName\documentsJD"
f=os.listdir(path)
files=[]
for i in f:
    if i.endswith(".pdf"):
        files.append(path+'/'+i)

#get bag of words of each file
b=[]
for i in range(len(files)):
        b.append(convert_pdf_to_txt(files[i]))
    
#files -> list of file names    and  b - list of bag of words

df=pd.DataFrame(zip(files,b),columns=["files","content"])
df.to_csv("main.csv",encoding="utf-8",index=False)


    