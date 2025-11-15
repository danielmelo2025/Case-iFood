def calculate_roi(
    uplift_retencao: float,
    receita_media: float,
    custo_cupom: float,
    n_usuarios: int
):
    """
    Calcula ROI simples baseado em:
    - ganho incremental de receita
    - custo total da campanha
    """

    receita_incremental = uplift_retencao * receita_media * n_usuarios
    custo_total = custo_cupom * n_usuarios

    roi = (receita_incremental - custo_total) / custo_total

    return {
        "receita_incremental": receita_incremental,
        "custo_total": custo_total,
        "ROI": roi
    }
