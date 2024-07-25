import pandas as pd
import numpy as np
from sklearn import datasets

import pandas as pd

#Read data from HuggingFace into Pandas DataFrame
df = pd.read_csv("hf://datasets/NebulaByte/E-Commerce_FAQs/FAQs.csv")

#Function to drop columns from the dataset
def drop_columns(data, columns):
    data.drop(columns, axis=1, inplace=True)
    return data

#Function to clean null values from the dataset
def clean_null_values(data):
    data = data.dropna()
    return data

#Function to clean duplicate values from the dataset
def clean_duplicate_values(data):
    data = data.drop_duplicates()
    return data

#Function to convert all text data to lower case
def to_lower_case(data):
    data = data.apply(lambda x: x.astype(str).str.lower())
    return data

#Function to remove special characters & new line characters from the dataset
def remove_special_characters(data):
    data = data.replace(r'[^A-Za-z0-9 ]+', '', regex=True) #remove special characters
    data.replace('/\n', '') #new line characters
    return data

#cleaning up dataset
cleaned_date = drop_columns(df, ['parent_category', 'category_id', 'question_id', 'faq_url', 'que_ans']) #drop columns as they do not contain releveant data
cleaned_date = clean_null_values(cleaned_date)
cleaned_date = clean_duplicate_values(cleaned_date)
cleaned_date = to_lower_case(cleaned_date)
cleaned_date = remove_special_characters(cleaned_date)

#export dataframe to csv
cleaned_date.to_csv('task1/output/cleaned_data.csv', index=False)





