import numpy as np

def monte_carlo_roi(n_users, sims=10_000):
    np.random.seed(42)
    custo = np.clip(np.random.normal(10, 3, sims), 1, None)
    receita = np.clip(np.random.normal(35, 10, sims), 5, None)
    op = np.clip(np.random.normal(0.15, 0.05, sims), 0, 1)

    roi = []
    for i in range(sims):
        custo_total = custo[i] * n_users
        receita_total = receita[i] * n_users
        custos = custo_total + custo_total * op[i]
        roi.append((receita_total - custos) / custos)

    return np.array(roi)
