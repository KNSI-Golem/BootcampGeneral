from operator import is_
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix

def print_metric_error(original_func, user_func, y_true, y_pred, is_weighted=False):
    print('Sample of the data:', y_true[:10], y_pred[:10])
    if is_weighted:
        print('True vals:', original_func(y_true[:10], y_pred[:10], average='macro'), original_func(y_true, y_pred, average='macro'))
    else:
        print('True vals:', original_func(y_true[:10], y_pred[:10]), original_func(y_true, y_pred))
    print('Your scores:', user_func(y_true[:10], y_pred[:10]), user_func(y_true, y_pred))

def gen_data(is_binary):
    size = np.random.randint(1000, 10000)
    if is_binary:
        y_true, y_pred = [np.random.rand(size) > np.random.rand() for _ in (0, 1)]
    else:
        n_classes = np.random.randint(3, 10)
        y_true, y_pred = [np.random.randint(0, n_classes, size) for _ in (0, 1)]
    return y_true, y_pred

def compare_output(original_output, user_output):
    if type(user_output) in [int, float]:
        user_output = np.float64(user_output)
    
    if original_output.shape != user_output.shape:
        return False
    
    if len(original_output.shape) > 1:
        return (original_output==user_output).all()
    
    return round(original_output, 12) == round(user_output, 12)

def test_metric(metric_func, user_func):
    is_weighted = metric_func in [precision_score, recall_score, f1_score]
    for _ in range(100):
        y_true, y_pred = gen_data(is_binary=True)
        try:
            assert(compare_output(metric_func(y_true, y_pred), user_func(y_true, y_pred)))
        except Exception as e:
            print(e, 'Binary case failed')
            print_metric_error(metric_func, user_func, y_true, y_pred)
            return y_true, y_pred

    for _ in range(100):
        y_true, y_pred = gen_data(is_binary=False)
        try:
            if is_weighted:
                assert(compare_output(metric_func(y_true, y_pred, average='macro'), user_func(y_true, y_pred)))
            else:
                assert(compare_output(metric_func(y_true, y_pred), user_func(y_true, y_pred)))
        except Exception as e:
            print(e, 'Multiclass case failed')
            print_metric_error(metric_func, user_func, y_true, y_pred, is_weighted)
            return y_true, y_pred
    return None, None
