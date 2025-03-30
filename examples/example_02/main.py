# main.py
from fastapi import FastAPI, Query
from pydantic import BaseModel
from typing import List, Optional
import pandas as pd

app = FastAPI(title="API de Dados de Vendas")

# Dados simulados - no exemplo isolado, usamos estes dados
# No exemplo do Docker Compose, estes dados viriam do banco PostgreSQL
vendas_df = pd.DataFrame({
    'id': range(1, 11),
    'produto': ['Laptop', 'Mouse', 'Teclado', 'Monitor', 'Headphone', 
                'Webcam', 'SSD', 'RAM', 'GPU', 'CPU'],
    'categoria': ['Computadores', 'Acessórios', 'Acessórios', 'Periféricos', 'Áudio',
                 'Periféricos', 'Componentes', 'Componentes', 'Componentes', 'Componentes'],
    'preco': [3500, 150, 200, 1200, 350, 180, 450, 300, 2000, 1500],
    'quantidade_vendida': [12, 85, 63, 35, 42, 30, 55, 70, 22, 25]
})

class Produto(BaseModel):
    id: int
    produto: str
    categoria: str
    preco: float
    quantidade_vendida: int

class ProdutoCreate(BaseModel):
    produto: str
    categoria: str
    preco: float
    quantidade_vendida: int

@app.get("/")
def read_root():
    return {"mensagem": "API de Dados de Vendas"}

@app.get("/produtos", response_model=List[Produto])
def get_produtos(
    categoria: Optional[str] = Query(None, description="Filtrar por categoria"),
    min_preco: Optional[float] = Query(None, description="Preço mínimo"),
    max_preco: Optional[float] = Query(None, description="Preço máximo")
):
    df = vendas_df.copy()
    
    if categoria:
        df = df[df['categoria'] == categoria]
    
    if min_preco is not None:
        df = df[df['preco'] >= min_preco]
    
    if max_preco is not None:
        df = df[df['preco'] <= max_preco]
    
    return df.to_dict(orient='records')

@app.get("/produtos/{produto_id}", response_model=Produto)
def get_produto(produto_id: int):
    produto = vendas_df[vendas_df['id'] == produto_id]
    if not produto.empty:
        return produto.iloc[0].to_dict()
    return {"erro": "Produto não encontrado"}

# Endpoint para inserir novos dados - disponível apenas no Docker Compose
@app.post("/produtos", response_model=Produto)
def create_produto(produto: ProdutoCreate):
    # No exemplo do Docker Compose, este método salvaria no PostgreSQL
    global vendas_df
    
    novo_id = vendas_df['id'].max() + 1 if not vendas_df.empty else 1
    novo_produto = {
        'id': novo_id,
        **produto.dict()
    }
    
    vendas_df = pd.concat([vendas_df, pd.DataFrame([novo_produto])])
    return novo_produto