"""다국어 지원 모듈."""

from enum import Enum
from typing import Any


class Language(str, Enum):
    """지원하는 언어 목록."""

    KOREAN = "ko"
    ENGLISH = "en"


# 한국어 메시지
MESSAGES_KO: dict[str, Any] = {
    "cli": {
        "app_help": "Litestar 기반 프로젝트 구조 보일러플레이트 생성 도구",
        "language_help": "사용할 언어 (ko: 한국어, en: 영어)",
        "version_help": "버전 정보를 표시합니다",
        "list_help": "사용 가능한 템플릿 목록을 표시합니다",
        "info_help": "특정 템플릿의 상세 정보를 표시합니다",
        "create_help": "새 프로젝트를 생성합니다",
        "project_name_help": "생성할 프로젝트 이름",
        "template_help": "사용할 템플릿 타입",
        "output_help": "프로젝트를 생성할 경로 (기본값: 현재 디렉토리)",
        "force_help": "기존 디렉토리가 있어도 덮어쓰기",
        "template_arg_help": "정보를 확인할 템플릿 이름",
    },
    "templates": {
        "available_templates": "📋 사용 가능한 템플릿",
        "template_info": "📝 템플릿 정보",
        "name": "이름",
        "description": "설명",
        "features": "주요 특징",
        "use_cases": "적합한 사용 사례",
        "advantages": "장점",
        "disadvantages": "단점",
        "layered": {
            "description": "전통적인 3계층 아키텍처 (Controller-Service-Repository)",
            "features": [
                "🏗️ 명확한 계층 분리",
                "🔄 MVC 패턴",
                "🧪 완전한 테스트 구조",
                "🔐 인증/보안 유틸리티",
                "📊 데이터베이스 마이그레이션",
            ],
            "use_cases": [
                "전통적인 웹 애플리케이션",
                "CRUD 중심의 비즈니스 애플리케이션",
                "팀 협업이 중요한 프로젝트",
                "명확한 구조가 필요한 경우",
            ],
            "advantages": ["✅ 이해하기 쉬운 구조", "✅ 빠른 개발 속도", "✅ 좋은 문서화", "✅ 표준적인 패턴"],
            "disadvantages": ["❌ 복잡한 비즈니스 로직에는 한계", "❌ 계층 간 강한 결합", "❌ 대규모 프로젝트에서 유지보수 어려움"],
        },
        "ddd-lite": {
            "description": "도메인 주도 설계 경량화 버전 (Domain-Application-Infrastructure)",
            "features": ["🎯 도메인 중심 설계", "🔄 CQRS 패턴", "📡 도메인 이벤트", "🏛️ 헥사고날 아키텍처 요소", "💉 의존성 주입"],
            "use_cases": ["복잡한 비즈니스 로직", "장기 유지보수 프로젝트", "대규모 팀 협업", "도메인 전문가와의 협업"],
            "advantages": ["✅ 비즈니스 로직 중심", "✅ 높은 테스트 가능성", "✅ 유연한 아키텍처", "✅ 확장성"],
            "disadvantages": ["❌ 높은 복잡성", "❌ 학습 곡선", "❌ 초기 개발 속도 느림", "❌ 단순한 CRUD에는 과도함"],
        },
        "feature-based": {
            "description": "기능별 수직 슬라이싱 구조 (Feature-by-Feature)",
            "features": ["📦 기능별 모듈화", "🔄 독립적인 개발", "🚀 마이크로서비스 준비", "🔧 공유 컴포넌트", "⚡ 빠른 기능 추가"],
            "use_cases": ["마이크로서비스 아키텍처", "여러 팀의 병렬 개발", "기능별 독립 배포", "빠른 프로토타이핑"],
            "advantages": ["✅ 기능별 독립성", "✅ 병렬 개발 가능", "✅ 마이크로서비스 전환 용이", "✅ 명확한 경계"],
            "disadvantages": ["❌ 코드 중복 가능성", "❌ 공통 로직 관리 복잡", "❌ 초기 구조 설계 중요", "❌ 작은 프로젝트에는 과도함"],
        },
    },
    "messages": {
        "project_created": "✅ 프로젝트가 성공적으로 생성되었습니다",
        "directory_exists": "⚠️ 디렉토리가 이미 존재합니다",
        "use_force": "--force 옵션을 사용하여 덮어쓸 수 있습니다",
        "invalid_template": "❌ 유효하지 않은 템플릿입니다",
        "creating_project": "🚀 프로젝트를 생성하는 중...",
        "next_steps": "다음 단계",
        "install_deps": "의존성과 개발 의존성 설치",
        "setup_env": "환경변수 설정: cp .env.example .env",
        "run_migrations": "데이터베이스 마이그레이션: alembic upgrade head",
        "start_server": "서버 실행: litestar run --reload",
    },
    "readme": {
        "title": "Litestar 보일러플레이트 컬렉션",
        "description": "Litestar 기반의 3가지 프로젝트 구조 보일러플레이트 모음입니다.",
        "subtitle": "🚀 현대적이고 확장 가능한 Python 웹 애플리케이션을 위한 프로덕션 레디 보일러플레이트",
        "badges": [
            "[![CI/CD Pipeline](https://github.com/dan1901/litestar-boilerplate/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/dan1901/litestar-boilerplate/actions)",
            "[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)",
            "[![Litestar](https://img.shields.io/badge/Litestar-2.0+-green.svg)](https://litestar.dev/)",
            "[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)",
            "[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)",
            "[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)"
        ],
        "badges_section": "## 📊 프로젝트 정보",
        "key_features": "## ✨ 주요 특징",
        "key_features_list": [
            "🏗️ **3가지 아키텍처 패턴**: Layered, DDD-lite, Feature-based 구조 지원",
            "🌍 **다국어 CLI**: 한국어/영어 지원으로 글로벌 개발팀 친화적",
            "⚡ **즉시 사용 가능**: 완전한 CRUD, 인증, 테스트 구조 포함",
            "🔧 **현대적 스택**: Litestar 2.0, SQLAlchemy 2.0, Pydantic V2 기반",
            "📚 **풍부한 문서**: 각 아키텍처별 상세 가이드 제공",
            "🧪 **테스트 우선**: pytest 기반 완전한 테스트 환경 구성"
        ],
        "architecture_types": "## 🏛️ 아키텍처 유형",
        "litestar_resources": "## 🧩 Litestar 관련 리소스",
        "litestar_resources_content": [
            "### 📖 공식 문서 및 리포지토리",
            "- [**Litestar 공식 문서**](https://docs.litestar.dev/) - 완전한 API 문서와 가이드",
            "- [**Litestar GitHub**](https://github.com/litestar-org/litestar) - 메인 리포지토리",
            "- [**Litestar Fullstack 예제**](https://github.com/litestar-org/litestar-fullstack) - 실제 프로덕션 예제",
            "",
            "### 🎓 학습 자료",
            "- [**Awesome Litestar**](https://github.com/litestar-org/awesome-litestar) - 큐레이션된 Litestar 리소스 모음",
            "- [**Litestar 튜토리얼**](https://docs.litestar.dev/latest/tutorials/) - 단계별 학습 가이드",
            "- [**Litestar 예제 모음**](https://github.com/litestar-org/litestar/tree/main/docs/examples) - 다양한 사용 사례 예제",
            "",
            "### 🛠️ 도구 및 플러그인",
            "- [**Litestar CLI**](https://docs.litestar.dev/latest/usage/cli/) - 강력한 명령줄 도구",
            "- [**Advanced Alchemy**](https://github.com/litestar-org/advanced-alchemy) - SQLAlchemy 확장",
            "- [**Litestar Users**](https://github.com/litestar-org/litestar-users) - 사용자 관리 플러그인"
        ],
        "usage": "## 🚀 사용법",
        "requirements": "## 📋 요구사항",
        "dev_setup": "## 🛠️ 개발환경 설정",
        "language_support": "## 🌍 다국어 지원",
        "install_cli": "CLI 도구 설치",
        "create_project": "새 프로젝트 생성",
        "list_templates": "템플릿 목록 보기",
        "help": "도움말",
        "create_venv": "가상환경 생성",
        "install_deps": "의존성과 개발 의존성 설치",
        "install_cmd": 'pip install -e ".[dev]"',
        "detailed_docs": "## 📚 상세 문서\n\n각 구조별 상세 문서와 예제는 해당 디렉토리의 README를 참고하세요.",
        "contributing": "## 🤝 기여하기",
        "contributing_content": "이 프로젝트에 기여하고 싶으시다면 이슈를 생성하거나 풀 리퀘스트를 보내주세요. 모든 기여를 환영합니다!",
        "license": "## 📄 라이선스",
        "license_content": "이 프로젝트는 MIT 라이선스 하에 배포됩니다.",
        "features": {
            "layered": {
                "title": "Layered + Controller 중심 구조",
                "subtitle": "전통적인 레이어드 아키텍처와 컨트롤러 중심의 구조",
                "points": ["명확한 계층 분리 (Controller, Service, Repository, Model)", "MVC 패턴 기반", "간단하고 이해하기 쉬운 구조"],
            },
            "ddd-lite": {
                "title": "DDD-lite",
                "subtitle": "도메인 주도 설계의 핵심 개념을 적용한 경량화된 구조",
                "points": ["도메인 중심 모델링", "애그리게이트와 도메인 서비스", "헥사고날 아키텍처 요소"],
            },
            "feature-based": {
                "title": "Feature-based Modular",
                "subtitle": "기능별 모듈화된 구조",
                "points": ["기능별 완전한 캡슐화", "수직적 슬라이싱", "마이크로서비스 전환 용이"],
            },
        },
    },
}

# 영어 메시지
MESSAGES_EN: dict[str, Any] = {
    "cli": {
        "app_help": "Litestar-based project structure boilerplate generator",
        "language_help": "Language to use (ko: Korean, en: English)",
        "version_help": "Show version information",
        "list_help": "List available templates",
        "info_help": "Show detailed information about a specific template",
        "create_help": "Create a new project",
        "project_name_help": "Name of the project to create",
        "template_help": "Template type to use",
        "output_help": "Path where to create the project (default: current directory)",
        "force_help": "Overwrite existing directory if it exists",
        "template_arg_help": "Template name to get information about",
    },
    "templates": {
        "available_templates": "📋 Available Templates",
        "template_info": "📝 Template Information",
        "name": "Name",
        "description": "Description",
        "features": "Key Features",
        "use_cases": "Suitable Use Cases",
        "advantages": "Advantages",
        "disadvantages": "Disadvantages",
        "layered": {
            "description": "Traditional 3-layer architecture (Controller-Service-Repository)",
            "features": [
                "🏗️ Clear layer separation",
                "🔄 MVC pattern",
                "🧪 Complete test structure",
                "🔐 Authentication/security utilities",
                "📊 Database migrations",
            ],
            "use_cases": [
                "Traditional web applications",
                "CRUD-focused business applications",
                "Team collaboration projects",
                "Cases requiring clear structure",
            ],
            "advantages": ["✅ Easy to understand structure", "✅ Fast development speed", "✅ Good documentation", "✅ Standard patterns"],
            "disadvantages": [
                "❌ Limited for complex business logic",
                "❌ Strong coupling between layers",
                "❌ Difficult maintenance in large projects",
            ],
        },
        "ddd-lite": {
            "description": "Lightweight Domain-Driven Design (Domain-Application-Infrastructure)",
            "features": [
                "🎯 Domain-centric design",
                "🔄 CQRS pattern",
                "📡 Domain events",
                "🏛️ Hexagonal architecture elements",
                "💉 Dependency injection",
            ],
            "use_cases": [
                "Complex business logic",
                "Long-term maintenance projects",
                "Large team collaboration",
                "Collaboration with domain experts",
            ],
            "advantages": ["✅ Business logic focused", "✅ High testability", "✅ Flexible architecture", "✅ Scalability"],
            "disadvantages": ["❌ High complexity", "❌ Learning curve", "❌ Slow initial development", "❌ Overkill for simple CRUD"],
        },
        "feature-based": {
            "description": "Feature-by-feature vertical slicing structure",
            "features": [
                "📦 Feature-based modularization",
                "🔄 Independent development",
                "🚀 Microservice ready",
                "🔧 Shared components",
                "⚡ Fast feature addition",
            ],
            "use_cases": [
                "Microservice architecture",
                "Parallel development by multiple teams",
                "Independent feature deployment",
                "Rapid prototyping",
            ],
            "advantages": [
                "✅ Feature independence",
                "✅ Parallel development possible",
                "✅ Easy microservice transition",
                "✅ Clear boundaries",
            ],
            "disadvantages": [
                "❌ Possible code duplication",
                "❌ Complex shared logic management",
                "❌ Important initial structure design",
                "❌ Overkill for small projects",
            ],
        },
    },
    "messages": {
        "project_created": "✅ Project created successfully",
        "directory_exists": "⚠️ Directory already exists",
        "use_force": "Use --force option to overwrite",
        "invalid_template": "❌ Invalid template",
        "creating_project": "🚀 Creating project...",
        "next_steps": "Next Steps",
        "install_deps": "Install dependencies: pip install -r requirements.txt",
        "setup_env": "Setup environment: cp .env.example .env",
        "run_migrations": "Run migrations: alembic upgrade head",
        "start_server": "Start server: litestar run --reload",
    },
    "readme": {
        "title": "Litestar Boilerplate Collection",
        "description": "A collection of 3 Litestar-based project structure boilerplates.",
        "subtitle": "🚀 Production-ready boilerplates for modern and scalable Python web applications",
        "badges": [
            "[![CI/CD Pipeline](https://github.com/dan1901/litestar-boilerplate/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/dan1901/litestar-boilerplate/actions)",
            "[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)",
            "[![Litestar](https://img.shields.io/badge/Litestar-2.0+-green.svg)](https://litestar.dev/)",
            "[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)",
            "[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)",
            "[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)"
        ],
        "badges_section": "## 📊 Project Information",
        "key_features": "## ✨ Key Features",
        "key_features_list": [
            "🏗️ **3 Architecture Patterns**: Support for Layered, DDD-lite, and Feature-based structures",
            "🌍 **Multilingual CLI**: Korean/English support for global development teams",
            "⚡ **Ready to Use**: Complete CRUD, authentication, and testing structure included",
            "🔧 **Modern Stack**: Based on Litestar 2.0, SQLAlchemy 2.0, Pydantic V2",
            "📚 **Rich Documentation**: Detailed guides for each architecture",
            "🧪 **Test-First**: Complete testing environment with pytest"
        ],
        "architecture_types": "## 🏛️ Architecture Types",
        "litestar_resources": "## 🧩 Litestar Resources",
        "litestar_resources_content": [
            "### 📖 Official Documentation & Repositories",
            "- [**Litestar Official Docs**](https://docs.litestar.dev/) - Complete API documentation and guides",
            "- [**Litestar GitHub**](https://github.com/litestar-org/litestar) - Main repository",
            "- [**Litestar Fullstack Example**](https://github.com/litestar-org/litestar-fullstack) - Real production example",
            "",
            "### 🎓 Learning Resources",
            "- [**Awesome Litestar**](https://github.com/litestar-org/awesome-litestar) - Curated collection of Litestar resources",
            "- [**Litestar Tutorials**](https://docs.litestar.dev/latest/tutorials/) - Step-by-step learning guides",
            "- [**Litestar Examples**](https://github.com/litestar-org/litestar/tree/main/docs/examples) - Various use case examples",
            "",
            "### 🛠️ Tools & Plugins",
            "- [**Litestar CLI**](https://docs.litestar.dev/latest/usage/cli/) - Powerful command-line tool",
            "- [**Advanced Alchemy**](https://github.com/litestar-org/advanced-alchemy) - SQLAlchemy extensions",
            "- [**Litestar Users**](https://github.com/litestar-org/litestar-users) - User management plugin"
        ],
        "usage": "## 🚀 Usage",
        "requirements": "## 📋 Requirements",
        "dev_setup": "## 🛠️ Development Setup",
        "language_support": "## 🌍 Language Support",
        "install_cli": "Install CLI tool",
        "create_project": "Create new project",
        "list_templates": "List templates",
        "help": "Help",
        "create_venv": "Create virtual environment",
        "install_deps": "Install dependencies and dev dependencies",
        "install_cmd": 'pip install -e ".[dev]"',
        "detailed_docs": "## 📚 Detailed Documentation\n\nFor detailed documentation and examples of each structure, refer to the README in the respective directory.",
        "contributing": "## 🤝 Contributing",
        "contributing_content": "If you'd like to contribute to this project, please create an issue or submit a pull request. All contributions are welcome!",
        "license": "## 📄 License",
        "license_content": "This project is distributed under the MIT License.",
        "features": {
            "layered": {
                "title": "Layered + Controller-Centric Structure",
                "subtitle": "Traditional layered architecture with controller-centric structure",
                "points": [
                    "Clear layer separation (Controller, Service, Repository, Model)",
                    "MVC pattern based",
                    "Simple and easy to understand structure",
                ],
            },
            "ddd-lite": {
                "title": "DDD-lite",
                "subtitle": "Lightweight structure applying core concepts of Domain-Driven Design",
                "points": ["Domain-centric modeling", "Aggregates and domain services", "Hexagonal architecture elements"],
            },
            "feature-based": {
                "title": "Feature-based Modular",
                "subtitle": "Structure modularized by features",
                "points": ["Complete encapsulation by features", "Vertical slicing", "Easy transition to microservices"],
            },
        },
    },
}

# 전체 메시지 매핑
MESSAGES = {
    Language.KOREAN: MESSAGES_KO,
    Language.ENGLISH: MESSAGES_EN,
}


class I18n:
    """다국어 지원 클래스."""

    def __init__(self, language: Language = Language.KOREAN):
        """I18n 인스턴스를 초기화합니다."""
        self.language = language
        self.messages = MESSAGES[language]

    def get(self, key: str, **kwargs) -> str:
        """메시지를 가져옵니다."""
        keys = key.split(".")
        value = self.messages

        for k in keys:
            if isinstance(value, dict) and k in value:
                value = value[k]
            else:
                return f"Missing translation: {key}"

        if isinstance(value, str) and kwargs:
            return value.format(**kwargs)

        return value

    def set_language(self, language: Language) -> None:
        """언어를 변경합니다."""
        self.language = language
        self.messages = MESSAGES[language]


# 전역 인스턴스
_i18n = I18n()


def get_i18n() -> I18n:
    """전역 I18n 인스턴스를 반환합니다."""
    return _i18n


def t(key: str, **kwargs) -> str:
    """메시지를 번역합니다."""
    return _i18n.get(key, **kwargs)


def set_language(language: Language) -> None:
    """전역 언어를 설정합니다."""
    _i18n.set_language(language)
