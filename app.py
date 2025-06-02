import streamlit as st

st.set_page_config(
    page_title="Dashboard de Vulnerabilidade Social",
    page_icon="📊",
    layout="wide"
)

# Exibe a imagem como fundo (com largura total da tela)
st.image("data/Vulnerabilidade_Social.jpg", use_container_width=True)

# Estilo grifado do texto
st.markdown("""
    <style>
        .highlight-box {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 10px;
            margin-top: -1320px;
            margin-bottom: 2rem;
            width: 70%;
            margin-left: auto;
            margin-right: auto;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.2);
            color: #000000;
        }
        .highlight-box h1, .highlight-box h3, .highlight-box p {
            color: #00000;
        }
    </style>
""", unsafe_allow_html=True)

# Bloco com o texto sobreposto
st.markdown("""
    <div class='highlight-box'>
        <h1>Bem-vindo ao Dashboard de Vulnerabilidade Social</h1>
        <h3>O que é o IVS?</h3>
        <p>O <strong>Índice de Vulnerabilidade Social (IVS)</strong> é uma métrica que avalia a qualidade de vida da população, com base em:</p>
        <ul>
            <li>Acesso à educação</li>
            <li>Renda e trabalho</li>
            <li>Condições de moradia</li>
            <li>Inclusão social</li>
        </ul>
        <p>Quanto mais próximo de <strong>1</strong>, maior a vulnerabilidade social de uma região.</p>
    </div>
""", unsafe_allow_html=True)

# Botão para ir à próxima página
if st.button("➡️ Conheça melhor os dados de Vulnerabilidade do Brasil"):
    st.switch_page("pages/1_Home.py")
