import numpy as np
from .model_performance import cross_validation, model_performance

def test_cross_validation():
    X = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])
    y = np.array([0, 1, 0, 1])

    X_train, X_test, X_val, y_train, y_test, y_val = cross_validation(X, y)

    assert len(X_train) == 2
    assert len(X_test) == 1
    assert len(X_val) == 1
    assert len(y_train) == 2
    assert len(y_test) == 1
    assert len(y_val) == 1

    assert np.array_equal(X_train, np.array([[1, 2], [7, 8]]))
    assert np.array_equal(X_test, np.array([[3, 4]]))
    assert np.array_equal(X_val, np.array([[5, 6]]))
    assert np.array_equal(y_train, np.array([0, 1]))
    assert np.array_equal(y_test, np.array([0]))
    assert np.array_equal(y_val, np.array([1]))

def test_model_performance():
    y_test = [0, 1, 2, 0, 1, 2]
    y_pred = [0, 1, 2, 0, 1, 2]
    accuracy, precision, recall, f1 = model_performance(y_test, y_pred)
    assert accuracy == 1.0
    assert precision == 1.0
    assert recall == 1.0
    assert f1 == 1.0

    y_test = [0, 1, 2, 0, 1, 2]
    y_pred = [2, 1, 0, 0, 1, 2]
    accuracy, precision, recall, f1 = model_performance(y_test, y_pred)
    assert accuracy == 0.6666666666666666
    assert precision == 0.6666666666666666
    assert recall == 0.6666666666666666
    assert f1 == 0.6666666666666666

    y_val = [0, 1, 2, 0, 1, 2]
    y_pred = [1, 1, 1, 0, 0, 0]
    accuracy, precision, recall, f1 = model_performance(y_val, y_pred)
    assert accuracy == 0.3333333333333333
    assert precision == 0.3333333333333333
    assert recall == 0.3333333333333333
    assert f1 == 0.3333333333333333