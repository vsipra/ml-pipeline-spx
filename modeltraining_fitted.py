from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
import pandas as pd
from sklearn.preprocessing import OneHotEncoder
from sklearn.preprocessing import MinMaxScaler

# Import excel file using pandas
data = pd.read_excel("C:\\Users\\vajih\\OneDrive\\Documents\\Learning\\ml-model-spx\\SPX_train_0.xlsx")

# The dataset has 899 rows and 16 columns

X = data.drop(columns=["Returns","Time"], axis=1)   #Feature Matrix
Y = data["Returns"]          #Target Variable

scaler = MinMaxScaler()

fitted = scaler.fit_transform(X)


clf1 = RandomForestClassifier()
clf1.fit(X.values, Y)

clf2 = RandomForestClassifier()
clf2.fit(X.values, Y)

X1_train, X1_test, Y1_train, Y1_test = train_test_split(X, Y, test_size=0.2)

X2_train, X2_test, Y2_train, Y2_test = train_test_split(fitted, Y, test_size=0.2)

#X_train.shape, Y_train.shape
#X_test.shape, Y_test.shape

clf1.fit(X1_train, Y1_train)
clf2.fit(X2_train, Y2_train)


print(clf1.predict(X1_test))
print(clf2.predict(X2_test))

# print(Y_test)

print("clf1 score:", clf1.score(X1_test, Y1_test))
print("clf2 score:", clf2.score(X2_test, Y2_test))


clf1.predict([[2,3,4,1,2,3,4,1,2,3,4,1,1,1]])
clf2.predict([[2,3,4,1,2,3,4,1,2,3,4,1,1,1]])


### Create a Pickle file using serialization 
import pickle
pickle_out = open("C:\\Users\\vajih\\OneDrive\\Documents\\Learning\\ml-model-spx\\classifier.pkl","wb")
pickle.dump(clf1, pickle_out)
pickle_out.close()