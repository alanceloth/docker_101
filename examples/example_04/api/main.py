# api/main.py
from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Float, Date, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
import os
from datetime import date
from pydantic import BaseModel
from typing import List

# Configuração do banco de dados
DATABASE_URL = os.environ.get("DATABASE_URL")
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# Modelo SQLAlchemy
class VendaDB(Base):
    __tablename__ = "vendas"
    
    id = Column(Integer, primary_key=True, index=True)
    data_venda = Column(Date)
    produto = Column(String)
    categoria = Column(String)
    valor = Column(Float)
    quantidade = Column(Integer)

# Modelo Pydantic para leitura
class Venda(BaseModel):
    id: int
    data_venda: date
    produto: str
    categoria: str
    valor: float
    quantidade: int
    
    class Config:
        orm_mode = True

# Modelo Pydantic para criação
class VendaCreate(BaseModel):
    data_venda: date
    produto: str
    categoria: str
    valor: float
    quantidade: int

# Dependência para obter a sessão do banco
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app = FastAPI(title="API de Análise de Dados")

@app.get("/vendas", response_model=List[Venda])
def listar_vendas(db: Session = Depends(get_db)):
    return db.query(VendaDB).all()

@app.get("/vendas/categoria/{categoria}", response_model=List[Venda])
def vendas_por_categoria(categoria: str, db: Session = Depends(get_db)):
    return db.query(VendaDB).filter(VendaDB.categoria == categoria).all()

@app.get("/vendas/analise")
def analise_vendas(db: Session = Depends(get_db)):
    resultado = db.query(
        VendaDB.categoria,
        func.count(VendaDB.id).label("total_vendas"),
        func.sum(VendaDB.valor * VendaDB.quantidade).label("receita_total"),
        func.avg(VendaDB.valor).label("ticket_medio")
    ).group_by(VendaDB.categoria).all()
    
    return [
        {
            "categoria": r.categoria,
            "total_vendas": r.total_vendas,
            "receita_total": float(r.receita_total),
            "ticket_medio": float(r.ticket_medio)
        }
        for r in resultado
    ]

# Endpoint para inserir novos dados - disponível apenas no Docker Compose
@app.post("/vendas", response_model=Venda)
def criar_venda(venda: VendaCreate, db: Session = Depends(get_db)):
    nova_venda = VendaDB(**venda.dict())
    db.add(nova_venda)
    db.commit()
    db.refresh(nova_venda)
    return nova_venda