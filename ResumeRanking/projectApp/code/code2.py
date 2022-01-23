#https://www.kaggle.com/stacykurnikova/using-glove-embedding
import re
import pandas as pd
import numpy as np

from nltk.corpus import stopwords
stop = set(stopwords.words('english'))

train=pd.read_csv('main.csv')
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

print(texts[0:5])

#https://www.kaggle.com/shahules/basic-eda-cleaning-and-glove
embedding_dict={}
with open('D:/sem_7_part3/glove.6B.100d.txt','r',encoding='utf-8') as f:
    for line in f:
        values=line.split()
        word=values[0]
        vectors=np.asarray(values[1:],'float32')
        embedding_dict[word]=vectors
f.close()


MAX_LEN=50
tokenizer_obj=Tokenizer()
tokenizer_obj.fit_on_texts(corpus)
sequences=tokenizer_obj.texts_to_sequences(corpus)

tweet_pad=pad_sequences(sequences,maxlen=MAX_LEN,truncating='post',padding='post')
