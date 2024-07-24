import pandas as pd
import numpy as np
from sklearn import datasets

import pandas as pd

df = pd.read_csv("hf://datasets/NebulaByte/E-Commerce_FAQs/FAQs.csv")
print(df.columns)

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

def drop_columns(data, columns):
    data.drop(columns, axis=1, inplace=True)
    return data

def clean_null_values(data):
    valuesrows_with_nan = data[data.isnull().any(axis=1)]
    print(valuesrows_with_nan)
    nullvaluescleaned_df = data.dropna(inplace=True)
    return nullvaluescleaned_df

def clean_duplicate_values(data):
    duplicate_rows = data[data.duplicated()]
    print(duplicate_rows)
    duplicatescleaned_df = data.drop_duplicates()
    return duplicatescleaned_df

def to_lower_case(data):
    lowercase_df = data.apply(lambda x: x.astype(str).str.lower())
    return lowercase_df

df2 = drop_columns(df, ['parent_category', 'category_id', 'question_id', 'faq_url', 'que_ans'])
print(df2.columns)

print(df2.describe())


