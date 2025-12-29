import pandas as pd

def load_continuous_dataset(path):
    return pd.read_csv(path, parse_dates=["datetime"], index_col="datetime")

def load_train_test(train_path, test_path):
    train = pd.read_excel(train_path, index_col=0, parse_dates=True)
    test = pd.read_excel(test_path, index_col=0, parse_dates=True)
    return train, test