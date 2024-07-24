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





