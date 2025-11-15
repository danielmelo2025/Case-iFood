import os
import gzip
import tarfile
import requests
import pandas as pd


RAW_DIR = "data/raw/"
PROC_DIR = "data/processed/"

os.makedirs(RAW_DIR, exist_ok=True)
os.makedirs(PROC_DIR, exist_ok=True)


# ===============================
# Download de arquivos
# ===============================
def download(url: str, dest_path: str):
    """Baixa arquivo da URL se ainda não existir."""
    if os.path.exists(dest_path):
        print(f"[OK] Já existe: {dest_path}")
        return dest_path

    print(f"[BAIXANDO] {url}")
    r = requests.get(url, stream=True)

    with open(dest_path, "wb") as f:
        f.write(r.content)

    print(f"[OK] Baixado: {dest_path}")
    return dest_path


# ===============================
# Descompressão
# ===============================
def unpack_gz(gz_path: str, out_path: str):
    """Extrai arquivos .gz."""
    with gzip.open(gz_path, "rb") as f_in:
        with open(out_path, "wb") as f_out:
            f_out.write(f_in.read())
    print(f"[OK] Extraído: {out_path}")
    return out_path


def unpack_tar(tar_path: str, out_dir: str):
    """Extrai arquivos .tar.gz."""
    with tarfile.open(tar_path) as tar:
        tar.extractall(out_dir)
    print(f"[OK] Extraído: {out_dir}")
    return out_dir


# ===============================
# Leitura dos dados
# ===============================
def load_orders(path: str) -> pd.DataFrame:
    """Lê o arquivo de pedidos JSON."""
    df = pd.read_json(path, lines=True)
    print(f"[OK] Pedidos lidos: {df.shape}")
    return df


def load_consumers(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"[OK] Consumers lidos: {df.shape}")
    return df


def load_restaurants(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"[OK] Restaurants lidos: {df.shape}")
    return df


def load_ab(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)
    print(f"[OK] AB Test lido: {df.shape}")
    return df


# ===============================
# Tratamento e merge final
# ===============================
def build_analytic_base(orders, consumers, restaurants, ab_ref):
    """Cria a base final consolidada (fato + dimensões)."""

    # Normalizar datas
    orders["order_created_at"] = pd.to_datetime(orders["order_created_at"])

    # Remover pedidos inválidos
    orders = orders[orders["order_total_amount"] > 0]
    orders = orders.dropna(subset=["customer_id"])

    # Selecionar colunas importantes
    orders_min = orders[[
        "order_id",
        "customer_id",
        "merchant_id",
        "order_total_amount",
        "order_created_at"
    ]]

    # Merges
    df = (
        orders_min
        .merge(consumers, on="customer_id", how="left")
        .merge(restaurants, left_on="merchant_id", right_on="id", how="left")
        .merge(ab_ref, on="customer_id", how="left")
    )

    df["is_target"] = df["is_target"].fillna("control")

    print(f"[OK] Base final criada: {df.shape}")
    return df


def save_base(df, filename="base_final.parquet"):
    """Salva a base final em formato parquet."""
    path = PROC_DIR + filename
    df.to_parquet(path)
    print(f"[OK] Salvo em {path}")
    return path
