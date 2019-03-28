# car.data
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

# read the data in the balance-scale.data file as a csv
balance_data = pd.read_csv('DataSets/car.data', sep= ',', header= None)
# get the shape of the data
balance_data.shape
# get the X values from balance_data
X_bef = balance_data.values[:, 0:-1]
# normalize
X = []
leveldic = {"vhigh": 3, "high": 2, "med": 1, "low": 0}
lugdic = {"big": 2, "med": 1, "small": 0}
for i in X_bef:
	X.append([leveldic[i[0]], leveldic[i[1]], 5 if i[2]=='5more' else i[2], 5 if i[3]=='more' else i[3], lugdic[i[4]], leveldic[i[5]]])

# get the Y values from balance_data
Y = balance_data.values[:,-1]
# split the dataset into a training and testing sections
X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3)

# construct the decision tree classifier with a max depth of 3 and 
clf_entropy = DecisionTreeClassifier(criterion = "entropy", max_depth=2, min_samples_leaf=5)
# train the classifier
clf_entropy.fit(X_train, y_train)
# get the y prediction using the test data
y_pred_en = clf_entropy.predict(X_test)
# print the result
print ("Accuracy is ", accuracy_score(y_test,y_pred_en)*100)
