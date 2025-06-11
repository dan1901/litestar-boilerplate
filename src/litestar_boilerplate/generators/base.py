"""기본 제너레이터 클래스."""

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class BaseGenerator(ABC):
    """모든 프로젝트 구조 제너레이터의 기본 클래스."""

    def __init__(self) -> None:
        """제너레이터를 초기화합니다."""
        self.template_name = self.__class__.__name__.lower().replace("generator", "")

    @abstractmethod
    def generate(self, project_name: str, output_path: Path) -> None:
        """프로젝트를 생성합니다.

        Args:
            project_name: 생성할 프로젝트 이름
            output_path: 프로젝트를 생성할 경로
        """
        pass

    def _create_directory_structure(self, base_path: Path, structure: dict[str, Any]) -> None:
        """디렉토리 구조를 생성합니다.

        Args:
            base_path: 기본 경로
            structure: 생성할 디렉토리 구조 딕셔너리
        """
        for name, content in structure.items():
            path = base_path / name

            if isinstance(content, dict):
                # 디렉토리인 경우
                path.mkdir(parents=True, exist_ok=True)
                if content:  # 하위 구조가 있는 경우
                    self._create_directory_structure(path, content)
            else:
                # 파일인 경우
                path.parent.mkdir(parents=True, exist_ok=True)
                if content is not None:
                    path.write_text(content, encoding="utf-8")
                else:
                    # 빈 파일 생성
                    path.touch()

    def _create_file(self, file_path: Path, content: str) -> None:
        """파일을 생성합니다.

        Args:
            file_path: 생성할 파일 경로
            content: 파일 내용
        """
        file_path.parent.mkdir(parents=True, exist_ok=True)
        file_path.write_text(content, encoding="utf-8")

    def _get_common_requirements(self) -> str:
        """공통 requirements.txt 내용을 반환합니다."""
        return """# Core dependencies
litestar[standard]>=2.0.0
sqlalchemy>=2.0.0
alembic>=1.12.0
pydantic>=2.0.0
pydantic-settings>=2.0.0

# Database
asyncpg>=0.28.0
aiosqlite>=0.19.0

# Authentication
passlib[bcrypt]>=1.7.4
python-jose[cryptography]>=3.3.0

# Caching
redis>=4.5.0

# Logging
structlog>=23.0.0

# Development
uvicorn[standard]>=0.23.0
"""

    def _get_common_dev_requirements(self) -> str:
        """공통 requirements-dev.txt 내용을 반환합니다."""
        return """# Testing
pytest>=7.4.0
pytest-asyncio>=0.21.0
pytest-cov>=4.1.0
pytest-mock>=3.11.0
httpx>=0.24.0

# Code quality
ruff>=0.1.0
mypy>=1.5.0
pre-commit>=3.3.0

# Development tools
ipython>=8.0.0
"""

    def _get_common_gitignore(self) -> str:
        """공통 .gitignore 내용을 반환합니다."""
        return """# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
build/
develop-eggs/
dist/
downloads/
eggs/
.eggs/
lib/
lib64/
parts/
sdist/
var/
wheels/
share/python-wheels/
*.egg-info/
.installed.cfg
*.egg
MANIFEST

# Virtual environments
.env
.venv
env/
venv/
ENV/
env.bak/
venv.bak/

# IDEs
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# Logs
*.log
logs/

# Database
*.db
*.sqlite
*.sqlite3

# Environment variables
.env.local
.env.*.local

# Coverage
.coverage
.pytest_cache/
.coverage.*
htmlcov/

# mypy
.mypy_cache/
.dmypy.json
dmypy.json
"""

    def _get_common_env_example(self) -> str:
        """공통 .env.example 내용을 반환합니다."""
        return """# Application
DEBUG=True
APP_NAME=MyApp
SECRET_KEY=your-secret-key-here

# Database
DATABASE_URL=postgresql+asyncpg://user:password@localhost:5432/dbname

# Redis
REDIS_URL=redis://localhost:6379/0

# Logging
LOG_LEVEL=INFO
"""
