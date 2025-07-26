# /fintrack/reports.py

from sqlalchemy import func, text  #type: ignore
from database import SessionLocal
from models import Transacao, Categoria

def gerar_relatorio_geral():
    """Busca e exibe todas as transações cadastradas, formatando a saída."""
    db = SessionLocal()
    try:
        print("\n--- Relatório Geral de Transações ---")
        
        transacoes = db.query(Transacao).join(Categoria).order_by(Transacao.data).all()
        
        if not transacoes:
            print("Nenhuma transação encontrada.")
            return

        for t in transacoes:
            data_formatada = t.data.strftime('%d/%m/%Y')
            valor_formatado = f"R$ {t.valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            tipo = "Receita" if t.valor > 0 else "Despesa"
            
            print(f"Data: {data_formatada} | Categoria: {t.categoria.nome:<20} | Tipo: {tipo:<7} | Valor: {valor_formatado:<15} | Descrição: {t.descricao}")
            
    finally:
        db.close()

def gerar_relatorio_por_categoria():
    """Agrupa os gastos por categoria e mostra o total de cada uma."""
    db = SessionLocal()
    try:
        print("\n--- Relatório de Gastos por Categoria ---")
        
        resultado = db.query(
            Categoria.nome,
            func.sum(Transacao.valor).label('total_gasto')
        ).join(Transacao, Transacao.categoria_id == Categoria.id)\
         .filter(Transacao.valor < 0)\
         .group_by(Categoria.nome)\
         .order_by(text('total_gasto'))\
         .all() 

        if not resultado:
            print("Nenhuma despesa encontrada para gerar o relatório.")
            return

        for nome_categoria, total_gasto in resultado:
            valor_formatado = f"R$ {total_gasto:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
            print(f"Categoria: {nome_categoria:<25} | Total Gasto: {valor_formatado}")

    finally:
        db.close()