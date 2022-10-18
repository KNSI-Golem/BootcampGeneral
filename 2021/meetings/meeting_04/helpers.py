import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score



def evaluate_test(preds):

    labels = pd.read_csv("data/test_labels.csv")
    assert len(preds) == len(labels)
    acc = accuracy_score(labels, preds)

    return acc




def get_score(train_X: pd.DataFrame,
              test_X: pd.DataFrame,
              train_y: pd.DataFrame,
              test_y: pd.DataFrame):
    
    model = LogisticRegression()
    model.fit(train_X, train_y)
    preds = model.predict(test_X)
    
    acc = accuracy_score(test_y, preds)
    print(f"Accuracy score: {round(100 * acc, 2)} %")
    
    return acc