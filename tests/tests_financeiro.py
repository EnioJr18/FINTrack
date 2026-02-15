import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Categoria, Conta, Transacao
from services import FinanceiroService
from datetime import date

# --- Configuração do Banco de Teste (Na Memória RAM) ---
@pytest.fixture
def db_session():
    # Cria um banco SQLite na memória (desaparece ao fim do teste)
    engine = create_engine("sqlite:///:memory:")
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    yield session
    session.close()

# --- O Teste em Si ---
def test_calculo_de_saldo(db_session):
    # 1. Preparação (Arrange)
    service = FinanceiroService(db_session)
    service._garantir_dados_iniciais() # Cria conta e categorias
    
    # Vamos criar dados falsos manualmente para testar a matemática
    conta = db_session.query(Conta).first()
    cat_salario = db_session.query(Categoria).filter_by(nome="Salário").first()
    cat_uber = db_session.query(Categoria).filter_by(nome="Transporte").first()

    # Adiciona R$ 5000 de salário
    t1 = Transacao(data=date.today(), descricao="Salário", valor=5000.0, 
                   categoria_id=cat_salario.id, conta_id=conta.id)
    
    # Adiciona R$ 200 de gasto
    t2 = Transacao(data=date.today(), descricao="Uber", valor=-200.0, 
                   categoria_id=cat_uber.id, conta_id=conta.id)
    
    db_session.add_all([t1, t2])
    db_session.commit()

    # 2. Execução (Act)
    # Pedimos ao service para calcular o extrato
    resultado = service.obter_extrato_completo()
    resumo = resultado["resumo"]

    # 3. Verificação (Assert)
    assert resumo["receitas"] == 5000.0
    assert resumo["despesas"] == -200.0
    assert resumo["saldo"] == 4800.0