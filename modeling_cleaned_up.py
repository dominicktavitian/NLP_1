
# coding: utf-8

# In[1]:

import numpy as np
import pandas as pd
import random
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegressionCV
from sklearn.metrics import f1_score, accuracy_score, recall_score, precision_score

model_bow = LogisticRegressionCV(penalty='l2', scoring='f1', solver='liblinear')
model_bobg = LogisticRegressionCV(penalty='l2', scoring='f1', solver='liblinear')
model_tfidf = LogisticRegressionCV(penalty='l2', scoring='f1', solver='liblinear')
model_tfidf_bobg = LogisticRegressionCV(penalty='l2', scoring='f1', solver='liblinear')


# In[2]:

# Core methods
def unison_shuffled_copies(a, b):
    assert len(a) == len(b)
    p = np.random.permutation(len(a))
    return a[p], b[p]

def train_and_test(model, data, size=300):
    X, y = data
    sample_1 = np.random.choice((np.where(y == 1)[0]).squeeze(), size, replace=False)
    sample_0 = np.random.choice((np.where(y == 0)[0]).squeeze(), size, replace=False)
    X_1_sample, y_1_sample = X[sample_1], y[sample_1]
    X_0_sample, y_0_sample = X[sample_0], y[sample_0]
    X_test_bal, y_test_bal = np.vstack((X_1_sample[0:size/2], X_0_sample[0:size/2])), np.vstack((y_1_sample[0:size/2], y_0_sample[0:size/2]))
    X_train_bal, y_train_bal = np.vstack((X_1_sample[size/2:], X_0_sample[size/2:])), np.vstack((y_1_sample[size/2:], y_0_sample[size/2:]))
    
    X_train_bal, y_train_bal = unison_shuffled_copies(X_train_bal, y_train_bal)
    model.fit(X_train_bal, y_train_bal)
    print "Accuracy: {}\nF-score: {}".format(model.score(X_test_bal, y_test_bal), 
                                             f1_score(model.predict(X_test_bal), y_test_bal))
    


# In[3]:

y = pd.read_csv('y_train.csv', index_col=0).values
features = pd.read_csv('bow_train.csv', index_col=0)

X = features.values
data = (X, y)
train_and_test(model_bow, data)


# In[4]:

features = pd.read_csv('tfidf_train.csv', index_col=0)

X = features.values
data = (X, y)
train_and_test(model_tfidf, data)


# In[5]:

features = pd.read_csv('bobg_train.csv', index_col=0)

X = features.values
data = (X, y)
train_and_test(model_bobg, data)


# In[6]:

features = pd.read_csv('tfidf_bobg_train.csv', index_col=0)

X = features.values
data = (X, y)
train_and_test(model_tfidf_bobg, data)


# In[ ]:



