import pandas as pd
import numpy as np
from sklearn import datasets

import pandas as pd

df = pd.read_csv("hf://datasets/NebulaByte/E-Commerce_FAQs/FAQs.csv")

def drop_columns(data, columns):
    data.drop(columns, axis=1, inplace=True)
    return data

def clean_null_values(data):
    data = data.dropna()
    return data

def clean_duplicate_values(data):
    data = data.drop_duplicates()
    return data

def to_lower_case(data):
    data = data.apply(lambda x: x.astype(str).str.lower())
    return data

def remove_special_characters(data):
    data = data.replace(r'[^A-Za-z0-9 ]+', '', regex=True) #remove special characters
    data.replace('/\n', '') #new line characters
    return data

#cleaning up dataset
df2 = drop_columns(df, ['parent_category', 'category_id', 'question_id', 'faq_url', 'que_ans'])
df2 = clean_null_values(df2)
df2 = clean_duplicate_values(df2)
df2 = to_lower_case(df2)
df2 = remove_special_characters(df2)





