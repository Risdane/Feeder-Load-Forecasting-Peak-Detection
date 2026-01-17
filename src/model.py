from sklearn.ensemble import GradientBoostingRegressor

def build_model():
    return GradientBoostingRegressor(
        n_estimators=300,
        learning_rate=0.05,
        max_depth=4,
        random_state=42
    )

def train_model(model, X_train, y_train):
    model.fit(X_train, y_train)
    return model