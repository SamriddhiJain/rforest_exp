from sklearn import ensemble


def classify(class1, label, features_test, labels_test):   
    ### import the sklearn module for GaussianNB
    ### create classifier
    ### fit the classifier on the training features and labels
    ### return the fit classifier
    
	
	clf = ensemble.RandomForestClassifier(n_estimators=20)
	clf = clf.fit(class1,label)
	pred=clf.predict(features_test)

	cnt = [[0 for x in range(3)] for x in range(3)] 

	f = open('rforest.txt', 'w')

	for i in range(len(features_test)):
		var=[int(x) for x in clf.predict(features_test[i])][0]
		print>>f,features_test[i],var

		cnt[labels_test[i]][var]+=1

	print cnt;
	print "Accuracy calculated: ",float(cnt[0][0]+cnt[1][1]+cnt[2][2])/len(features_test)

	from sklearn.metrics import accuracy_score
	print "Accuracy from function: ",accuracy_score(pred,labels_test)
	return clf
    ### your code goes here!