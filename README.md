# WorkHuma Senior QA Engineer (AI) Technical Assessment

## Configure Project

`pip install -r requirements.txt`

## Run Tests

To run all tests: `pytest -v task1 task2 task3`
To run for each assessment task e.g: `pytest -v task1`

## Task 1 - Data Quality Assurance

Dataset: https://huggingface.co/datasets/NebulaByte/E-Commerce_FAQs

This dataset consists of a number of question & answers for an E-commerce website. The dataset has 6 features:
parent_category, category_id, category, question_id, question, answer, faq_url and que_ans. 
The dataset consists of 659 rows.

**Python script**: `task1/data_preprocessing.py`

To run script: `python task1/data_preprocessing.py`

This script cleans and preprocesses the E-Commerce_FAQs dataset to produced a cleaned data CSV which is exported to the task1/output/cleaned_data.csv file. The script removes uneccesary columns to leave only category, question and answer. It removes NULL values, removes duplicates, converts all strings to lower case and removes all special characters. 

**Tests**: `task1/test_data_preprocessing.py`

To run tests: `pytest -v task1`

## Task 2 - Performance Testing

**Python Script:** `task2/model_performance.py` is used to generated performance metrics for the selected sample classification dataset & model. 

To run script: `python task2/model_performance.py `

**Tests**: `task2/test_model_performance.py`

To run tests: `pytest -v task2`



## Task 3 - API Endpoint Testing


To run FastAPI: `fastapi dev task3/api.py`

**Tests**: `task3/test_api.py`

To run tests: `pytest -v task3`
