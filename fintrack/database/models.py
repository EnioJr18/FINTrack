import datetime
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey # type: ignore
from sqlalchemy.orm import relationship, declarative_base # type: ignore

Base = declarative_base()

class Categoria(Base):
    __tablename__ = 'categorias'
    
    id = Column(Integer, primary_key=True)
    nome = Column(String(50), nullable=False, unique=True)

    transacoes = relationship('Transacao', back_populates='categoria')

    def __repr__(self):
        return f"<Categoria(nome='{self.nome}')>"
    

class Conta(Base):
    __tablename__ = 'contas'
    
    id = Column(Integer, primary_key=True)
    nome_banco = Column(String(100), nullable=False)
    tipo_conta = Column(String(100))

    transacoes = relationship('Transacao', back_populates='conta')

    def __repr__(self):
        return f"<Conta(nome='{self.nome_banco}', tipo='{self.tipo_conta}')>"
    

class Transacao(Base):
    __tablename__ = 'transacoes'

    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False, default=datetime.date.today)
    descricao = Column(String(255), nullable=False)
    valor = Column(Float, nullable=False)

    categoria_id = Column(Integer, ForeignKey('categorias.id'))
    conta_id = Column(Integer, ForeignKey('contas.id'))

    categoria = relationship('Categoria', back_populates='transacoes')
    conta = relationship('Conta', back_populates='transacoes')

    def __repr__(self):
        return f"<Transacao(data='{self.data}', desc='{self.descricao}', valor={self.valor})>"