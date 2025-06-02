import streamlit as st
import pandas as pd
from PIL import Image

st.set_page_config(page_title="Pernambuco x Santa Catarina", layout="centered")

# Carrega os dados
df = pd.read_csv("data/PExSC.csv")
df.columns = df.columns.str.strip()
df["Estado"] = df["Estado"].str.title().str.strip()

# Dados de cada estado
pe = df[df["UF"] == "PE"].iloc[0]
sc = df[df["UF"] == "SC"].iloc[0]

# Lista de indicadores
indicadores_info = {
    "IVS": "#440154",
    "Renda per capita 2021": "#482475",
    "% Trabalho Informal 2024": "#3B528B",
    "Taxa de analfabetismo (18+) 2021": "#21908C",
    "IDH 2021": "#5DC863",
    "IDH Renda 2021": "#AADC32",
    "IDH Educação 2021": "#DCE319",
}

# CSS dos cartões
st.markdown("""
<style>
.card {
    padding: 10px 18px;
    border-radius: 10px;
    margin-bottom: 10px;
    font-size: 15px;
    font-weight: 500;
    background-color: #1f1f2e;
    box-shadow: 0 0 4px rgba(255,255,255,0.05);
}
</style>
""", unsafe_allow_html=True)

# Função de formatação
def formatar_valor(indicador, valor):
    if "Renda" in indicador:
        return f"R$ {valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    elif "%" in indicador or "analfabetismo" in indicador:
        return f"{valor}%"
    else:
        return f"{valor}"

# Layout com colunas
col1, _, col2 = st.columns([1.4, 0.2, 1.4])

# Imagens
img_pe = Image.open("data/mapPE.png")
img_sc = Image.open("data/mapSC.png")

# Função para exibir os dados
def mostrar_indicadores(estado, dados, imagem, tamanho_img):
    st.image(imagem, width=tamanho_img, caption=estado)
    for indicador, cor in indicadores_info.items():
        valor = formatar_valor(indicador, dados[indicador])
        st.markdown(
            f"""<div class='card' style='border-left: 5px solid {cor};'>
                <b>{indicador}:</b> {valor}
            </div>""",
            unsafe_allow_html=True
        )

with col1:
    mostrar_indicadores("Pernambuco", pe, img_pe, 350)

with col2:
    mostrar_indicadores("Santa Catarina", sc, img_sc, 220)


# Separador
st.markdown("---")

# Seção explicativa
with st.expander("O que é o IDH? Clique para entender"):
    st.markdown("""
    O **IDH (Índice de Desenvolvimento Humano)** é um indicador que avalia o bem-estar da população com base em três pilares:

    - 📘 **Educação** (acesso e escolaridade)  
    - ❤️ **Longevidade** (esperança de vida ao nascer)  
    - 💰 **Renda** (PIB per capita ajustado)

    Os valores do IDH variam entre **0 e 1**, sendo que **quanto mais próximo de 1, melhor o desenvolvimento humano** da região.
    """)


# Espaçamento
st.markdown("<br>", unsafe_allow_html=True)

# Botão de navegação
if st.button("➡️ Conheça melhor os Projetos Sociais de cada Estado"):
    st.switch_page("pages/3_Programas.py")

# Rodapé
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("Desenvolvido pela equipe aruera • Projeto CESAR School")

