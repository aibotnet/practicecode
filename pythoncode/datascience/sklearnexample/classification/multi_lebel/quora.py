import numpy as np
import matplotlib.pylab as pl

from sklearn.datasets import make_multilabel_classification
from sklearn.multiclass import OneVsRestClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import LabelBinarizer
from sklearn.decomposition import PCA
from sklearn.cross_decomposition import CCA


        
   
X, Y = make_multilabel_classification(n_classes=4, n_labels=6,
                                      allow_unlabeled=False,
                                      return_indicator=True,
                                      random_state=1)

#X = np.array( [ [1,0,4,6],[2,3,5,1],[1,3,0,0],[0,0,1,0]] )

#Y= np.array([[0,1,1],[2,1,1],[1,0,0],[0,1,0,0]])

print X
print Y

#X = PCA(n_components=2).fit_transform(X)
classif = OneVsRestClassifier(SVC(kernel='linear'))
classif.fit(X,Y)

X_test, Y_test = make_multilabel_classification(n_classes=3, n_labels=6,
                                      allow_unlabeled=False,
                                      return_indicator=True,
                                      random_state=1)



print classif.predict(X_test)[5],Y_test[5]

