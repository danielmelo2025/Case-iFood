# Case Técnico de Data Analysis – iFood

Este repositório contém a solução completa do **Case Técnico de Data Analysis do iFood**, incluindo:

- **Notebook de Processamento e Análise de Dados**
- **Pipeline de ETL**
- **Análise estatística do teste A/B**
- **Segmentação de usuários (RFM)**
- **Simulação de viabilidade financeira**
- **Relatório final para a liderança**

A solução foi construída para ser **reprodutível, clara e pronta para produção**, seguindo boas práticas de analytics engineering, estatística e storytelling de dados.

---

## 📁 1. Estrutura do Repositório

ifood-case/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/
│ └── case_ifood.ipynb # Notebook principal com ETL + A/B + segmentações
│
├── src/
│ ├── etl.py # Download, descompressão, leitura e limpeza
│ ├── ab_test.py # Testes estatísticos e métricas A/B
│ ├── segmentation.py # Segmentação RFM + análises por cluster
│ └── finance_roi.py # Premissas + modelo de viabilidade financeira
│
├── data/
│ ├── raw/ # Arquivos .gz / .tar.gz baixados
│ └── processed/ # Parquet limpos e bases tratadas
│
└── reports/
└── relatorio_final.pdf # Arquivo final explicando conclusões e recomendações

yaml
Copiar código

---

## 🎯 2. Objetivo do Case

O objetivo é analisar um **teste A/B** realizado pelo iFood para avaliar o impacto de um **cupom especial na retenção de usuários**, além de:

- Avaliar impacto estatístico do experimento  
- Entender quais segmentos se beneficiam mais  
- Calcular a viabilidade financeira da ação  
- Propor recomendações estratégicas para negócio  
- Sugerir próximos passos com estimativa de impacto  

Toda a solução está implementada no notebook:

notebooks/case_ifood.ipynb

yaml
Copiar código

---

## 🔧 3. Pré-requisitos

Instale as dependências:

```bash
pip install -r requirements.txt
Abra o notebook:

bash
Copiar código
jupyter notebook notebooks/case_ifood.ipynb
O notebook:

Faz o download automático dos arquivos do case

Descompacta e trata os dados

Cria os datasets analíticos

Realiza toda a análise A/B

Gera segmentações RFM

Cria gráficos e tabelas

Exporta artefatos usados no relatório final

Não é necessário baixar manualmente os dados — tudo é feito pelo módulo:

bash
Copiar código
src/etl.py
🧼 4. ETL — Extração, Transformação e Carregamento
O pipeline está em:

bash
Copiar código
src/etl.py
O ETL realiza:

Download dos arquivos originais (.gz e .tar.gz)

Descompressão automática

Leitura otimizada dos 3.6M pedidos

Normalização de schemas

Remoção de erros e registros inválidos

Tratamento de datas e monetização

Criação de base analítica única (fato + dimensões)

Exportação em Parquet para processamento eficiente

A base final é salva em:

bash
Copiar código
data/processed/base_final.parquet
🧪 5. Análise do Teste A/B
Implementada em:

bash
Copiar código
src/ab_test.py
Métricas avaliadas:

Retenção (usuários que voltaram no período seguinte)

Total de pedidos por usuário

Receita média

Ticket médio

Atividade mensal

Testes estatísticos utilizados:

Z-test para proporções (retenção)

Welch T-test para médias (ticket médio)

(Opcional) Bootstrap para robustez

Resultados descritos no relatório final.

🧩 6. Segmentação de Usuários
Segmentação implementada em:

bash
Copiar código
src/segmentation.py
Modelo:

RFM (Recency, Frequency, Monetary)

Quantis para score R, F e M

Segmentos gerados via combinação R+F+M

Análise do impacto do cupom dentro de cada segmento

Essencial para responder o item 2 do case.

💰 7. Viabilidade Financeira (ROI)
Simulações implementadas em:

bash
Copiar código
src/finance_roi.py
Inclui:

Estimativa de custo do cupom

Incrementalidade observada

Modelo de impacto financeiro

ROI e Payback

Cenários:

Otimista

Base

Pessimista

📄 8. Relatório Final (PDF)
Disponível em:

bash
Copiar código
reports/relatorio_final.pdf
O relatório contém:

Explicação simples e visual para liderança

Conclusões do teste

Recomendações estratégicas

Tamanho estimado do impacto

Sugestão de próximos testes A/B

Premissas explicitadas

👤 10. Autor
Daniel Leite

Analista de Dados
Marketing Digital • Growth • Modelagem Estatística
