# app.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Configuração da página
st.set_page_config(page_title="Dashboard de Vendas", layout="wide")

# Título
st.title("Dashboard de Vendas - 2025")

# Carregar dados de exemplo
@st.cache_data
def load_data():
    # NOTA: No exemplo isolado, usamos dados estáticos
    # No exemplo do Docker Compose, estes dados virão da API
    data = {
        'Mês': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun'],
        'Vendas': [15000, 17500, 19800, 22300, 21500, 25000]
    }
    return pd.DataFrame(data)

df = load_data()

# Mostrar dados
st.subheader("Dados de Vendas")
st.dataframe(df)

# Visualização
st.subheader("Tendência de Vendas")
fig, ax = plt.subplots(figsize=(10, 4))
ax.plot(df['Mês'], df['Vendas'], marker='o')
ax.set_ylabel('Vendas (R$)')
ax.grid(True)
st.pyplot(fig)

# Métricas
st.subheader("Métricas")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Total de Vendas", f"R$ {df['Vendas'].sum():,.2f}")
with col2:
    st.metric("Média Mensal", f"R$ {df['Vendas'].mean():,.2f}")
with col3:
    st.metric("Crescimento", f"{((df['Vendas'].iloc[-1] / df['Vendas'].iloc[0]) - 1) * 100:.1f}%")