import sys
import pandas as pd
import streamlit as st
import plotly.express as px

sys.path.append("../src")

from limpeza_dados import converter_k, formatar_mes
from calculo_engajamento import calcular_engajamento
from medias import media_por_grupo
from medias_grupo import resumo_max_min_por_grupo
from categorias import categorizar_post

# ------------------------
# CONFIGURAÇÃO
# ------------------------
st.set_page_config(page_title="Dashboard Instagram 2025", layout="wide")
st.title("📊 Dashboard de Análise Instagram 2025")

# ------------------------
# CARREGAMENTO DOS DADOS
# ------------------------
df = pd.read_excel("Posts_2025.xlsx")

# Tratamento
colunas = ["Curtidas", "Coment.", "Compart.", "Salvos", "Visualiz.", "Alcance", "Visitas", "Seguid."]
for col in colunas:
    df[col] = df[col].apply(converter_k)

df = formatar_mes(df)
df = calcular_engajamento(df)
df["Categoria"] = df["Título / Tema do Post"].map(categorizar_post)

# ------------------------
# FILTROS
# ------------------------
st.sidebar.header("Filtros")

formato = st.sidebar.multiselect(
    "Formato",
    options=df["Formato"].unique(),
    default=df["Formato"].unique()
)

df = df[df["Formato"].isin(formato)]

# ------------------------
# MÉTRICAS PRINCIPAIS
# ------------------------
st.subheader("📌 Métricas Gerais")

col1, col2, col3 = st.columns(3)

col1.metric("Engajamento Médio", round(df["Engajamento"].mean(), 2))
col2.metric("Alcance Médio", round(df["Alcance"].mean(), 2))
col3.metric("Seguidores Médios", round(df["Seguid."].mean(), 2))

# ------------------------
# GRÁFICO: ENGAGEMENTO POR FORMATO
# ------------------------
st.subheader("📈 Engajamento Médio por Formato")

df_medias = (
    df.groupby("Formato")[["Engajamento"]]
    .mean()
    .reset_index()
)

fig = px.bar(
    df_medias,
    x="Formato",
    y="Engajamento",
    text_auto=".2s"
)

st.plotly_chart(fig, use_container_width=True)

# ------------------------
# TABELA RESUMO MAX / MIN
# ------------------------
st.subheader("🏆 Destaques por Métrica")

colunas_metricas = ["Curtidas", "Coment.", "Compart.", "Salvos", "Engajamento"]
df_resumo = resumo_max_min_por_grupo(df, colunas_metricas, grupo="Formato")

st.dataframe(df_resumo.round(2))
