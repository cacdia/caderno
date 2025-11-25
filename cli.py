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
docker_app = typer.Typer(help="Gerenciamento do ambiente Docker (substitui Makefile).")
app.add_typer(docker_app, name="docker")


def run_command(command: list[str], description: str, check: bool = True, cwd: Path | None = None):
    """Executa um comando no shell com feedback visual."""
    console.print(f"[info]Executando:[/info] {description}...")
    if cwd:
        console.print(f"[dim]Diretório:[/dim] {cwd}")
    console.print(f"[dim]{' '.join(command)}[/dim]")

    try:
        # Tenta usar 'docker compose' (v2), se falhar tenta 'docker-compose' (v1)
        if command[0] == "docker" and command[1] == "compose":
            try:
                result = subprocess.run(
                    command, check=check, text=True, capture_output=False, cwd=cwd
                )
            except FileNotFoundError:
                # Fallback para docker-compose
                new_command = ["docker-compose"] + command[2:]
                console.print(
                    "[warning]docker compose não encontrado, tentando docker-compose...[/warning]"
                )
                result = subprocess.run(
                    new_command, check=check, text=True, capture_output=False, cwd=cwd
                )
        else:
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


# --- Comandos Locais (uv/myst) ---


@app.command()
def build(
    execute: bool = typer.Option(False, help="Executar notebooks durante o build."),
    all_exports: bool = typer.Option(False, "--all", help="Construir todos os exports."),
    html: bool = typer.Option(False, help="Construir saída HTML estática."),
    site: bool = typer.Option(False, help="Construir site MyST."),
    typst: bool = typer.Option(False, help="Construir saída PDF via Typst."),
    strict: bool = typer.Option(False, help="Parar o build se houver erros."),
    check_links: bool = typer.Option(False, help="Verificar links quebrados."),
):
    """
    Constrói o projeto MyST localmente (usando uv).
    """
    console.print(Panel.fit("🔨 Construindo o Projeto (Local)", style="bold blue"))

    books_dir = Path("books")
    if not books_dir.exists():
        console.print("[error]Erro:[/error] Diretório 'books/' não encontrado.")
        raise typer.Exit(code=1)

    cmd = ["uv", "run", "myst", "build"]

    if execute:
        cmd.append("--execute")
    if all_exports:
        cmd.append("--all")
    if html:
        cmd.append("--html")
    if site:
        cmd.append("--site")
    if typst:
        cmd.append("--typst")
    if strict:
        cmd.append("--strict")
    if check_links:
        cmd.append("--check-links")

    run_command(cmd, "Build do MyST", cwd=books_dir)


@app.command()
def start():
    """Inicia o servidor de desenvolvimento local."""
    console.print(Panel.fit("🚀 Iniciando Servidor Local", style="bold green"))
    books_dir = Path("books")
    run_command(["uv", "run", "myst", "start"], "Servidor MyST", check=False, cwd=books_dir)


@app.command()
def check(fix: bool = typer.Option(False, "--fix", help="Corrigir erros automaticamente.")):
    """Executa verificações de qualidade (Ruff, Pyrefly)."""
    console.print(Panel.fit("🔍 Verificando Código", style="bold yellow"))

    ruff_cmd = ["uv", "run", "ruff", "check", "."]
    if fix:
        ruff_cmd.append("--fix")

    console.print("[bold]1. Linter (Ruff)[/bold]")
    run_command(ruff_cmd, "Ruff Check", check=False)

    console.print("\n[bold]2. Type Checker (Pyrefly)[/bold]")
    run_command(["uv", "run", "pyrefly", "check"], "Pyrefly Check", check=False)


@app.command()
def format(check_only: bool = typer.Option(False, "--check", help="Apenas verificar.")):
    """Formata o código usando Ruff."""
    console.print(Panel.fit("🎨 Formatando Código", style="bold magenta"))
    cmd = ["uv", "run", "ruff", "format", "."]
    if check_only:
        cmd.append("--check")
    run_command(cmd, "Ruff Format")


@app.command()
def clean():
    """Limpa artefatos de build locais."""
    console.print(Panel.fit("🧹 Limpando Projeto Local", style="bold red"))
    for path in [Path("books/_build"), Path("books/.myst")]:
        if path.exists():
            try:
                shutil.rmtree(path)
                console.print(f"[success]✓ Removido:[/success] {path}")
            except Exception as e:
                console.print(f"[error]Erro ao remover {path}:[/error] {e}")


@app.command()
def info():
    """Exibe informações do ambiente."""
    console.print(Panel.fit("ℹ️ Informações do Ambiente", style="bold cyan"))
    run_command(["uv", "version"], "Versão do UV", check=False)
    run_command(["python", "--version"], "Versão do Python", check=False)
    try:
        run_command(["uv", "run", "myst", "--version"], "Versão do MyST", check=False)
    except Exception as e:
        console.print(f"[warning]MyST não encontrado via uv:[/warning] {e}")


# --- Comandos Docker ---


@docker_app.command("build")
def docker_build_image():
    """Constrói a imagem Docker do projeto."""
    console.print(Panel.fit("🐳 Construindo Imagem Docker", style="bold blue"))
    run_command(["docker", "build", "-t", "caderno-myst:latest", "."], "Docker Build")


@docker_app.command("up")
def docker_up():
    """Inicia o servidor de desenvolvimento no Docker (porta 3000)."""
    console.print(Panel.fit("🚀 Iniciando Servidor Docker", style="bold green"))
    run_command(["docker", "compose", "up", "myst-dev"], "Docker Compose Up", check=False)


@docker_app.command("shell")
def docker_shell():
    """Abre um shell interativo no container."""
    console.print(Panel.fit("🐚 Shell Interativo", style="bold magenta"))
    run_command(["docker", "compose", "run", "--rm", "myst-shell"], "Docker Shell", check=False)


@docker_app.command("typst")
def docker_typst(
    springer: bool = typer.Option(False, "--springer", help="Compilar apenas o exemplo Springer."),
    html: bool = typer.Option(False, "--html", help="Também gerar HTML."),
):
    """Compila o projeto usando Typst via Docker."""
    console.print(Panel.fit("📝 Compilando com Typst (Docker)", style="bold yellow"))

    cmd = ["myst", "build", "--typst"]
    if springer:
        cmd = ["myst", "build", "books/guia-myst/exemplo-springer.md", "--typst"]

    if html:
        cmd.append("--html")

    full_cmd = ["docker", "compose", "run", "--rm", "myst-build"] + cmd
    run_command(full_cmd, "Docker Typst Build")


@docker_app.command(
    "run", context_settings={"allow_extra_args": True, "ignore_unknown_options": True}
)
def docker_run(ctx: typer.Context):
    """
    Executa um comando arbitrário no container.
    Exemplo: python cli.py docker run myst build --pdf
    """
    cmd_args = ctx.args
    if not cmd_args:
        console.print("[warning]Nenhum comando fornecido.[/warning]")
        console.print("Exemplo: [bold]python cli.py docker run myst build --typst[/bold]")
        return

    console.print(Panel.fit(f"🏃 Executando no Docker: {' '.join(cmd_args)}", style="bold cyan"))
    full_cmd = ["docker", "compose", "run", "--rm", "myst-build"] + cmd_args
    run_command(full_cmd, "Docker Run", check=False)


@docker_app.command("clean")
def docker_clean():
    """Limpa containers e volumes do Docker."""
    console.print(Panel.fit("🧹 Limpando Docker", style="bold red"))
    run_command(["docker", "compose", "down", "-v"], "Docker Compose Down")


if __name__ == "__main__":
    app()
