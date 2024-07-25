from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

from sklearn import datasets
import pandas as pd

from transformers import pipeline

"""
Split the data into training, testing, and validation sets. Takes in the data, test size, random state, and validation size as input.
"""
def cross_validation(X, y, test_size, random_state, val_size):
    #splitting the data into training and testing data (80% training, 20% testing)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=test_size, random_state=random_state)
    #splitting the training data into training and validation data (75% training, 25% validation (20% of the original data))
    X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size=val_size, random_state=random_state) 

    print(f"Training data size: {len(X_train)}")
    print(f"Testing data size: {len(X_test)}")
    print(f"Validation data size: {len(X_val)}")

    return X_train, X_test, X_val, y_train, y_test, y_val

"""
Generates model metrics based on the predicted and actual labels. Takes in the actual labels and predicted labels as input.
"""
def model_performance(label, prediction):
    accuracy = accuracy_score(label, prediction)
    precision = precision_score(label, prediction, average='micro')
    recall = recall_score(label, prediction, average='micro')
    f1 = f1_score(label, prediction, average='micro')
    return accuracy, precision, recall, f1

"""
Validates the model outputs against a set of predefined queries and expected responses.
Harcoded the predefined queries and expected responses for now.
Hardcoded the context for the model.
Hardcoded the model to be used for now - google/flan-t5-small
Prints the model's answers to a file for validation - necessary for human in the loop validation.
More work needed on this to properly validate the model outputs.
"""
def validate_model_outputs():

    # Load the question-answering pipeline
    pipe = pipeline("text2text-generation", model="google/flan-t5-small")

    context =   "You are a chatbot that provides technical support for customers of a tech company specialising in consumer electronics. \n" \
                "Questions can include troubleshooting common issues, providing step-by-step guides, and offering information on warranty and repair services. \n" \
                "Your goal is to assist customers in resolving their technical problems and improving their overall experience with the company's products."

    # Validate the model outputs against a set of predefined queries and expected responses
    # Create a list of questions
    questions = [
        "How can I reset my device to factory settings?",
        "What should I do if my device won't turn on?",
        "How do I update the firmware on my device?",
        "Why is my device not connecting to Wi-Fi?",
        "How can I improve the battery life of my device?"
    ]
    # Create a list of expected answers
    answers = [
        "To reset your device to factory settings, go to 'Settings' > 'System' > 'Reset' > 'Factory data reset'. Confirm the reset by following the on-screen instructions. Please note that this will erase all data on the device.",
        "If your device won't turn on, try the following steps: \n   - Ensure the device is charged by connecting it to the charger for at least 30 minutes. \n   - Press and hold the power button for 10-15 seconds to force a restart. \n   - If the device still does not turn on, try using a different charger or cable. \n   - If none of these steps work, please contact customer support for further assistance.",
        "To update the firmware on your device, follow these steps: \n   - Connect your device to a stable Wi-Fi network. \n   - Go to 'Settings' > 'About device' > 'Software update'. \n   - Check for updates and follow the on-screen instructions to download and install the latest firmware.",
        "If your device is not connecting to Wi-Fi, try these troubleshooting steps: \n   - Ensure that Wi-Fi is turned on in the device settings. \n   - Restart your device and router. \n   - Forget the Wi-Fi network and reconnect by entering the password again. \n   - Move closer to the router to ensure a strong signal. \n   - Check if other devices can connect to the Wi-Fi network. \n   - If the issue persists, contact your Internet Service Provider or customer support.",
        "To improve the battery life of your device, consider the following tips: \n   - Reduce screen brightness and timeout duration. \n   - Turn off Wi-Fi, Bluetooth, and GPS when not in use. \n   - Close background apps and disable auto-sync for non-essential apps. \n   - Use power-saving mode if available. \n   - Keep your device's software up to date. \n   - Avoid using live wallpapers and excessive widgets on the home screen."
    ]
    # Initialize an empty list to store the model's answers
    model_answers = []
    # Loop through the questions and generate answers using the model
    for question in questions:
        answer = pipe(context + question)
        model_answers.append(answer)  # Append the model's answer to the list

    #write generated answers to file - important for oversight & human in the loop validation
    with open('task2/output/model_answers.txt', 'w') as f:
        f.write(f"Model Answers for predefined queries:\n")
        for i in range(len(model_answers)):
            f.write(f"Question: {questions[i]}\n")
            f.write(f"Answer: {model_answers[i]}\n\n")
    
    return answers, model_answers

X, y = datasets.load_iris(return_X_y=True) #simple dataset for now...
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

#predict on the validation data
y_pred = model.predict(X_val)
#calculate metrics for validation data
accuracy, precision, recall, f1 = model_performance(y_val, y_pred)

#print metrics to file
with open('task2/output/model_metrics.txt', 'w') as f:
    f.write(f"Model Metrics for sklean dataset with {model}:\n")

    f.write("Model Performance (Test Set):\n")
    f.write(f"Accuracy: {accuracy}\n")
    f.write(f"Precision: {precision}\n")
    f.write(f"Recall: {recall}\n")
    f.write(f"F1 Score: {f1}\n\n")

    f.write("Model Performance (Validation Set):\n")
    f.write(f"Accuracy: {accuracy}\n")
    f.write(f"Precision: {precision}\n")
    f.write(f"Recall: {recall}\n")
    f.write(f"F1 Score: {f1}\n")

#call the validate_model_outputs function
validate_model_outputs()








