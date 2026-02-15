from sqlalchemy.orm import Session, joinedload
from sqlalchemy import func, text
from models import Transacao, Categoria, Conta
from datetime import date

class TransacaoRepository:
    def __init__(self, db: Session):
        self.db = db

    def criar(self, transacao: Transacao) -> Transacao:
        """Salva uma nova transação no banco."""
        self.db.add(transacao)
        self.db.commit()
        self.db.refresh(transacao)
        return transacao

    def buscar_existente(self, data: date, descricao: str, valor: float) -> Transacao | None:
        """Verifica se uma transação idêntica já existe (para evitar duplicatas)."""
        return self.db.query(Transacao).filter_by(
            data=data, 
            descricao=descricao, 
            valor=valor
        ).first()

    def listar_todas(self):
        """Lista todas as transações, trazendo a categoria junto (Eager Loading)."""
        return self.db.query(Transacao)\
            .options(joinedload(Transacao.categoria))\
            .order_by(Transacao.data)\
            .all()

    def agrupar_por_categoria(self):
        """Retorna o total gasto agrupado por categoria."""
        return self.db.query(
            Categoria.nome, 
            func.sum(Transacao.valor).label("total")
        ).join(Transacao)\
         .group_by(Categoria.nome)\
         .order_by(text("total"))\
         .all()

class ContaRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def obter_conta_padrao(self) -> Conta:
        return self.db.query(Conta).first()

class CategoriaRepository:
    def __init__(self, db: Session):
        self.db = db
    
    def buscar_por_nome(self, nome: str) -> Categoria | None:
        return self.db.query(Categoria).filter_by(nome=nome).first()
    
    def criar(self, categoria: Categoria):
        self.db.add(categoria)
        self.db.commit()