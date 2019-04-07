from sklearn import tree

# [roll,result,improve]
features = [[140,1], [130,1], [150,0], [170, 0]]
labels = [1,1,0,0]

clf = tree.DecisionTreeClassifier()

clf = clf.fit(features,labels)
prediction = clf.predict([[300,1]])

if prediction == 1:
    print("Orange")

else:
    print("Apple")
