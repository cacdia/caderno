import shutil
import subprocess
from pathlib import Path

import typer
from rich.console import Console
from rich.panel import Panel
from rich.theme import Theme

# Configure Rich Console
custom_theme = Theme(
    {
        "info": "cyan",
        "success": "bold green",
        "warning": "yellow",
        "error": "bold red",
        "command": "bold blue",
    }
)
console = Console(theme=custom_theme)
app = typer.Typer(help="CLI para gerenciamento do projeto Caderno.")


def run_command(command: list[str], description: str, check: bool = True, cwd: Path | None = None):
    """Executa um comando no shell com feedback visual."""
    console.print(f"[info]Executando:[/info] {description}...")
    if cwd:
        console.print(f"[dim]Diretório:[/dim] {cwd}")
    console.print(f"[dim]{' '.join(command)}[/dim]")

    try:
        result = subprocess.run(command, check=check, text=True, capture_output=False, cwd=cwd)
        if result.returncode == 0:
            console.print(f"[success]✓ Sucesso:[/success] {description}")
        else:
            console.print(f"[error]✗ Falha:[/error] {description} (Código {result.returncode})")
            if check:
                raise typer.Exit(code=result.returncode)
    except FileNotFoundError:
        console.print(f"[error]Erro:[/error] Comando não encontrado: {command[0]}")
        raise typer.Exit(code=1) from None
    except Exception as e:
        console.print(f"[error]Erro inesperado:[/error] {e}")
        raise typer.Exit(code=1) from None


@app.command()
def build(
    execute: bool = typer.Option(False, help="Executar notebooks durante o build."),
    all_exports: bool = typer.Option(False, "--all", help="Construir todos os exports."),
    html: bool = typer.Option(False, help="Construir saída HTML estática."),
    site: bool = typer.Option(False, help="Construir site MyST."),
    strict: bool = typer.Option(False, help="Parar o build se houver erros."),
    check_links: bool = typer.Option(False, help="Verificar links quebrados."),
):
    """
    Constrói o projeto MyST (HTML, etc).

    Executa o build dentro do diretório books/ que é a raiz do projeto MyST.
    """
    console.print(Panel.fit("🔨 Construindo o Projeto", style="bold blue"))

    books_dir = Path("books")
    if not books_dir.exists():
        console.print("[error]Erro:[/error] Diretório 'books/' não encontrado.")
        raise typer.Exit(code=1)

    cmd = ["uv", "run", "myst", "build"]

    # Adicionar flags opcionais
    if execute:
        cmd.append("--execute")
    if all_exports:
        cmd.append("--all")
    if html:
        cmd.append("--html")
    if site:
        cmd.append("--site")
    if strict:
        cmd.append("--strict")
    if check_links:
        cmd.append("--check-links")

    # Se nenhuma flag específica for passada, usar comportamento padrão do myst
    # que constrói baseado no myst.yml

    run_command(cmd, "Build do MyST", cwd=books_dir)


@app.command()
def start():
    """
    Inicia o servidor de desenvolvimento local.

    Executa o servidor dentro do diretório books/ que é a raiz do projeto MyST.
    """
    console.print(Panel.fit("🚀 Iniciando Servidor Local", style="bold green"))

    books_dir = Path("books")
    if not books_dir.exists():
        console.print("[error]Erro:[/error] Diretório 'books/' não encontrado.")
        raise typer.Exit(code=1)

    run_command(["uv", "run", "myst", "start"], "Servidor MyST", check=False, cwd=books_dir)


@app.command()
def check(
    fix: bool = typer.Option(
        False, "--fix", help="Tenta corrigir erros automaticamente onde possível."
    ),
):
    """
    Executa verificações de qualidade de código (Linter e Type Checker).
    """
    console.print(Panel.fit("🔍 Verificando Código", style="bold yellow"))

    # Ruff
    ruff_cmd = ["uv", "run", "ruff", "check", "."]
    if fix:
        ruff_cmd.append("--fix")

    console.print("[bold]1. Executando Linter (Ruff)[/bold]")
    run_command(ruff_cmd, "Ruff Check", check=False)

    # Pyrefly
    console.print("\n[bold]2. Executando Type Checker (Pyrefly)[/bold]")
    run_command(["uv", "run", "pyrefly", "check"], "Pyrefly Check", check=False)


@app.command()
def format(
    check_only: bool = typer.Option(
        False, "--check", help="Apenas verifica a formatação sem alterar arquivos."
    ),
):
    """
    Formata o código usando Ruff.
    """
    console.print(Panel.fit("🎨 Formatando Código", style="bold magenta"))

    cmd = ["uv", "run", "ruff", "format", "."]
    if check_only:
        cmd.append("--check")

    run_command(cmd, "Ruff Format")


@app.command()
def clean():
    """
    Limpa artefatos de build.

    Remove o diretório books/_build/ onde o MyST gera os arquivos compilados.
    """
    console.print(Panel.fit("🧹 Limpando Projeto", style="bold red"))

    # Limpar books/_build (raiz do projeto MyST)
    build_dir = Path("books/_build")

    if build_dir.exists():
        try:
            shutil.rmtree(build_dir)
            console.print(f"[success]✓ Removido:[/success] {build_dir}")
        except Exception as e:
            console.print(f"[error]Erro ao remover {build_dir}:[/error] {e}")
    else:
        console.print(f"[dim]Não existe:[/dim] {build_dir}")

    # Também limpar cache do MyST se existir
    myst_cache = Path("books/.myst")
    if myst_cache.exists():
        try:
            shutil.rmtree(myst_cache)
            console.print(f"[success]✓ Removido cache:[/success] {myst_cache}")
        except Exception as e:
            console.print(f"[error]Erro ao remover cache:[/error] {e}")


@app.command()
def info():
    """
    Exibe informações sobre o ambiente.
    """
    console.print(Panel.fit("ℹ️ Informações do Ambiente", style="bold cyan"))
    run_command(["uv", "version"], "Versão do UV", check=False)
    run_command(["python", "--version"], "Versão do Python", check=False)
    run_command(["uv", "run", "myst", "--version"], "Versão do MyST", check=False)


if __name__ == "__main__":
    app()
