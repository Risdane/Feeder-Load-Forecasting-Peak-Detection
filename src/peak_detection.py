import numpy as np

def compute_residuals(y_true, y_pred):
    return y_true - y_pred

def detect_peaks(residuals, percentile=95):
    threshold = np.percentile(residuals, percentile)
    return residuals > threshold, threshold