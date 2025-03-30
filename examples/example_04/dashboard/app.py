# dashboard/app.py
import streamlit as st
import pandas as pd
import plotly.express as px
import requests
import os
from datetime import datetime

# Configuração
API_URL = os.environ.get("API_URL", "http://api:8000")

st.set_page_config(
    page_title="Dashboard de Análise de Vendas",
    layout="wide",
    initial_sidebar_state="auto"
)

# Título
st.title("Dashboard de Análise de Vendas")
st.write("Dashboard interativo para análise de dados de vendas")

# Funções para carregar dados da API
@st.cache_data(ttl=300)
def carregar_vendas():
    response = requests.get(f"{API_URL}/vendas")
    return pd.DataFrame(response.json())

@st.cache_data(ttl=300)
def carregar_analise():
    response = requests.get(f"{API_URL}/vendas/analise")
    return pd.DataFrame(response.json())

# Função para inserir novos dados
def inserir_venda(dados):
    response = requests.post(f"{API_URL}/vendas", json=dados)
    return response.status_code == 200 or response.status_code == 201

try:
    # Carregar dados
    df_vendas = carregar_vendas()
    df_analise = carregar_analise()
    
    # Criar abas para separar visualização e entrada de dados
    tab1, tab2 = st.tabs(["Visualização de Dados", "Inserir Novos Dados"])
    
    with tab1:
        # Filtro por categoria (movido da sidebar para a parte superior)
        st.subheader("Filtros")
        categorias = ["Todas"] + sorted(df_vendas["categoria"].unique().tolist())
        categoria_selecionada = st.selectbox("Selecione uma categoria:", categorias)
        
        # Layout em colunas
        col1, col2 = st.columns(2)
        
        # Coluna 1: Gráfico de barras - Receita por categoria
        with col1:
            st.subheader("Receita Total por Categoria")
            fig1 = px.bar(
                df_analise, 
                x="categoria", 
                y="receita_total",
                text_auto=True,
                color="categoria",
                title="Receita Total por Categoria de Produto"
            )
            st.plotly_chart(fig1, use_container_width=True)
        
        # Coluna 2: Gráfico de pizza - Proporção de vendas
        with col2:
            st.subheader("Proporção de Vendas por Categoria")
            fig2 = px.pie(
                df_analise, 
                values="total_vendas", 
                names="categoria",
                title="Distribuição de Vendas por Categoria"
            )
            st.plotly_chart(fig2, use_container_width=True)
        
        # Tabela completa
        st.subheader("Dados de Vendas")
        st.dataframe(df_vendas)
        
        # Exibição dos dados filtrados (movido da sidebar)
        if categoria_selecionada != "Todas":
            df_filtrado = df_vendas[df_vendas["categoria"] == categoria_selecionada]
            st.subheader(f"Vendas na categoria: {categoria_selecionada}")
            st.dataframe(df_filtrado)
            
            # Gráfico de linha para a categoria
            if not df_filtrado.empty:
                df_por_data = df_filtrado.groupby("data_venda").agg(
                    {"valor": lambda x: (x * df_filtrado["quantidade"]).sum()}
                ).reset_index()
                df_por_data.columns = ["data", "receita"]
                
                fig3 = px.line(
                    df_por_data, 
                    x="data", 
                    y="receita",
                    markers=True,
                    title=f"Evolução de Receita: {categoria_selecionada}"
                )
                st.plotly_chart(fig3, use_container_width=True)
    
    with tab2:
        # Formulário para adicionar novas vendas
        st.subheader("Adicionar Nova Venda")
        with st.form("nova_venda_form"):
            data_venda = st.date_input("Data da Venda", datetime.now().date())
            produto = st.text_input("Nome do Produto")
            
            # Usar categorias existentes ou permitir nova
            usar_categoria_existente = st.checkbox("Usar categoria existente", value=True)
            if usar_categoria_existente and not df_vendas.empty:
                categoria = st.selectbox("Categoria", sorted(df_vendas["categoria"].unique().tolist()))
            else:
                categoria = st.text_input("Nova Categoria")
                
            valor = st.number_input("Valor Unitário (R$)", min_value=0.01, format="%.2f")
            quantidade = st.number_input("Quantidade", min_value=1, step=1)
            
            submitted = st.form_submit_button("Adicionar Venda")
            
            if submitted:
                if not produto or not categoria:
                    st.error("Todos os campos são obrigatórios!")
                else:
                    nova_venda = {
                        "data_venda": data_venda.isoformat(),
                        "produto": produto,
                        "categoria": categoria,
                        "valor": valor,
                        "quantidade": quantidade
                    }
                    
                    if inserir_venda(nova_venda):
                        st.success("Venda adicionada com sucesso!")
                        # Limpar cache para atualizar os dados
                        st.cache_data.clear()
                        # Adicionar rerun para forçar a atualização da página
                        st.rerun()
                    else:
                        st.error("Erro ao adicionar venda. Verifique os dados e tente novamente.")
    
except Exception as e:
    st.error(f"Erro ao carregar dados: {e}")
    st.warning("Verifique se a API está disponível e funcionando corretamente.")