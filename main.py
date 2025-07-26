import os
import platform
import time
from database import init_db
from processing import processar_extratos_csv
from reports import gerar_relatorio_geral, gerar_relatorio_por_categoria
from automation import automatizador

ARQUIVO_EXEMPLO = "extrato_exemplo.csv"

def limpar_tela():
    """Limpa a tela do terminal para uma melhor visualização."""
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')

#def criar_csv_exemplo():
    #""Cria um arquivo CSV de exemplo se ele não existir.""
    #if not os.path.exists(ARQUIVO_EXEMPLO):
    #    print(f"Arquivo de exemplo '{ARQUIVO_EXEMPLO}' não encontrado. Criando um novo...")
    #    conteudo_csv = (
    #        "data,descricao,valor\n"
    #        "20/07/2025,PAGAMENTO SALARIO JULHO,4500.00\n"
    #        "20/07/2025,PIX PAGO - CONTA DE LUZ,-250.00\n"
    #        "21/07/2025,COMPRA IFOOD,-55.90\n"
    #        "21/07/2025,UBER VIAGEM,-15.75\n"
    #        "22/07/2025,PAGAMENTO NETFLIX,-39.90\n"
    #        "22/07/2025,PAGAMENTO ALUGUEL,-1200.00\n"
    #        "23/07/2025,COMPRA IFOOD,-32.50\n"
    #        "25/07/2025,COMPRA MERCADO,-200.00\n"
    #        "25/07/2025,PIX RECEBIDO - CLIENTE A,3000.00\n"
    #    )
    #    with open(ARQUIVO_EXEMPLO, 'w', newline='', encoding='utf-8') as f:
    #        f.write(conteudo_csv)
    #    print("Arquivo de exemplo criado com sucesso.")

if __name__ == "__main__":
    limpar_tela()
    time.sleep(3.5)

    print("==============================================")
    print("    INICIANDO O ASSISTENTE FINTRACK V1.0    ")
    print("==============================================")

    init_db()
    time.sleep(2)
    #criar_csv_exemplo()
    #time.sleep(2)
    
    print("\n[ETAPA 1/2] Processando extratos...")
    time.sleep(2)
    processar_extratos_csv(caminho_arquivo=ARQUIVO_EXEMPLO)
    time.sleep(1.5)
    print("[ETAPA 1/2] Processamento concluído.")
    time.sleep(2.5)
    
    print("\n[ETAPA 2/2] Gerando relatórios...")
    time.sleep(2)
    gerar_relatorio_geral()
    time.sleep(2)
    gerar_relatorio_por_categoria()
    time.sleep(2.5)
    print("[ETAPA 2/2] Relatórios gerados.")
    time.sleep(1)

    print("\n==============================================")
    print("           PROGRAMA FINALIZADO            ")
    print("==============================================")