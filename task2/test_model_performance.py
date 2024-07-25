import numpy as np
from .model_performance import cross_validation, model_performance, validate_model_outputs

def test_cross_validation():
    # Create a sample dataset for testing
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([0, 1, 0, 1])

    # Call the cross_validation function to split the data into train, test, and validation sets
    X_train, X_test, X_val, y_train, y_test, y_val = cross_validation(X, y, test_size=0.2, random_state=42, val_size=0.25)

    # Check if the data is split correctly
    assert len(X_train) == 2
    assert len(X_test) == 1
    assert len(X_val) == 1
    assert len(y_train) == 2
    assert len(y_test) == 1
    assert len(y_val) == 1

    # Check if the data values are correct
    assert np.array_equal(X_train, np.array([[1, 2], [5,6]]))
    assert np.array_equal(X_test, np.array([[3, 4]]))
    assert np.array_equal(X_val, np.array([[7, 8]]))
    assert np.array_equal(y_train, np.array([0, 0]))
    assert np.array_equal(y_test, np.array([1]))
    assert np.array_equal(y_val, np.array([1]))

def test_model_performance():
    #Create sample data for testing
    y_test = [0, 1, 2, 0, 1, 2]
    y_pred = [0, 1, 2, 0, 1, 2]
    #Calculate model performance metrics using the test set
    accuracy, precision, recall, f1 = model_performance(y_test, y_pred)
    #Check if the metrics are calculated correctly
    assert accuracy == 1.0
    assert precision == 1.0
    assert recall == 1.0
    assert f1 == 1.0

    #Create sample data for testing
    y_test = [0, 1, 2, 0, 1, 2]
    y_pred = [2, 1, 0, 0, 1, 2]
    #Calculate model performance metrics using the test set
    accuracy, precision, recall, f1 = model_performance(y_test, y_pred)
    #Check if the metrics are calculated correctly
    assert accuracy == 0.6666666666666666
    assert precision == 0.6666666666666666
    assert recall == 0.6666666666666666
    assert f1 == 0.6666666666666666

    #Create sample data for testing
    y_val = [0, 1, 2, 0, 1, 2]
    y_pred = [1, 1, 1, 0, 0, 0]
    #Calculate model performance metrics using the validation set
    accuracy, precision, recall, f1 = model_performance(y_val, y_pred)
    #Check if the metrics are calculated correctly
    assert accuracy == 0.3333333333333333
    assert precision == 0.3333333333333333
    assert recall == 0.3333333333333333
    assert f1 == 0.3333333333333333
    
def test_validate_model_outputs():
    # Call the validate_model_outputs function
    expected_answers, model_answers = validate_model_outputs()

    # Check if the number of expected answers matches the number of model answers
    assert len(expected_answers) == len(model_answers)

    # Check if each expected answer matches the corresponding model answer
    for i in range(len(expected_answers)):
        assert expected_answers[i] == model_answers[i]