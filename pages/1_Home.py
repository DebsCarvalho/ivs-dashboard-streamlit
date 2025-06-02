import streamlit as st
import pandas as pd
import plotly.express as px
import json
import plotly.graph_objects as go
from plotly.graph_objs.layout import Shape


st.set_page_config(page_title="Dashboard de Vulnerabilidade Social", layout="wide")

st.title("Dados da Vulnerabilidade Social no Brasil")
st.markdown("Este dashboard apresenta Indicadores relacionados ao IVS no Brasil e seus Estados.")

cores_ivs = {
    "Muito Baixo": "#1a60a8",
    "Baixo": "#73acdc",
    "Médio": "#F2EFBB",
    "Alto": "#F29D7E",
    "Muito Alto": "#F23030"
}

@st.cache_data
def carregar_dados():
    df = pd.read_csv('data/full_data.csv', encoding='latin1')
    df.columns = df.columns.str.strip()

    colunas_float = [
        'IVS', 'Renda per capita 2019', 'Renda per capita 2020', 'Renda per capita 2021',
        '% Trabalho Informal 2024', 'Taxa de analfabetismo (18+) 2021'
    ]
    for col in colunas_float:
        if col in df.columns:
            df[col] = df[col].astype(float)

    def categorizar_ivs(valor):
        if valor <= 0.200:
            return "Muito Baixo"
        elif valor <= 0.300:
            return "Baixo"
        elif valor <= 0.400:
            return "Médio"
        elif valor <= 0.500:
            return "Alto"
        else:
            return "Muito Alto"

    df['Faixa_IVS'] = df['IVS'].apply(categorizar_ivs)
    return df

@st.cache_data
def carregar_geojson():
    try:
        with open("data/brazil-states.geojson", "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        st.error("Erro ao carregar o arquivo GeoJSON.")
        return None

# Carregar dados
df_completo = carregar_dados()
df_brasil = df_completo.iloc[0]
df = df_completo.iloc[1:].copy()
geojson = carregar_geojson()

# Espaçamento
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("#### Dados de Referência - Brasil")

col1, col2, col3, col4, col5 = st.columns(5)

# Estilo base para os blocos
card_style = """
    background-color: #39568C;
    padding: 0.5rem 0.4rem;
    border-radius: 0.5rem;
    border: 1px solid #ddd;
    text-align: center;
    font-weight: bold;
    font-size: 0.95rem;
    color: #00000;
"""

value_style = "font-size: 1.15rem; font-weight: bold; color: #00000; margin-top: 0.3rem;"

with col1:
    st.markdown(f"""
    <div style="{card_style}">
        Analfabetismo (18+)
        <div style="{value_style}">{df_brasil['Taxa de analfabetismo (18+) 2021']}%</div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    <div style="{card_style}">
        Trabalho Informal
        <div style="{value_style}">{df_brasil['% Trabalho Informal 2024']}%</div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown(f"""
    <div style="{card_style}">
        Renda 2019
        <div style="{value_style}">R$ {df_brasil['Renda per capita 2019']:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col4:
    st.markdown(f"""
    <div style="{card_style}">
        Renda 2020
        <div style="{value_style}">R$ {df_brasil['Renda per capita 2020']:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown(f"""
    <div style="{card_style}">
        Renda 2021
        <div style="{value_style}">R$ {df_brasil['Renda per capita 2021']:,.2f}</div>
    </div>
    """, unsafe_allow_html=True)

# Espaçamento
st.markdown("<br>", unsafe_allow_html=True)

# Sidebar
st.sidebar.header("Filtros")
estado = st.sidebar.selectbox("Selecione o estado:", sorted(df["UF"].unique()))
df_estado = df[df["UF"] == estado].iloc[0]

# Espaçamento
st.markdown("<br>", unsafe_allow_html=True)

st.markdown(f"#### Indicadores por estado: **{estado}**")

# Estilo dos Cards
st.markdown("""
<style>
.card {
    background-color: #ffffff;
    padding: 0.6rem 0.6rem;
    border-radius: 0.5rem;
    border: 1px solid #4A90E2;
    text-align: center;
    margin: 0.8rem 0.8rem;
    min-height: 90px;
    box-shadow: 0 1px 2px rgba(0,0,0,0.05);
}
.card h2 {
    font-size: 1.1rem;
    margin: 0.2rem 0 0;
    color: #222;
}
.card p {
    font-size: 0.95rem;
    color: #555;
    margin: 0;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)


# Linha 1 - IVS, Analfabetismo, Informalidade
col1, col2, col3 = st.columns(3)
with col1:
    st.markdown(f"<div class='card'><p>IVS</p><h2>{df_estado['IVS']:.3f}</h2></div>", unsafe_allow_html=True)
with col2:
    st.markdown(f"<div class='card'><p>Taxa de Analfabetismo (18+)</p><h2>{df_estado['Taxa de analfabetismo (18+) 2021']}%</h2></div>", unsafe_allow_html=True)
with col3:
    st.markdown(f"<div class='card'><p>% Trabalho Informal</p><h2>{df_estado['% Trabalho Informal 2024']}%</h2></div>", unsafe_allow_html=True)

# Linha 2 - Renda per capita
col4, col5, col6 = st.columns(3)
with col4:
    st.markdown(f"<div class='card'><p>Renda per capita 2019</p><h2>R$ {df_estado['Renda per capita 2019']:,.2f}</h2></div>", unsafe_allow_html=True)
with col5:
    st.markdown(f"<div class='card'><p>Renda per capita 2020</p><h2>R$ {df_estado['Renda per capita 2020']:,.2f}</h2></div>", unsafe_allow_html=True)
with col6:
    st.markdown(f"<div class='card'><p>Renda per capita 2021</p><h2>R$ {df_estado['Renda per capita 2021']:,.2f}</h2></div>", unsafe_allow_html=True)

# Mapa
if geojson is not None:
    st.subheader("Mapa por faixa do **IVS** (*Indicador de Vulnerabilidade Social*)")
    choromap = px.choropleth_map(
        df,
        geojson=geojson,
        locations="UF",
        featureidkey="properties.sigla",
        color="Faixa_IVS",
        color_discrete_map=cores_ivs,
        center={"lat": -14.2, "lon": -51.9},
        zoom=2.7,
        hover_name="UF",
        hover_data={"Faixa_IVS": True, "IVS": ':.3f', "UF": False}
    )

    choromap.update_layout(
        geo=dict(
            bgcolor="#90cce8",
            showland=True,
            landcolor="#69965a",
            showcountries=True,
            countrycolor="#cdd0d1"
        ),
        margin={"r": 0, "t": 0, "l": 0, "b": 0},
        uirevision=True,
        showlegend=False
        )

# Legenda embutida no mapa
faixas = [
    ("Muito Baixo ≤ 0.200", "#1a60a8"),
    ("Baixo 0.201 a 0.300", "#73acdc"),
    ("Médio 0.301 a 0.400", "#F2EFBB"),
    ("Alto 0.401 a 0.500", "#F29D7E"),
    ("Muito Alto > 0.500", "#F23030")
]

# Posição e tamanho
x_base = 0.78
y_base = 0.2
height = 0.03
width = 0.03
spacing = 0.01

# Fundo da legenda
choromap.add_shape(
    type="rect",
    xref="paper", yref="paper",
    x0=x_base - 0.015,
    x1=x_base + width + 0.15,
    y0=y_base - len(faixas) * (height + spacing) - 0.01,
    y1=y_base + 0.01,
    fillcolor="white",
    line=dict(width=1, color="gray"),
    layer="below"
)

# Adiciona quadrado + texto ao lado
for i, (nome, cor) in enumerate(faixas):
    y0 = y_base - i * (height + spacing)
    y1 = y0 + height
    y_center = (y0 + y1) / 2

    choromap.add_shape(
        type="rect",
        xref="paper", yref="paper",
        x0=x_base,
        x1=x_base + width,
        y0=y0,
        y1=y1,
        fillcolor=cor,
        line=dict(width=0)
    )

    # Texto ao lado, perfeitamente alinhado
    choromap.add_annotation(
        x=x_base + width + 0.01,
        y=y_center,
        xref="paper", yref="paper",
        text=nome,
        showarrow=False,
        font=dict(size=12, color="black"),
        xanchor="left",
        yanchor="middle",
        align="left"
    )


# Exibir o gráfico do mapa
st.plotly_chart(choromap, use_container_width=True)

# Espaçamento
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""Pernambuco e Santa Catarina apresentam realidades bastante distintas em relação à vulnerabilidade social.  
**Santa Catarina possui atualmente o menor IVS do país**, por esse motivo decidimos comparar com Pernambuco, nosso estado.
Através disso, gerar **insights que possam elevar Pernambuco para outro patamar**.
""")


# Botão para ir à próxima página
if st.button("➡️ Comparativo PE x SC"):
    st.switch_page("pages/2_Comparativo.py")


st.markdown("---")
st.markdown("Desenvolvido pela equipe aruera • Projeto CESAR School")