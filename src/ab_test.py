import numpy as np
from scipy.stats import ttest_ind
from statsmodels.stats.proportion import proportions_ztest

def retention_ztest(df):
    success = [
        df[df["ab_group"] == "target"]["retido_jan"].sum(),
        df[df["ab_group"] == "control"]["retido_jan"].sum()
    ]
    total = [
        df[df["ab_group"] == "target"].shape[0],
        df[df["ab_group"] == "control"].shape[0]
    ]
    return proportions_ztest(success, total)

def welch_ttest(a, b):
    return ttest_ind(a, b, equal_var=False)
