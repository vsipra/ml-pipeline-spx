from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import pandas as pd
from sklearn.preprocessing import OneHotEncoder

# Import excel file using pandas
data = pd.read_excel("C:\\Users\\vajih\\OneDrive\\Documents\\Learning\\ml-model-spx\\SPX_train_0.xlsx")

# The dataset has 899 rows and 16 columns

X = data.drop(columns=["Returns","Time"], axis=1)   #Feature Matrix
Y = data["Returns"]          #Target Variable

clf = RandomForestClassifier()
   

clf.fit(X.values, Y)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2)

X_train.shape, Y_train.shape

X_test.shape, Y_test.shape

clf.fit(X_train.values, Y_train)

print(clf.predict(X_test.values))

print(Y_test)

print(clf.score(X_test.values, Y_test))

clf.predict([[2,3,4,1,2,3,4,1,2,3,4,1,1,1]])


### Create a Pickle file using serialization 
import pickle
pickle_out = open("C:\\Users\\vajih\\OneDrive\\Documents\\Learning\\ml-model-spx\\classifier.pkl","wb")
pickle.dump(clf, pickle_out)
pickle_out.close()