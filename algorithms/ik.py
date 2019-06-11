#!/usr/bin/python3

from  sklearn.datasets  import  load_iris
from  sklearn.model_selection    import train_test_split
from  sklearn  import tree
from sklearn.neighbors import KNeighborsClassifier
from   sklearn.metrics  import  accuracy_score 
import  matplotlib.pyplot  as plt
import  mpld3
# loading  dataset
iris=load_iris()
#print (dir(iris))

# checking number of rows in  IRIS feature data  
#print  (iris.data.shape)
# checking complete data 
#print  iris.data

#  label data
#print  iris.target
#  spliting  train and test data in  10%
train_data,test_data,train_target,test_target=train_test_split(iris.data,iris.target,test_size=0.1)

#  calling  decision tree classifier 
clf=tree.DecisionTreeClassifier()
# now training data
trained=clf.fit(train_data,train_target)

#  now predicting  test_data  output with Decision Tree
output=trained.predict(test_data)
print  (output)

#  calling  KNN
knn=KNeighborsClassifier(n_neighbors=3)
# now training data 
knn_trained=knn.fit(train_data,train_target)
#  predicting with KNN
outputknn=knn_trained.predict(test_data)


#  calling  KNN with diff
knng=KNeighborsClassifier(n_neighbors=7)
# now training data
knn_trained=knng.fit(train_data,train_target)
#  predicting with KNN
outputknng=knn_trained.predict(test_data)

#  calculating  accuracy score  for Decision
pctdsc=accuracy_score(test_target,output)
print  (type(pctdsc))
x1=["showing pct for DC"]

#  calculating  accuracy score for KNN
pctknn=accuracy_score(test_target,outputknn)
print  (type(pctknn))
x2=["showing pct for KNN"]

#  calculating  accuracy score for KNN
pctknng=accuracy_score(test_target,outputknng)
print  (type(pctknng))
x3=["showing pct for KNN next generation"]


plt.xlabel("percet")
plt.ylabel("bargraph")
plt.bar(x1,pctdsc,label="DecisionTree")
plt.bar(x2,pctknn,label="KNN")
plt.bar(x3,pctknng,label="KNNNg")
plt.legend()
mpld3.show()


