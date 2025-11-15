import pandas as pd
import numpy as np
from statsmodels.stats.proportion import proportions_ztest
from scipy.stats import ttest_ind


# ===============================
# Métricas básicas do experimento
# ===============================
def retention_by_group(ab_base):
    """Retenção média por grupo (0/1)."""
    return ab_base.groupby("is_target")["retido_jan"].mean()


def ztest_retention(ab_base):
    """Z-test para proporção de retenção."""
    target = ab_base[ab_base["is_target"] == "target"]
    control = ab_base[ab_base["is_target"] == "control"]

    success = [target["retido_jan"].sum(), control["retido_jan"].sum()]
    nobs = [len(target), len(control)]

    z, p = proportions_ztest(success, nobs)
    return z, p


# ===============================
# Ticket médio e receita
# ===============================
def welch_test_ticket(dezembro_df):
    """T-test de Welch para ticket médio."""
    target_vals = dezembro_df[dezembro_df["is_target"]=="target"]["order_total_amount"]
    control_vals = dezembro_df[dezembro_df["is_target"]=="control"]["order_total_amount"]

    t, p = ttest_ind(target_vals, control_vals, equal_var=False)
    return t, p
