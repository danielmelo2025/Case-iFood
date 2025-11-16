# Case Técnico de Data Analysis – iFood

Este repositório contém a solução completa do Case Técnico de Data Analysis do iFood, com:

- ETL completo
- Análise estatística do teste A/B
- Segmentação de usuários (RFM)
- Simulação de viabilidade financeira
- Recomendações para negócio
- Notebook 100% executável no Google Colab

---

## 1. Executar o Notebook

Clique abaixo para rodar diretamente no Google Colab:

[![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/drive/1C66WFOfESRlab8i9kmMVH3VC1oEfusog?authuser=1#scrollTo=AGiVcQcJGIOE)

Isso garante reprodutibilidade sem necessidade de instalação local.

---

## 2. Estrutura do Repositório

```text
Case-iFood/
│
├── README.md
├── requirements.txt        # Dependências (usado para execução local)
│
├── notebooks/
│   └── Case_iFood_Daniel_Leite.ipynb    # Notebook principal com ETL, A/B, RFM e ROI
│
├── src/                    
│   ├── etl.py
│   ├── ab_test.py
│   ├── segmentation.py
│   └── finance_roi.py
│
└── reports/
    └── Case_iFood_Daniel_Leite.pdf # Relatório final apresentado às lideranças
```
# 3. Instruções de Execução Local

Clone o repositório: 
```
git clone https://github.com/danielmelo2025/Case-iFood.git
cd Case-iFood
```

Instale dependências:
```
pip install -r requirements.txt
```

Execute o notebook:
```
jupyter notebook notebooks/case_ifood.ipynb
```

Observação: como a solução é totalmente compatível com Google Colab, recomenda-se executar por lá.

# 4. Objetivo do Case
Avaliar o impacto de uma campanha de cupons por meio de um teste A/B, incluindo:
- Definição de indicadores de sucesso
- Validação estatística
- Entendimento de comportamento dos usuários via segmentação
- Avaliação financeira da ação
- Recomendações e próximos passos

# 5. Entregáveis conforme solicitado no case

- Repositório GitHub
- Notebook com análise
- README contendo instruções
Relatório final em PDF

# 6. Autor
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Daniel%20Leite-white?style=for-the-badge&logo=linkedin&logoColor=0A66C2)](https://www.linkedin.com/in/daniel-leite-93862b160/)
