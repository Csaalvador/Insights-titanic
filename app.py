import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="🚢 Viagem ao Titanic", layout="wide")

# Carregar e tratar os dados
df = pd.read_csv("./titanic/train.csv")

df.rename(columns={
    'PassengerId': 'ID',
    'Survived': 'Sobreviveu',
    'Pclass': 'Classe',
    'Name': 'Nome',
    'Sex': 'Sexo',
    'Age': 'Idade',
    'SibSp': 'Irmãos/Cônjuges',
    'Parch': 'Pais/Filhos',
    'Ticket': 'Bilhete',
    'Fare': 'Tarifa',
    'Cabin': 'Cabine',
    'Embarked': 'Embarque'
}, inplace=True)

df['Idade'].fillna(df['Idade'].median(), inplace=True)
df['Cabine'].fillna('Não informado', inplace=True)
df['Embarque'].fillna('Não informado', inplace=True)
df['Sobreviveu'] = df['Sobreviveu'].map({0: '❌ Não', 1: '✅ Sim'})

# Título com emoji e estilo
st.markdown("Insights sobre o titânic")
st.markdown("---")

# Métricas principais com estilo
col1, col2, col3 = st.columns(3)
col1.metric("Total de Passageiros", len(df))
col2.metric("Sobreviveram", df[df['Sobreviveu'] == '✅ Sim'].shape[0])
col3.metric("Não Sobreviveram", df[df['Sobreviveu'] == '❌ Não'].shape[0])

st.markdown("---")

# Gráficos com design mais chamativo
fig1 = px.histogram(
    df,
    x="Classe",
    color="Sobreviveu",
    barmode="group",
    color_discrete_sequence=["#EF553B", "#00CC96"],
    category_orders={"Classe": [1, 2, 3]},
    title="Sobrevivência por Classe",
    labels={"Classe": "Classe", "count": "Passageiros"}
)

fig2 = px.histogram(
    df,
    x="Sexo",
    color="Sobreviveu",
    barmode="group",
    color_discrete_sequence=["#EF553B", "#00CC96"],
    title="Sobrevivência por Sexo",
    labels={"Sexo": "Sexo", "count": "Quantidade"}
)

fig3 = px.box(
    df,
    x="Sobreviveu",
    y="Tarifa",
    color="Sobreviveu",
    color_discrete_sequence=["#636EFA", "#AB63FA"],
    points="all",
    title="Tarifa vs Sobrevivência",
    labels={"Tarifa": "Valor da Passagem", "Sobreviveu": "Sobreviveu?"}
)

# Exibir gráficos lado a lado
col_g1, col_g2, col_g3 = st.columns(3)
with col_g1:
    st.plotly_chart(fig1, use_container_width=True)
with col_g2:
    st.plotly_chart(fig2, use_container_width=True)
with col_g3:
    st.plotly_chart(fig3, use_container_width=True)

st.markdown("---")

# Tabela de dados
st.header("Detalhes dos Passageiros")
st.markdown("Explore livremente a tabela completa abaixo:")
st.dataframe(df, use_container_width=True)

# Rodapé com conclusões
st.markdown("---")
st.markdown("""
- 🎖️ **Passageiros da 1ª Classe** tinham muito mais chances de sobreviver.
- 👩 **Mulheres** sobreviveram mais que os homens.
- 👶 **Crianças e idosos** tiveram taxas elevadas de salvação.
- ⛴️ Indícios de **privilégios por status social**.
- 💰 Não é possível afirmar suborno, mas a **tarifa mais alta** tende a aparecer entre os sobreviventes.

---
""")

st.markdown("<div style='text-align: center;'>Feito para explorar histórias reais através de dados.</div>", unsafe_allow_html=True)
