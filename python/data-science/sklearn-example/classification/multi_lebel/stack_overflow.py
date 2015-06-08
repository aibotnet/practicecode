import numpy as np
from sklearn import *
from sklearn.multiclass import OneVsRestClassifier
from sklearn.neighbors import KNeighborsClassifier
import time

def test_classifier(clf, X, Y, description, jobs=1):
    print '=== Testing classifier {0} ==='.format(description)
    for class_idx in xrange(Y.shape[1]):
        print ' > Cross-validating for class {:d}'.format(class_idx)
        n_samples = X.shape[0]
        cv = cross_validation.StratifiedKFold(Y[:,class_idx], 3)
        t_start = time.clock()
        scores = cross_validation.cross_val_score(clf, X, Y[:,class_idx], cv=cv, score_func=metrics.precision_recall_fscore_support, n_jobs=jobs)
        t_end = time.clock();
        print 'Cross validation time: {:0.3f}s.'.format(t_end-t_start)
        str_tbl_fmt = '{:>15s}{:>15s}{:>15s}{:>15s}{:>15s}'
        str_tbl_entry_fmt = '{:0.2f} +/- {:0.2f}'
        print str_tbl_fmt.format('', 'Precision', 'Recall', 'F1 score', 'Support')
        for (score_class, lbl) in [(0, 'Negative'), (1, 'Positive')]:
            mean_precision = scores[:,0,score_class].mean()
            std_precision = scores[:,0,score_class].std()
            mean_recall = scores[:,1,score_class].mean()
            std_recall = scores[:,1,score_class].std()
            mean_f1_score = scores[:,2,score_class].mean()
            std_f1_score = scores[:,2,score_class].std()
            support = scores[:,3,score_class].mean()
            print str_tbl_fmt.format(
                lbl,
                str_tbl_entry_fmt.format(mean_precision, std_precision),
                str_tbl_entry_fmt.format(mean_recall, std_recall),
                str_tbl_entry_fmt.format(mean_f1_score, std_f1_score),
                '{:0.2f}'.format(support))

def test_classifier_multilabel(clf, X, Y, description, jobs=1):
    print '=== Testing multi-label classifier {0} ==='.format(description)
    n_samples = X.shape[0]
    Y_list = [value for value in Y.T]
    print 'Y_list[0].shape:', Y_list[0].shape, 'len(Y_list):', len(Y_list)
    cv = cross_validation.StratifiedKFold(Y_list, 3)
    clf_ml = OneVsRestClassifier(clf)
    accuracy = (clf_ml.fit(X, Y).predict(X) != Y).sum()
    print 'Accuracy: {:0.2f}'.format(accuracy)
    scores = cross_validation.cross_val_score(clf_ml, X, Y_list, cv=cv, score_func=metrics.precision_recall_fscore_support, n_jobs=jobs)
    str_tbl_fmt = '{:>15s}{:>15s}{:>15s}{:>15s}{:>15s}'
    str_tbl_entry_fmt = '{:0.2f} +/- {:0.2f}'
    print str_tbl_fmt.format('', 'Precision', 'Recall', 'F1 score', 'Support')
    for (score_class, lbl) in [(0, 'Negative'), (1, 'Positive')]:
        mean_precision = scores[:,0,score_class].mean()
        std_precision = scores[:,0,score_class].std()
        mean_recall = scores[:,1,score_class].mean()
        std_recall = scores[:,1,score_class].std()
        mean_f1_score = scores[:,2,score_class].mean()
        std_f1_score = scores[:,2,score_class].std()
        support = scores[:,3,score_class].mean()
        print str_tbl_fmt.format(
            lbl,
            str_tbl_entry_fmt.format(mean_precision, std_precision),
            str_tbl_entry_fmt.format(mean_recall, std_recall),
            str_tbl_entry_fmt.format(mean_f1_score, std_f1_score),
            '{:0.2f}'.format(support))

def main():
    nfeatures = 13
    nclasses = 5
    ncolumns = nfeatures + nclasses
    data = np.loadtxt('', delimiter=',', usecols=range(ncolumns))

    print data, data.shape
    X = np.hstack((data[:,0:3], data[:,(nfeatures-1):nfeatures]))
    print 'X.shape:', X.shape
    Y = data[:,nfeatures:ncolumns]
    print 'Y.shape:', Y.shape

    test_classifier(svm.LinearSVC(), X, Y, 'Linear Support Vector Machine', jobs=-1)
    test_classifier_multilabel(svm.LinearSVC(), X, Y, 'Linear Support Vector Machine')

if  __name__ =='__main__':
    main()
