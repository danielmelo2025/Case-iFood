# Case Técnico de Data Analysis – iFood

Este repositório contém a solução completa do Case Técnico de Data Analysis do iFood, incluindo:

- Notebook de Processamento e Análise de Dados
- Pipeline de ETL
- Análise estatística do teste A/B
- Segmentação de usuários (RFM)
- Simulação de viabilidade financeira
- Relatório final para a liderança

A solução foi construída para ser reprodutível, clara e pronta para produção, seguindo boas práticas de analytics engineering, estatística e storytelling de dados.


# 1. Estrutura do Repositório
``` text
ifood-case/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── notebooks/
│   └── case_ifood.ipynb          # Notebook principal com ETL + A/B + segmentações
│
├── src/
│   ├── etl.py                    # Download, descompressão, leitura e limpeza
│   ├── ab_test.py                # Testes estatísticos e métricas A/B
│   ├── segmentation.py           # Segmentação RFM + análises por cluster
│   └── finance_roi.py            # Premissas + modelo de viabilidade financeira
│
├── data/
│   ├── raw/                      # Arquivos .gz / .tar.gz baixados
│   └── processed/                # Parquet limpos e bases tratadas
│
└── reports/
    └── relatorio_final.pdf       # Arquivo final explicando conclusões e recomendações
```

# 2. Objetivo do Case

O objetivo é analisar um teste A/B realizado pelo iFood para avaliar o impacto de um cupom especial na retenção de usuários, além de:

- Avaliar impacto estatístico do experimento
- Entender quais segmentos se beneficiam mais
- Calcular a viabilidade financeira da ação
- Propor recomendações estratégicas para negócio
- Sugerir próximos passos com estimativa de impacto

Toda a solução está implementada no notebook case_ifood.ipynb.

# 3. Pré-requisitos

Instale as dependências:
``` text
pip install -r requirements.txt
```

Abra o notebook:
``` text
jupyter notebook notebooks/case_ifood.ipynb
```
O notebook:

Faz o download automático dos arquivos do case
- Descompacta e trata os dados
- Cria os datasets analíticos
- Realiza toda a análise A/B
- Gera segmentações
- Cria gráficos e tabelas
- Exporta artefatos usados no relatório final

Não é necessário baixar manualmente os dados — tudo é feito pelo módulo etl.py.

# 4. ETL — Extração, Transformação e Carregamento
Todo o pipeline está no módulo: ``` text src/etl.py ```

O ETL realiza:

- Download dos arquivos originais (.gz e .tar.gz)
-  Descompressão automática
- Leitura otimizada dos 3.6M pedidos
- Normalização de schemas
- Remoção de erros e registros inválidos
- Tratamento de datas e monetização
- Criação de base analítica única (fato + dimensões)
- Exportação em Parquet para processamento eficiente

A base final fica salva em: ``` text data/processed/base_final.parquet ```

# 5. Análise do Teste A/B
A análise estatística do experimento está implementada em: ``` text src/ab_test.py ```

Métricas avaliadas:
- Retenção (usuários que voltaram no período seguinte)
- Total de pedidos por usuário
- Receita média
- Ticket médio
- Atividade mensal
- Testes estatísticos
- Z-test para proporções (retenção)
- Welch T-test (ticket médio)
- Bootstrap

Os resultados são discutidos no relatório.


# 6. Segmentação de Usuários
Segmentação implementada no módulo: ``` text src/segmentation.py ```

- RFM (Recency, Frequency, Monetary)
- Quantis para criação de score R, F e M
- Criação do segmento via concatenação R+F+M
- Análise da performance do A/B dentro de cada segmento
- Essa parte é essencial para responder o item 2 do case


# 7. Viabilidade Financeira (ROI)
Simulações e premissas implementadas em: ``` text src/finance_roi.py ```

Inclui:
- Estimativa de custo do cupom
- Incrementalidade observada
- Modelo de cálculo do impacto financeiro
- ROI e Payback do experimento
- Cenários otimista / base / pessimista

 # 8. Relatório Final (PDF)
O documento ```text reports/relatorio_final.pdf ```contém:

Explicação simples e visual para liderança
- Conclusões do teste
- Recomendações estratégicas
- Tamanho estimado do impacto
- Sugestão de próximos testes A/B
- Premissas explicitadas 


# 10. Autor
Daniel Leite


