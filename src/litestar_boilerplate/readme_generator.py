"""README 생성기 모듈."""

from pathlib import Path

from .i18n import Language, get_i18n, t


class ReadmeGenerator:
    """README 파일 생성기."""

    def __init__(self, language: Language = Language.KOREAN):
        """README 생성기를 초기화합니다."""
        self.language = language
        self.i18n = get_i18n()
        self.i18n.set_language(language)

    def generate_main_readme(self, output_path: Path | None = None) -> str:
        """메인 README 내용을 생성합니다."""
        content = self._generate_readme_content()

        if output_path:
            # 출력 디렉토리가 없으면 생성
            output_path.mkdir(parents=True, exist_ok=True)

            # GitHub 표준 언어별 README 파일명 결정
            filename = "README.md" if self.language == Language.ENGLISH else "README.ko.md"
            readme_path = output_path / filename
            readme_path.write_text(content, encoding="utf-8")

        return content

    def _generate_readme_content(self) -> str:
        """README 내용을 생성합니다."""
        return f"""{self._get_language_selector()}

# {t("readme.title")}

{t("readme.subtitle")}

{self._format_badges()}

{t("readme.description")}

{t("readme.key_features")}

{self._format_feature_points(t("readme.key_features_list"))}

{t("readme.architecture_types")}

### 1. {t("readme.features.layered.title")} (`layered/`)
{t("readme.features.layered.subtitle")}
{self._format_feature_points(t("readme.features.layered.points"))}

### 2. {t("readme.features.ddd-lite.title")} (`ddd-lite/`)
{t("readme.features.ddd-lite.subtitle")}
{self._format_feature_points(t("readme.features.ddd-lite.points"))}

### 3. {t("readme.features.feature-based.title")} (`feature-based/`)
{t("readme.features.feature-based.subtitle")}
{self._format_feature_points(t("readme.features.feature-based.points"))}

{t("readme.usage")}

```bash
# {t("readme.install_cli")}
pip install -e .

# {t("readme.create_project")}
litestar-boilerplate create --type layered --name my-project
litestar-boilerplate create --type ddd-lite --name my-project
litestar-boilerplate create --type feature-based --name my-project

# {t("readme.list_templates")}
litestar-boilerplate list-templates

# {t("readme.help")}
litestar-boilerplate --help
```

{t("readme.language_support")}

{self._get_language_support_section()}

{t("readme.requirements")}

- Python 3.11+
- Litestar 2.0+
- SQLAlchemy 2.0+
- Alembic
- Pydantic V2

{t("readme.dev_setup")}

```bash
# {t("readme.create_venv")}
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\\Scripts\\activate  # Windows

# {t("readme.install_deps")}
{t("readme.install_cmd")}
```

{t("readme.litestar_resources")}

{self._format_litestar_resources()}

{t("readme.detailed_docs")}

{t("readme.contributing")}

{t("readme.contributing_content")}

{t("readme.license")}

{t("readme.license_content")}
"""

    def _get_language_selector(self) -> str:
        """GitHub 스타일의 언어 선택기를 생성합니다."""
        if self.language == Language.KOREAN:
            return """<p align="right">
  <a href="README.md">🇺🇸 English</a> |
  <strong>🇰🇷 한국어</strong>
</p>"""
        else:
            return """<p align="right">
  <strong>🇺🇸 English</strong> |
  <a href="README.ko.md">🇰🇷 한국어</a>
</p>"""

    def _format_feature_points(self, points: list[str]) -> str:
        """특징 포인트를 포맷팅합니다."""
        return "\n".join(f"- {point}" for point in points)

    def _get_language_support_section(self) -> str:
        """언어 지원 섹션을 생성합니다."""
        if self.language == Language.KOREAN:
            return """이 CLI 도구는 한국어와 영어를 지원합니다:

```bash
# 한국어 사용 (기본값)
litestar-boilerplate --language ko list-templates

# 영어 사용
litestar-boilerplate --language en list-templates

# 단축 옵션
litestar-boilerplate -l en create --type layered --name my-app
```

📋 **README 다국어 지원**:
- [`README.md`](README.md) - 🇺🇸 English (GitHub 기본)
- [`README.ko.md`](README.ko.md) - 🇰🇷 한국어"""
        else:
            return """This CLI tool supports Korean and English:

```bash
# Use Korean
litestar-boilerplate --language ko list-templates

# Use English (default in English environment)
litestar-boilerplate --language en list-templates

# Short option
litestar-boilerplate -l ko create --type layered --name my-app
```

📋 **Multi-language README**:
- [`README.md`](README.md) - 🇺🇸 English (GitHub default)
- [`README.ko.md`](README.ko.md) - 🇰🇷 한국어 (Korean)"""

    def _format_litestar_resources(self) -> str:
        """Litestar 리소스 섹션을 포맷팅합니다."""
        resources = t("readme.litestar_resources_content")
        return "\n".join(resources)

    def _format_badges(self) -> str:
        """배지 섹션을 포맷팅합니다."""
        badges = t("readme.badges")
        return "\n".join(badges)


def generate_readme_files(output_path: Path) -> None:
    """GitHub 표준 다국어 README 파일을 생성합니다."""
    # 출력 디렉토리가 없으면 생성
    output_path.mkdir(parents=True, exist_ok=True)

    # 영어 README 생성 (GitHub 기본)
    en_generator = ReadmeGenerator(Language.ENGLISH)
    en_generator.generate_main_readme(output_path)

    # 한국어 README 생성
    ko_generator = ReadmeGenerator(Language.KOREAN)
    ko_generator.generate_main_readme(output_path)
