def check_missing_values(df):
    return df.isna().sum()

def basic_feature_summary(df):
    return df.describe()