import pandas as pd
from sqlalchemy.orm import Session
from models import Transacao, Categoria, Conta
from repositories import TransacaoRepository, CategoriaRepository, ContaRepository
from settings import MAPA_CATEGORIAS, CATEGORIA_PADRAO 

class FinanceiroService:
    def __init__(self, db: Session):
        self.db = db
        self.transacao_repo = TransacaoRepository(db)
        self.categoria_repo = CategoriaRepository(db)
        self.conta_repo = ContaRepository(db)
        
    def _determinar_categoria(self, descricao: str) -> Categoria:
        """Método interno para definir a categoria baseada na descrição."""
        descricao_upper = descricao.upper()
        
        for palavra_chave, nome_categoria in MAPA_CATEGORIAS.items():
            if palavra_chave in descricao_upper:
                categoria = self.categoria_repo.buscar_por_nome(nome_categoria)
                if categoria:
                    return categoria
        
        return self.categoria_repo.buscar_por_nome(CATEGORIA_PADRAO)

    def importar_extrato(self, caminho_arquivo: str):
        """
        Lê um CSV e salva as transações. Retorna estatísticas.
        """
        self._garantir_dados_iniciais()

        try:
            df = pd.read_csv(caminho_arquivo)
        except FileNotFoundError:
            raise FileNotFoundError(f"Arquivo não encontrado: {caminho_arquivo}")

        conta_padrao = self.conta_repo.obter_conta_padrao()
        estatisticas = {"sucesso": 0, "puladas": 0, "erros": 0}

        for _, row in df.iterrows():
            try:
                data = pd.to_datetime(row['data'], dayfirst=True).date()
                desc = row['descricao']
                valor = float(row['valor'])

                if self.transacao_repo.buscar_existente(data, desc, valor):
                    estatisticas["puladas"] += 1
                    continue

                categoria = self._determinar_categoria(desc)
                if not categoria:
                    estatisticas["erros"] += 1
                    continue

                nova_transacao = Transacao(
                    data=data, descricao=desc, valor=valor,
                    categoria_id=categoria.id, conta_id=conta_padrao.id
                )
                self.transacao_repo.criar(nova_transacao)
                estatisticas["sucesso"] += 1

            except Exception as e:
                print(f"Erro ao processar linha: {e}")
                estatisticas["erros"] += 1

        return estatisticas

    def obter_extrato_completo(self):
        """Retorna todas as transações + o cálculo do balanço."""
        transacoes = self.transacao_repo.listar_todas()
        
        total_receitas = sum(t.valor for t in transacoes if t.valor > 0)
        total_despesas = sum(t.valor for t in transacoes if t.valor < 0)
        saldo = total_receitas + total_despesas

        return {
            "transacoes": transacoes,
            "resumo": {
                "receitas": total_receitas,
                "despesas": total_despesas,
                "saldo": saldo
            }
        }

    def obter_gastos_por_categoria(self):
        """Retorna os dados agrupados prontos para exibição."""
        return self.transacao_repo.agrupar_por_categoria()

    def _garantir_dados_iniciais(self):
        """Garante que categorias e conta padrão existam no banco."""
        if self.db.query(Categoria).count() == 0:
            nomes = set(MAPA_CATEGORIAS.values())
            nomes.add(CATEGORIA_PADRAO)
            for nome in nomes:
                self.categoria_repo.criar(Categoria(nome=nome))
        
        if self.db.query(Conta).count() == 0:
            self.db.add(Conta(nome_banco='Banco Padrão', tipo_conta='Corrente'))
            self.db.commit()