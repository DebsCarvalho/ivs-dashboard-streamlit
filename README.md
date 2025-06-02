# 📊 IVS Dashboard - Dashboard de Vulnerabilidade Social

Este projeto é um **dashboard interativo** desenvolvido com [Streamlit](https://streamlit.io/) que apresenta uma análise comparativa entre os estados de **Pernambuco (PE)** e **Santa Catarina (SC)** com foco em indicadores sociais como **IVS, IDH, renda, educação, trabalho informal**, entre outros.

---

## 🎯 Objetivo

Explorar dados públicos e destacar **boas práticas de programas sociais**, sugerindo caminhos para o aprimoramento de políticas públicas em Pernambuco, com base no sucesso de iniciativas em Santa Catarina.

---

## 📌 Funcionalidades

- Visualização de **indicadores sociais** com gráficos e mapas dos estados.
- Destaque para **programas sociais** relevantes em PE e SC.
- Comparativo visual e dinâmico de dados.
- **Insights estratégicos** com sugestões de melhorias para PE.
- Interface intuitiva e responsiva via Streamlit.

---

## 🛠️ Tecnologias utilizadas

- Python 3.11+
- Streamlit
- Plotly
- Pandas
- Pillow
- Jupyter (para análise exploratória)
- VSCode

---
🧠 Insights gerados
SC apresenta melhores resultados em quase todos os indicadores analisados.

Ações integradas com universidades e redes locais contribuem para o sucesso dos programas em SC.

Pernambuco pode avançar com articulação institucional, monitoramento de impacto e capacitação comunitária.
---

## 📂 Estrutura de pastas

dashboard_streamlit/
│
├── data/ # Dados CSV, imagens e gráficos
├── pages/ # Páginas do dashboard (multi-page)
├── venv/ # Ambiente virtual (recomendado adicionar no .gitignore)
├── app.py # Arquivo principal do Streamlit
├── requirements.txt # Dependências do projeto
└── README.md # Você está aqui


## 🚀 Como Executar

1. Clone o repositório:
git clone https://github.com/DebsCarvalho/ivs-dashboard-streamlit.git
cd ivs-dashboard-streamlit

2. Crie e ative o ambiente virtual:
python -m venv venv
venv\Scripts\activate

3. Instale as dependências:
pip install -r requirements.txt

4. Execute o Streamlit:
streamlit run app.py
