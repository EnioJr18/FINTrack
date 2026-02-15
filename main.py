import typer
from rich.console import Console
from rich.table import Table
from rich import box
from rich.panel import Panel
from rich.text import Text

from database import init_db, SessionLocal
from services import FinanceiroService  

app = typer.Typer(help="FINTrack - Gerenciador Financeiro via CLI")
console = Console()

@app.command()
def setup():
    """Inicializa o banco de dados."""
    with console.status("[bold green]Configurando banco..."):
        init_db()
    console.print("[bold green]✔ Sistema pronto![/bold green]")

@app.command()
def importar(arquivo: str = typer.Argument(..., help="Caminho do CSV")):
    """Importa transações de um arquivo CSV."""
    db = SessionLocal()
    service = FinanceiroService(db) 

    try:
        with console.status(f"[bold blue]Lendo {arquivo}..."):
            stats = service.importar_extrato(arquivo)

        console.print(Panel(
            f"[green]Sucesso: {stats['sucesso']}[/green]\n"
            f"[yellow]Duplicadas (Puladas): {stats['puladas']}[/yellow]\n"
            f"[red]Erros: {stats['erros']}[/red]",
            title="Relatório de Importação",
            expand=False
        ))

    except FileNotFoundError:
        console.print(f"[bold red]Erro:[/bold red] O arquivo '{arquivo}' não foi encontrado.")
    except Exception as e:
        console.print(f"[bold red]Erro Crítico:[/bold red] {e}")
    finally:
        db.close()

@app.command()
def extrato():
    """Exibe o extrato e o saldo atual."""
    db = SessionLocal()
    service = FinanceiroService(db)

    dados = service.obter_extrato_completo()
    db.close()

    transacoes = dados["transacoes"]
    resumo = dados["resumo"]

    if not transacoes:
        console.print("[yellow]Nenhuma transação registrada.[/yellow]")
        return

    table = Table(title="Extrato Detalhado", box=box.ROUNDED)
    table.add_column("Data", style="cyan")
    table.add_column("Categoria", style="magenta")
    table.add_column("Descrição", style="white")
    table.add_column("Valor", justify="right")

    for t in transacoes:
        valor_fmt = f"[green]R$ {t.valor:,.2f}[/green]" if t.valor >= 0 else f"[red]R$ {t.valor:,.2f}[/red]"
        table.add_row(t.data.strftime('%d/%m/%Y'), t.categoria.nome, t.descricao, valor_fmt)

    console.print(table)

    cor_saldo = "green" if resumo["saldo"] >= 0 else "red"
    texto_resumo = Text.assemble(
        "\nResumo Financeiro:\n",
        (f"Receitas: R$ {resumo['receitas']:,.2f}\n", "green"),
        (f"Despesas: R$ {resumo['despesas']:,.2f}\n", "red"),
        (f"Saldo:    R$ {resumo['saldo']:,.2f}", f"bold {cor_saldo}")
    )
    console.print(Panel(texto_resumo, title="Balanço", expand=False))

@app.command()
def categorias():
    """Exibe gastos por categoria."""
    db = SessionLocal()
    service = FinanceiroService(db)
    resultados = service.obter_gastos_por_categoria()
    db.close()

    table = Table(title="Análise por Categoria", box=box.SIMPLE)
    table.add_column("Categoria", style="magenta")
    table.add_column("Total", justify="right")

    for nome, total in resultados:
        cor = "green" if total >= 0 else "red"
        table.add_row(nome, f"[{cor}]R$ {total:,.2f}[/{cor}]")

    console.print(table)

if __name__ == "__main__":
    app()