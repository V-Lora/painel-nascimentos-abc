import pandas as pd

amostra = pd.read_csv("SINASC_2026.csv", sep=";", encoding="latin-1",
                      dtype=str, nrows=20)

print("Colunas:", len(amostra.columns))
print(amostra["CODMUNRES"].head(10).to_string())
