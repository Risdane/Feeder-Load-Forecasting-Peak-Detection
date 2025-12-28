import pandas as pd

def load_train_test(train_path, test_path):
    return pd.read_excel(train_path), pd.read_excel(test_path)