from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from sklearn import datasets

#splitting data into train, test & validation sets - validation only to be used as a final check of the models performance
def cross_validation(X, y, test_size, random_state, val_size):
    #splitting the data into training and testing data (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    #splitting the training data into training and validation data (75% training, 25% validation (20% of the original data))
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=val_size, random_state=random_state) 

    print(f"Training data size: {len(X_train)}")
    print(f"Testing data size: {len(X_test)}")
    print(f"Validation data size: {len(X_val)}")

    return X_train, X_test, X_val, y_train, y_test, y_val

#generating model metrics
def model_performance(label, prediction):
    accuracy = accuracy_score(label, prediction)
    precision = precision_score(label, prediction, average='micro')
    recall = recall_score(label, prediction, average='micro')
    f1 = f1_score(label, prediction, average='micro')
    return accuracy, precision, recall, f1

X, y = datasets.load_iris(return_X_y=True) #placeholder data for now...
print(X.shape, y.shape)

#generate the train, test & validation datasets
X_train, X_test, X_val, y_train, y_test, y_val = cross_validation(X, y, 0.2, 42, 0.25)

#select the model & fit the training data to it
model = GaussianNB()
model.fit(X_train, y_train)

#predict on the test data
y_pred = model.predict(X_test)
#calculate metrics for test data
accuracy, precision, recall, f1 = model_performance(y_test, y_pred)

print("Model Performance (Test Set):")
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")  
print(f"F1 Score: {f1}")

#predict on the validation data
y_pred = model.predict(X_val)
#calculate metrics for validation data
accuracy, precision, recall, f1 = model_performance(y_val, y_pred)

print("Model Performance (Validation Set):")
print(f"Accuracy: {accuracy}")
print(f"Precision: {precision}")
print(f"Recall: {recall}")  
print(f"F1 Score: {f1}")

questions = [
    "1. How can I reset my device to factory settings?",
    "2. What should I do if my device won't turn on?",
    "3. How do I update the firmware on my device?",
    "4. Why is my device not connecting to Wi-Fi?",
    "5. How can I improve the battery life of my device?"
]

answers = [
    "1. To reset your device to factory settings, go to 'Settings' > 'System' > 'Reset' > 'Factory data reset'. Confirm the reset by following the on-screen instructions. Please note that this will erase all data on the device.",
    "2. If your device won't turn on, try the following steps: \n   - Ensure the device is charged by connecting it to the charger for at least 30 minutes. \n   - Press and hold the power button for 10-15 seconds to force a restart. \n   - If the device still does not turn on, try using a different charger or cable. \n   - If none of these steps work, please contact customer support for further assistance.",
    "3. To update the firmware on your device, follow these steps: \n   - Connect your device to a stable Wi-Fi network. \n   - Go to 'Settings' > 'About device' > 'Software update'. \n   - Check for updates and follow the on-screen instructions to download and install the latest firmware.",
    "4. If your device is not connecting to Wi-Fi, try these troubleshooting steps: \n   - Ensure that Wi-Fi is turned on in the device settings. \n   - Restart your device and router. \n   - Forget the Wi-Fi network and reconnect by entering the password again. \n   - Move closer to the router to ensure a strong signal. \n   - Check if other devices can connect to the Wi-Fi network. \n   - If the issue persists, contact your Internet Service Provider or customer support.",
    "5. To improve the battery life of your device, consider the following tips: \n   - Reduce screen brightness and timeout duration. \n   - Turn off Wi-Fi, Bluetooth, and GPS when not in use. \n   - Close background apps and disable auto-sync for non-essential apps. \n   - Use power-saving mode if available. \n   - Keep your device's software up to date. \n   - Avoid using live wallpapers and excessive widgets on the home screen."
]





