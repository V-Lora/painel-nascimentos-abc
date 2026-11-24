import pandas as pd
import plotly.express as px
import streamlit as st

st.title("Nascimentos no Grande ABC - SINASC 2026")

d = pd.read_csv("nascimentos_abc_2026.csv", dtype=str, low_memory=False)
d["MES"] = pd.to_numeric(d["DTNASC"].str[2:4], errors="coerce")
MUN = {"351380": "Diadema", "352940": "Maua", "354330": "Ribeirao Pires", "354410": "Rio Grande da Serra", "354780": "Santo Andre", "354870": "Sao Bernardo", "354880": "Sao Caetano"}
d["MUN"] = d["CODMUNRES"].str.strip().str[:6].map(MUN)

st.metric("Total de nascimentos", len(d))

m = d["MUN"].value_counts().reset_index()
m.columns = ["Municipio", "Nascimentos"]
st.plotly_chart(px.bar(m, x="Nascimentos", y="Municipio", orientation="h", text_auto=True, title="Por municipio"))

p = d["PARTO"].value_counts().reset_index()
p.columns = ["Codigo do parto", "Nascimentos"]
st.plotly_chart(px.bar(p, x="Codigo do parto", y="Nascimentos", text_auto=True, title="Tipo de parto"))

s = d.groupby("MES").size().reset_index(name="Nascimentos")
st.plotly_chart(px.line(s, x="MES", y="Nascimentos", markers=True, title="Evolucao mensal"))

peso = pd.to_numeric(d["PESO"], errors="coerce")
dp = d.assign(PESO=peso).dropna(subset=["PESO"])
st.plotly_chart(px.histogram(dp, x="PESO", nbins=50, title="Peso ao nascer"))