"""CLI 도구 메인 모듈."""

import shutil
from pathlib import Path
from typing import TYPE_CHECKING

import click
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from . import SUPPORTED_TEMPLATES, __version__
from .generators import GeneratorFactory
from .i18n import Language, set_language, t
from .readme_generator import generate_readme_files

if TYPE_CHECKING:
    from .generators.base import BaseGenerator

console = Console()


def language_callback(ctx: click.Context, param: click.Parameter, value: str) -> str:
    """언어 콜백 함수."""
    if value:
        try:
            lang = Language(value)
            set_language(lang)
        except ValueError:
            click.echo(f"Unsupported language: {value}")
            ctx.exit(1)
    return value


@click.group(invoke_without_command=True)
@click.option(
    "--language",
    "-l",
    type=click.Choice(["ko", "en"]),
    default="ko",
    callback=language_callback,
    expose_value=False,
    is_eager=True,
    help="Language to use (ko: Korean, en: English)",
)
@click.option("--version", is_flag=True, help="Show version information")
@click.pass_context
def main(ctx: click.Context, version: bool) -> None:
    """Litestar project boilerplate generator."""
    if version:
        click.echo(f"litestar-boilerplate {__version__}")
        return

    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())


@main.command()
@click.option("--type", "template_type", type=click.Choice(SUPPORTED_TEMPLATES), required=True, help="Template type to use")
@click.option("--name", "project_name", required=True, help="Project name")
@click.option("--output", "output_dir", type=click.Path(), default=".", help="Output directory (default: current directory)")
@click.option("--force", is_flag=True, help="Force creation even if directory exists")
def create(template_type: str, project_name: str, output_dir: str, force: bool) -> None:
    """Create a new Litestar project."""
    output_path = Path(output_dir) / project_name

    if output_path.exists() and not force:
        console.print(f"[red]{t('messages.directory_exists')}[/red] '{output_path}'")
        console.print(t("messages.use_force"))
        raise click.Abort()

    if output_path.exists() and force:
        console.print(f"[yellow]Warning:[/yellow] Removing existing directory '{output_path}'")
        shutil.rmtree(output_path)

    console.print(f"[blue]{t('messages.creating_project')}[/blue] '{project_name}' with {template_type} template")

    try:
        generator: BaseGenerator = GeneratorFactory.create(template_type)
        generator.generate(project_name, output_path)

        console.print(f"[green]{t('messages.project_created')}[/green] at '{output_path}'")

        # 다국어 지원 다음 단계 안내
        console.print(f"\n[bold]{t('messages.next_steps')}:[/bold]")
        console.print(f"1. cd {project_name}")
        console.print("2. python -m venv venv")
        console.print("3. source venv/bin/activate  # Linux/Mac")
        console.print(f"4. {t('messages.install_deps')}")
        console.print(f"5. {t('messages.setup_env')}")
        console.print(f"6. {t('messages.run_migrations')}")
        console.print(f"7. {t('messages.start_server')}")

    except Exception as e:
        console.print(f"[red]Error:[/red] {e}")
        raise click.Abort() from e


@main.command("list-templates")
def list_templates() -> None:
    """List available templates."""
    table = Table(title=t("templates.available_templates"))

    table.add_column(t("templates.name"), style="cyan", no_wrap=True)
    table.add_column(t("templates.description"), style="magenta")
    table.add_column(t("templates.features"), style="green")

    templates = [
        ("layered", t("templates.layered.description"), ", ".join(t("templates.layered.features")[:2])),
        ("ddd-lite", t("templates.ddd-lite.description"), ", ".join(t("templates.ddd-lite.features")[:2])),
        ("feature-based", t("templates.feature-based.description"), ", ".join(t("templates.feature-based.features")[:2])),
    ]

    for template, desc, features in templates:
        table.add_row(template, desc, features)

    console.print(table)


@main.command()
@click.argument("template_name", type=click.Choice(SUPPORTED_TEMPLATES), required=False)
def info(template_name: str | None = None) -> None:
    """Show detailed information about templates."""
    if template_name:
        _show_template_info(template_name)
    else:
        _show_all_templates_info()


@main.command("generate-readme")
@click.option("--output", "output_dir", type=click.Path(), default=".", help="Output directory (default: current directory)")
def generate_readme(output_dir: str) -> None:
    """Generate README files in multiple languages."""
    output_path = Path(output_dir)

    try:
        generate_readme_files(output_path)
        console.print("[green]✅ GitHub multi-language README files generated successfully![/green]")
        console.print("  📄 README.md (🇺🇸 English - GitHub default)")
        console.print("  📄 README.ko.md (🇰🇷 한국어 - Korean)")
        console.print(f"  📁 Output: {output_path.absolute()}")
        console.print("\n[blue]💡 GitHub will automatically show the appropriate language based on user's language preference.[/blue]")
    except Exception as e:
        console.print(f"[red]❌ Error generating README files:[/red] {e}")
        raise click.Abort() from e


def _show_template_info(template_name: str) -> None:
    """특정 템플릿의 상세 정보를 표시합니다."""
    template_key = template_name.replace("-", "-")

    console.print(
        Panel(
            f"[bold cyan]{template_name.upper()}[/bold cyan]\n\n{t(f'templates.{template_key}.description')}",
            title=t("templates.template_info"),
        )
    )

    # 주요 특징
    console.print(f"\n[bold green]{t('templates.features')}:[/bold green]")
    features = t(f"templates.{template_key}.features")
    for feature in features:
        console.print(f"  {feature}")

    # 적합한 사용 사례
    console.print(f"\n[bold blue]{t('templates.use_cases')}:[/bold blue]")
    use_cases = t(f"templates.{template_key}.use_cases")
    for use_case in use_cases:
        console.print(f"  • {use_case}")

    # 장점
    console.print(f"\n[bold green]{t('templates.advantages')}:[/bold green]")
    advantages = t(f"templates.{template_key}.advantages")
    for advantage in advantages:
        console.print(f"  {advantage}")

    # 단점
    console.print(f"\n[bold red]{t('templates.disadvantages')}:[/bold red]")
    disadvantages = t(f"templates.{template_key}.disadvantages")
    for disadvantage in disadvantages:
        console.print(f"  {disadvantage}")


def _show_all_templates_info() -> None:
    """모든 템플릿의 상세 정보를 표시합니다."""
    console.print(f"[bold blue]{t('templates.template_info')}[/bold blue]\n")

    for template_name in SUPPORTED_TEMPLATES:
        _show_template_info(template_name)
        console.print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()
