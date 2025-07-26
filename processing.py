import pandas as pd #type: ignore
from datetime import datetime
from database import SessionLocal
from models import Categoria, Transacao, Conta

MAPA_CATEGORIAS = {
    'IFOOD': 'Alimentação',
    'UBER': 'Transporte',
    'PAGAMENTO SALARIO': 'Salário',
    'PIX RECEBIDO': 'Renda Extra',
    'ALUGUEL': 'Contas da Casa',
    'ENERGIA ELETRICA': 'Contas da Casa',
    'Streaming': 'Assinaturas e Serviços',
    }
CATEGORIA_PADRAO = 'Outros'

def obter_categoria_por_descricao(descricao: str, db_session) -> Categoria:
    """Tenta encontrar uma categoria baseada na descrição da transação."""
    for palavra_chave, nome_categoria in MAPA_CATEGORIAS.items():
        if palavra_chave in descricao.upper():   # Verifica se a palavra-chave já existe no banco
            categoria = db_session.query(Categoria).filter_by(nome=nome_categoria).first()
            if categoria:
                return categoria

    # Se não encontrar nenhuma palavra-chave, usa a categoria padrão "Outros"       
    categoria = db_session.query(Categoria).filter_by(nome=CATEGORIA_PADRAO).first()
    return categoria

def popular_dados_inicias(db_session):
    """Cria categorias e uma conta padrão se o banco estiver vazio."""

    # Se não houver nenhuma categoria, cria as categorias do nosso mapa
    if db_session.query(Categoria).count() == 0:
        print("Banco de Dados vazio. Populando com dados iniciais...")
        nomes_categorias = set(MAPA_CATEGORIAS.values())
        nomes_categorias.add(CATEGORIA_PADRAO)

        for nome_cat in nomes_categorias:
            nova_categoria = Categoria(nome=nome_cat)
            db_session.add(nova_categoria)
        print(f'{len(nomes_categorias)} categorias criadas.')
    # se não houver nenhuma conta, cria uma conta padrão
    if db_session.query(Conta).count() == 0:
        print("Nenhuma conta encontrada. Criando conta padrão...")
        conta_padrao = Conta(nome_banco='Meu Banco', tipo_conta='Conta Corrente Principal')
        db_session.add(conta_padrao)
        print("Conta padrão criada.")
    
    db_session.commit()

def processar_extratos_csv(caminho_arquivo: str):
    """Lê um arquivo CSV, processa e insere as transições no banco de dados"""
    print(f'Iniciando processamento do arquivo: {caminho_arquivo}')

    db = SessionLocal()

    try:
        popular_dados_inicias(db)

        df = pd.read_csv(caminho_arquivo, sep=',')

        conta_padrao = db.query(Conta).first()
        if not conta_padrao:
            raise Exception("Nenhuma conta encontrada no banco de dados")
        
        transacoes_adicionadas = 0
        for _, row in df.iterrows():
            data_trasacao = pd.to_datetime(row['data'], dayfirst=True).date()
            descricao = row['descricao']
            valor = float(row['valor'])

            existe = db.query(Transacao).filter_by(
                data=data_trasacao,
                descricao=descricao,
                valor=valor,
                ).first()
            
            if existe:
                print(f'Skipping: Transação já existe  -> {data_trasacao} | {descricao} | {valor}')
                continue

            categoria = obter_categoria_por_descricao(descricao, db)


            nova_transacao = Transacao(
                data=data_trasacao,
                descricao=descricao,
                valor=valor,
                categoria_id=categoria.id,
                conta_id=conta_padrao.id
                )
            
            db.add(nova_transacao)
            transacoes_adicionadas += 1

        db.commit()
        print(f'Processamento concluído. {transacoes_adicionadas} novas transações adicionadas')

    except FileNotFoundError:
        print(f'Erro: Arquivo {caminho_arquivo} não encontrado.')
    except Exception as e:
        print(f'Ocorreu um erro inesperado: {e}')
        db.rollback()
    finally:
        db.close()