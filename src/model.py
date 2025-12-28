from sklearn.ensemble import GradientBoostingRegressor

def train_model(X,y):
    model=GradientBoostingRegressor(random_state=42)
    model.fit(X,y)
    return model