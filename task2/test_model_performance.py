from .model_performance import model_performance

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

    y_test = [0, 1, 2, 0, 1, 2]
    y_pred = [1, 1, 1, 0, 0, 0]
    accuracy, precision, recall, f1 = model_performance(y_test, y_pred)
    assert accuracy == 0.3333333333333333
    assert precision == 0.3333333333333333
    assert recall == 0.3333333333333333
    assert f1 == 0.3333333333333333