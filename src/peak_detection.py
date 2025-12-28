import numpy as np

def detect(res, q=95):
    return res>np.percentile(res,q)