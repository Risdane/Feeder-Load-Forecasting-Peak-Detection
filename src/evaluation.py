from sklearn.metrics import mean_absolute_error

def evaluate(y,yhat):
    return mean_absolute_error(y,yhat)