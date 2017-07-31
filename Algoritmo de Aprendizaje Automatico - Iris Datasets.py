from sklearn import datasets
from sklearn import svm
iris = datasets.load_iris()
iris_data = iris.data
flower_iris = iris.target
clf = svm.LinearSVC()
clf.fit(iris_data, flower_iris)
result = clf.predict([[6.5,3.0,5.2,2.0]])