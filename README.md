# WorkHuman Senior QA Engineer (AI) Technical Assessment

## Configure Project

`pip install -r requirements.txt`

## Run Tests

To run all tests: `pytest -v task1 task2 task3`

To run for each assessment task e.g: `pytest -v task1`

The Jenkinsfile will enable the tests to run as part of a CI/CD pipeline

## Task 1 - Data Quality Assurance

Dataset: https://huggingface.co/datasets/NebulaByte/E-Commerce_FAQs

This dataset consists of a number of question & answers for an E-commerce website. The dataset has 8 features:
parent_category, category_id, category, question_id, question, answer, faq_url and que_ans. 
The dataset consists of 659 rows.

**Python script**: `task1/data_preprocessing.py`

To run script: `python task1/data_preprocessing.py`

The script uses numoy, pandas and scikit-learn.

This script cleans and preprocesses the E-Commerce_FAQs dataset to produced a cleaned data CSV which is exported to the task1/output/cleaned_data.csv file. The script removes uneccesary columns to leave only category, question and answer. It removes NULL values, removes duplicates, converts all strings to lower case and removes all special characters. 

**Tests**: `task1/test_data_preprocessing.py`

To run tests: `pytest -v task1`

## Task 2 - Performance Testing

**Python Script:** `task2/model_performance.py` is used to generated performance metrics for the selected sample classification dataset & model. It uses scikit-learn, pandas and transformers. 

To run script: `python task2/model_performance.py`

This will generate performance metrics for a basic model & dataset which has been split into a train, test and validation for cross-validation. Performance metrics will be calculated for the test and validation set and written to the task2/outputs/model_metrics.txt

The script also validates the model outputs against a set of predefined queries and expected responses. A pre-defined context is passed to the model along with the question. The responses that are genererated are written to the task2/output/model_answers.txt for review and oversight which is necessary for human in the loop validation. More work is needed here to ensure the response that is generated more closely matches the pre-set responses for the set of questions. To improve the models response it could be trained on a set of specific technical documents. A RAG Architcture would be a good fit for that. With the addition of a RAG architecture the model would be capable of more accuratley responding to the specific technical support questions. 

**Tests**: `task2/test_model_performance.py`

To run tests: `pytest -v task2`

Tests cover testing cross-validation of data, testing the pre-processing of data and testing the model validation with preset questions and answers. More work is needed on this test as it is currently checking for a direct match on the generated response and the pre-set response. A cosine similarity would offer better insight into how accurate the model is generating responses. 

## Task 3 - API Endpoint Testing

To run FastAPI: `fastapi dev task3/api.py`

This script contains a number of GET endpoints, including one with a mocked database and one with an SQLite database. 
The GET /query request takes a string as the query param and will throw a 400 error if there is no parameter provided. 
The GET /query/{query} request queries the mocked db and will throw a 400 error if the query parameter is not provided and a 404 if it's not found Further work needed on this as tests are failing. 
The GET /query/sql/{query} request queries an SQLite db and will throw a 400 error if the query parameter is not provided and a 404 if it's not found. Further work needed on this as tests are failing. 

**Tests**: `task3/test_api.py`

A test suite for the `/query` endpoint that handles user queries. Tests cover testing for valid query parameters, testing for valid query parameter with mocked db, testing for valid query parameter with sql database, test for non-existant query in mocked db, test for no query parameter and test for query parameter not provided. 

To run tests: `pytest -v task3`
