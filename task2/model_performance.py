from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from sklearn import datasets

X, y = datasets.load_iris(return_X_y=True) #placeholder data for now...
print(X.shape, y.shape)

#splitting data into train, test & validation sets - validation only to be used as a final check of the models performance
#splitting the data into training and testing data (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)
#splitting the training data into training and validation data (75% training, 25% validation (20% of the original data))
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=0.25, random_state=1) 

print(f"Training data size: {len(X_train)}")
print(f"Testing data size: {len(X_test)}")

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

def model_performance(y_test, y_pred):
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='micro')
    recall = recall_score(y_test, y_pred, average='micro')
    f1 = f1_score(y_test, y_pred, average='micro')
    return accuracy, precision, recall, f1

model_performance(y_test, y_pred)





