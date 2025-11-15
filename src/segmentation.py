import pandas as pd

def safe_qcut(series, q):
    try:
        return pd.qcut(series, q, labels=False, duplicates="drop") + 1
    except:
        ranked = series.rank(method="first")
        return pd.qcut(ranked, q, labels=False, duplicates="drop") + 1

def calculate_rfm(df, ref_date, bins=4):
    df = df.copy()
    df["recency"] = (ref_date - df["last_order_date"]).dt.days

    df["recency_score"] = safe_qcut(df["recency"], bins)
    df["frequency_score"] = safe_qcut(df["order_count"], bins)
    df["monetary_score"] = safe_qcut(df["total_spent"], bins)

    df["recency_score"] = (bins + 1) - df["recency_score"]

    return df
