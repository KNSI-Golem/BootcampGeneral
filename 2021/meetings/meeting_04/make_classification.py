import pandas as pd
import numpy as np

from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import RandomizedSearchCV
from sklearn.metrics import accuracy_score

def make_hm_classification(train_X: pd.DataFrame,
                        train_y: pd.Series,
                        test_X: pd.DataFrame):
    
    model = LogisticRegression(random_state=42)
    model.fit(train_X, test_X)
    
    predictions = model.predict(test_X)
    ground_truth = pd.read_csv('data/test_set.csv')['is_cardio_ill']

    acc = accuracy_score(ground_truth, predictions)

    return acc


def evaluate(train_X, train_y, test_X):

    test_y = pd.read_csv('data/adult_test_labels.csv').iloc[test_X.index, :]

    assert train_X.shape[0] == len(train_y), "Lengths of the train data and labels mismatch"
    assert train_X.shape[1] == test_X.shape[1], "Number of features in the train and test datasets mismatch"
    assert test_X.shape[0] == len(test_y), "Lengths of the test data and labels mismatch"

    model = DecisionTreeClassifier()

    distributions = {
        "max_depth": [2, 3, 5, 10, 15],
        "min_samples_split": [2, 5, 10],
        "min_samples_leaf": [2, 5, 10]
    }

    searcher = RandomizedSearchCV(model, distributions, n_jobs=2)
    searcher.fit(train_X, train_y)
    
    best_model = searcher.best_estimator_
    train_score = searcher.best_score_

    # train_score = 0
    # best_model = model
    # best_model.fit(train_X, train_y)

    preds_test = best_model.predict(test_X)
    test_score = accuracy_score(test_y, preds_test)

    return train_score, test_score, best_model