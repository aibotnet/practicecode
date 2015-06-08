import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.svm import LinearSVC
from sklearn.svm import SVC
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.multiclass import OneVsRestClassifier
from sklearn.feature_extraction.text import CountVectorizer

f = open('train.in')

line = f.readline().split('\n')[0]
T=int(line.split(' ')[0].strip())
E=int(line.split(' ')[0].strip())
i=0
x_train = []
y_train = []
while i < T:
    lebels = f.readline().split('\n')[0][2:].strip()
    tokens = f.readline().split('\n')[0]
    x_train.append(tokens.strip())
    y_train.append(lebels)  
    i+=1

vect1 = CountVectorizer()
vect1.fit_transform(x_train)
t1 = vect1.transform(x_train)
X_train = t1.todense()


Y_train = np.zeros((T,250),dtype=np.int)
i=0
for el in y_train:
    for e in el.strip().split(' '):
        j=  int(e)
        Y_train[i][j]=1
    i+=1
print type(X_train[0][0])
print type(Y_train[0][0])

'''
classif = OneVsRestClassifier(LenearSVC(kernel='linear'))
classif.fit(x_train, x_train)

i=0
while i < E:
    tokens = f.readline().split('\n')[0].strip()

    predicted = classif.predict(vect1.transform(Y_train[0]).todense())
    i+=1
'''
