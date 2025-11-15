import pandas as pd
import numpy as np
import gzip
import tarfile
import requests
from io import BytesIO

def download_file(url, path):
    print(f"Baixando: {url}")
    r = requests.get(url, stream=True)
    with open(path, "wb") as f:
        for chunk in r.iter_content(chunk_size=1024*1024):
            f.write(chunk)
    print(f"Salvo em {path}")

def read_orders_chunks(path, chunksize=150_000, usecols=None):
    with gzip.open(path, "rt") as f:
        for chunk in pd.read_json(f, lines=True, chunksize=chunksize):
            if usecols:
                chunk = chunk[usecols]
            chunk["order_created_at"] = pd.to_datetime(chunk["order_created_at"])
            yield chunk

def load_ab_ref(path):
    with tarfile.open(path, "r:gz") as tar:
        members = [m for m in tar.getmembers() if m.name.endswith(".csv")]
        member = members[0]
        raw = tar.extractfile(member).read()
        df = pd.read_csv(BytesIO(raw), encoding="utf-8")
        return df

def prepare_orders(df):
    df = df.rename(columns={"merchant_id": "restaurant_id"})
    df["order_created_at"] = pd.to_datetime(df["order_created_at"])
    df = df.dropna(subset=["order_id", "customer_id", "restaurant_id"])
    return df[[
        "order_id", "customer_id", "restaurant_id",
        "order_created_at", "order_total_amount", "order_scheduled"
    ]]

def prepare_consumers(df):
    df = df.drop_duplicates(subset=["customer_id"])
    return df

def prepare_restaurants(df):
    df = df.rename(columns={"id": "restaurant_id"})
    df["created_at"] = pd.to_datetime(df["created_at"])
    return df.drop_duplicates(subset=["restaurant_id"])

def prepare_ab(df):
    df = df.rename(columns={"is_target": "ab_group"})
    return df.drop_duplicates(subset=["customer_id"])
