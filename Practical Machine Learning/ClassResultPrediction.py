from sklearn import tree

# [roll,result,improve]
X = [[2,3.33,3],[3,2.68,7],[6,2.95,8],[7,3.68,0],[8,2.61,8],[11,2.98,6],[16,2.77,8],
	[18,3.00,6],[19,3.50,1],[21,3.18,3],[22,2.79,4]]

Y = ['male','female','male','female','male','male',
	'male','male','female','male','male']

clf = tree.DecisionTreeClassifier()

clf = clf.fit(X,Y)
prediction = clf.predict([[44,3.21,3]])

print(prediction)
