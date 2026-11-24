# Painel de Monitoramento de Nascimentos — Grande ABC

Dashboard interativo dos nascimentos registrados no SINASC 2026 (Ministério da Saúde)
para os sete municípios do Grande ABC paulista.

# Painel de Monitoramento de Nascimentos — Grande ABC

**Painel publicado:** https://painel-nascimentos-abc-bc2gcfvtjaihqemc6nsmnr.streamlit.app

Dashboard interativo dos nascimentos registrados no SINASC 2026...

## Fonte dos dados
SINASC — Sistema de Informação sobre Nascidos Vivos (DATASUS / Ministério da Saúde).
Dados abertos: https://dadosabertos.saude.gov.br/dataset/sistema-de-informacao-sobre-nascidos-vivos-sinasc

## Municípios
Santo André, São Bernardo do Campo, São Caetano do Sul, Diadema, Mauá,
Ribeirão Pires e Rio Grande da Serra.

## Preparação dos dados
O arquivo original do SINASC contém registros de todo o Brasil (530 MB).
A preparação lê a base em blocos de 200 mil linhas, filtra os sete códigos
IBGE do Grande ABC e grava o recorte em `nascimentos_abc_2026.csv`
(15.865 registros, 62 colunas).

## Como executar
    pip install -r requirements.txt
    streamlit run app2.py

## Tecnologias
Python, Pandas, Plotly e Streamlit.