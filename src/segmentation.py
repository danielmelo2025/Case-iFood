import pandas as pd


def build_rfm(df):
    """Calcula tabela RFM a partir dos pedidos."""
    max_date = df["order_created_at"].max()

    rfm = df.groupby("customer_id").agg({
        "order_created_at": lambda x: (max_date - x.max()).days,
        "order_id": "count",
        "order_total_amount": "sum"
    }).reset_index()

    rfm.columns = ["customer_id", "recency", "frequency", "monetary"]

    # Normalizar com quantis
    rfm["R"] = pd.qcut(rfm["recency"], 5, labels=[5,4,3,2,1])
    rfm["F"] = pd.qcut(rfm["frequency"].rank(method="first"), 5, labels=[1,2,3,4,5])
    rfm["M"] = pd.qcut(rfm["monetary"], 5, labels=[1,2,3,4,5])

    rfm["segment"] = rfm["R"].astype(str) + rfm["F"].astype(str) + rfm["M"].astype(str)

    return rfm


def ab_by_segment(rfm, ab_ref, recencia_jan):
    """Cruza segmentos com os resultados do experimento."""
    df_seg = (
        rfm[["customer_id", "segment"]]
        .merge(ab_ref, on="customer_id", how="left")
        .merge(recencia_jan, on="customer_id", how="left")
        .fillna({"is_target": "control", "retido_jan": 0})
    )

    return df_seg.groupby(["segment", "is_target"])["retido_jan"].mean().unstack()
