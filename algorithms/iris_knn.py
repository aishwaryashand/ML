#!/usr/bin/python3

import sklearn
from sklearn.datasets  import load_iris
from sklearn import  tree
from sklearn.model_selection  import train_test_split
from sklearn.metrics  import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import mpld3

#  loading  iris data
iris=load_iris()

#  NOW SPLITING  
train_iris,test_iris,train_target,test_target=train_test_split(iris.data,iris.target,test_size=0.1)

#  train_iris  and  train_target data will be using under fit method

#  calling  DecisionTree  classifier
DCclf=tree.DecisionTreeClassifier()

#calling KNN algo
KNNclf=KNeighborsClassifier(n_neighbors=5)


# now training  data DC
trainedDC=DCclf.fit(train_iris,train_target)

# now training data KNN
trainedKNN=KNNclf.fit(train_iris,train_target)

#  test with test_iris DC
outputDC=trainedDC.predict(test_iris)
print("test_iris data by DC is:  ",outputDC)

# test with KNN
outputKNN=trainedKNN.predict(test_iris)
print("test_iris data by KNN is: ",outputKNN)

# actual output 
print("actual data must be:      ",test_target)

# calculating  accuracy score DC
pctDC=accuracy_score(test_target,outputDC)
print("% of accuracy by DC is:  ",pctDC)

# calculating  accuracy score KNN
pctKNN=accuracy_score(test_target,outputKNN)
print("% of accuracy by KNN is: ",pctKNN)

#  exporting  graph  for decisionTree
tree.export_graphviz(DCclf, out_file="tree.dot", max_depth=7, feature_names=iris.feature_names, class_names=iris.target_names, filled=True,rounded=True)

x1=['showing pct of DC']
x2=['showing pct of KNN']

plt.xlabel("bargraph")
plt.ylabel("accuracy")
plt.bar(x1,pctDC,width=0.5)
plt.bar(x2,pctKNN,width=0.5)
#plt.grid(color='y')
mpld3.show()

