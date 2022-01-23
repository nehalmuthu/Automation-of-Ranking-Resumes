import pandas as pd
import sklearn
import scipy
s=pd.read_csv('matrix.csv',encoding='utf-8')
v=s.values
#Call scipy.spatial.distance.cosine(u, v) to find the cosine distance between vectors u and v.
# Subtract the result from 1 to find cosine similarity.
cosine_similarity = 1-scipy.spatial.distance.cosine(v[0], v[2])
print(cosine_similarity)

