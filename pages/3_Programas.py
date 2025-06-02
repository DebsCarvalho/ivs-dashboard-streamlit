import streamlit as st
st.set_page_config(page_title="Programas Sociais por Estado", layout="wide")
from streamlit_card import card
import pandas as pd
import plotly.express as px

# Carregamento dos dados
@st.cache_data
def carregar_dados():
    df = pd.read_csv('data/full_data.csv', encoding='latin1')
    df.columns = df.columns.str.strip()
    df = df.iloc[1:]
    return df

df = carregar_dados()

# Título e introdução
st.title("📌 Programas Sociais em Destaque")
st.markdown("### Compare iniciativas de Pernambuco e Santa Catarina")
st.markdown("Clique em cada programa para ver os detalhes.")

st.markdown("<br>", unsafe_allow_html=True)

# ---------------------- Programas PE ----------------------
st.markdown("### Programas em Pernambuco")

with st.expander("🌟 Programa Mãe Coruja Pernambucana"):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("data/mae_coruja_pe.png", width=300)
    with col2:
        st.markdown("""
        **Objetivo:** Reduzir a mortalidade infantil e acompanhar gestantes.  
        **Público-Alvo:** Gestantes e crianças (0 a 5 anos).  
        **Impacto:** +360 mil gestantes atendidas.
        """)

with st.expander("🌾 Chapéu de Palha"):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("data/chapeu_de_palha.jpg", width=300)
    with col2:
        st.markdown("""
        **Objetivo:** Garantir renda para trabalhadores rurais fora de safra.  
        **Público-Alvo:** Agricultores familiares e trabalhadores sazonais.  
        **Impacto:** Benefícios pagos a milhares de famílias anualmente.  
        """)

with st.expander("🏠 Programa Morar Bem Pernambuco"):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("data/morar_bem_pe.png", width=300)
    with col2:
        st.markdown("""
        **Objetivo:** Garantir moradia digna para famílias de baixa renda.  
        **Público-Alvo:** Famílias em áreas de risco ou sem titulação de propriedade.   
        **Impacto:**  Redução do déficit habitacional e Melhoria da qualidade de vida.

        **Ações Desenvolvidas:**  
        - Construção de unidades habitacionais  
        - Regularização fundiária  
        - Urbanização de comunidades 
        """)

# ---------------------- Programas SC ----------------------
st.markdown("### Programas em Santa Catarina")

with st.expander("🍲 Cozinhas Comunitárias"):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("data/cozinha_comunitaria_sc.jpg", width=300)
    with col2:
        st.markdown("""
        **Objetivo:** Fornecer alimentação a população em situação de vulnerabilidade.  
        **Público-Alvo:** Famílias de baixa renda e moradores de rua.  
        **Impacto:** +200 mil refeições servidas por mês.
        """)

with st.expander("🏠 Programa de Moradia Popular"):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("data/moradia_sc.jpeg", width=300)
    with col2:
        st.markdown("""
        **Objetivo:** Construção e reforma de unidades habitacionais.  
        **Público-Alvo:** Famílias em vulnerabilidade social.  
        **Impacto:** Milhares de casas entregues desde 2018.
        """)

with st.expander("🎓 Projetos de Extensão Universitária em SC"):
    col1, col2 = st.columns([1, 2])
    with col1:
        st.image("data/programas_universitarios_sc.jpg", width=300)
    with col2:
        st.markdown("""
        **Objetivo:** Promover inclusão social, educação cidadã e desenvolvimento regional.  
        **Instituições Envolvidas:** UFSC, UDESC, IFSC e outras.  
        **Público-Alvo:** Comunidades urbanas e rurais em vulnerabilidade social.  
        **Impacto:**
        - +2.000 ações de extensão só pela UFSC em 2020  
        - +453 mil pessoas atendidas  
        - Cursos, oficinas, hortas comunitárias, saúde, educação ambiental, inclusão digital  
        """)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("#### Conheça mais a fundo os programas sociais de cada Estado e seus impactos:")

# URL dos arquivos no Google Drive
url_pernambuco = "https://drive.google.com/file/d/1NwIz9Jugut33nDZyOJkKqs-878Pz2XSv/view?usp=drive_link"
url_santa_catarina = "https://docs.google.com/document/d/1YBsiwEOTeUsDcaGUEQMHwn4SJIMLau6B4QKCPnrZTlo/edit?usp=sharing"

# Botão de link externo para Pernambuco
if st.button("Programas Sociais Pernambuco"):
    st.markdown(f"Visualize [aqui]({url_pernambuco}).")

# Botão de link externo para Santa Catarina
if st.button("Programas Sociais Santa Catarina"):
    st.markdown(f"Visualize [aqui]({url_santa_catarina}).")


st.markdown("<br>", unsafe_allow_html=True)

st.markdown("## 📌 Insights Estratégicos para Pernambuco")

st.markdown("""
Apesar dos esforços em Pernambuco, Santa Catarina se destaca por estratégias mais integradas e sustentáveis. 
A seguir, destacamos os principais diferenciais de SC com propostas práticas de aplicação em PE.
""")

# Cores da paleta Viridis escolhidas
viridis_colors = ["#440154", "#443983", "#31688E", "#35B779"]

card_style_base = {
    "background-color": "",
    "color": "white",
    "padding": "1.5rem",
    "width": "100%",
    "min-height": "280px",
    "font-size": "1.1rem",
    "border-radius": "12px",
    "box-shadow": "0 4px 12px rgba(0, 0, 0, 0.2)"
}

col1, col2 = st.columns(2)

with col1:
    card(
        title="🤝 Integração Institucional",
        text="✅ SC integra universidades e governo.\n\n📌 PE pode estimular convênios com UFPE, UFRPE, IFPE e UPE para projetos sociais contínuos.",
        styles={"card": {**card_style_base, "background-color": viridis_colors[0]}}
    )
    card(
        title="🚀 Foco em Autonomia",
        text="✅ SC promove empreendedorismo e capacitação.\n\n📌 PE deve ampliar programas de qualificação profissional e incentivo ao microcrédito.",
        styles={"card": {**card_style_base, "background-color": viridis_colors[1]}}
    )

with col2:
    card(
        title="🌱 Multiplicadores de Impacto",
        text="✅ SC prefeituras e estudantes como agentes disseminadores.\n\n📌 PE precisa ampliar suas redes locais de impacto social.",
        styles={"card": {**card_style_base, "background-color": viridis_colors[2]}}
    )
    card(
        title="🛰️ Cobertura Estadual",
        text="✅ SC tem dados e cobertura ampla.\n\n📌 PE precisa investir em monitoramento.",
        styles={"card": {**card_style_base, "background-color": viridis_colors[3]}}
    )


st.markdown("<br>", unsafe_allow_html=True)

# Rodapé
st.markdown("---")
st.markdown("Desenvolvido pela equipe aruera • Projeto CESAR School")