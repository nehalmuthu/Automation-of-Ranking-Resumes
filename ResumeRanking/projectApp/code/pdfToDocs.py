from convertPDFtoText import convert_pdf_to_txt
from nltk.corpus import stopwords 
import os
stop_words = set(stopwords.words('english')) 

#give pdf filepath as input fn returns bag of words
def docTobagofwords(pdfPath):
    l=convert_pdf_to_txt(pdfPath)
    #split into lines
    l=l.split("\n")
    #split line into words and create list of words
    s=[]
    for i in l:
        s.extend(i.split())

    #remove stop words ,lower case , remove word of len<2 
    bag=[]    
    for i in range(len(s)):
        s[i]=s[i].lower()
        s[i]=s[i].replace(' ','')
        s[i]=s[i].replace(")","")
        s[i]=s[i].replace("(",'')
        s[i]=s[i].replace(' ','')
        s[i]=s[i].replace("\x0c",'')
        if len(s[i])>3:
            bag.append(s[i])
    
    return bag



#give folder with pdf docs
#function return 2 lists 
#list of file names(.pdf) and  list of bag of words coreesponnding to each file  
def bulkConvert(path):
    #get all pdf fil names in data folder        
    f=os.listdir(path)
    files=[]
    for i in f:
        if i.endswith(".pdf"):
            files.append(path+'/'+i)

    #get bag of words of each file
    b=[]
    for i in range(len(files)):
        b.append(docTobagofwords(files[i]))
    
    #files -> list of file names    and  b - list of bag of words
    return files,b
    




if __name__ == "__main__":
    path='../data/subset/'
    f,b=bulkConvert(path)
    
