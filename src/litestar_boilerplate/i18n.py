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
        "architecture_types": "구조 유형",
        "usage": "사용법",
        "requirements": "요구사항",
        "dev_setup": "개발환경 설정",
        "language_support": "다국어 지원",
        "install_cli": "CLI 도구 설치",
        "create_project": "새 프로젝트 생성",
        "list_templates": "템플릿 목록 보기",
        "help": "도움말",
        "create_venv": "가상환경 생성",
        "install_deps": "의존성과 개발 의존성 설치",
        "install_cmd": 'pip install -e ".[dev]"',
        "detailed_docs": "각 구조별 상세 문서는 해당 디렉토리의 README를 참고하세요.",
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
        "description": "A collection of 3 project structure boilerplates based on Litestar.",
        "architecture_types": "Architecture Types",
        "usage": "Usage",
        "requirements": "Requirements",
        "dev_setup": "Development Setup",
        "language_support": "Language Support",
        "install_cli": "Install CLI tool",
        "create_project": "Create new project",
        "list_templates": "List templates",
        "help": "Help",
        "create_venv": "Create virtual environment",
        "install_deps": "Install dependencies and dev dependencies",
        "install_cmd": 'pip install -e ".[dev]"',
        "detailed_docs": "For detailed documentation of each structure, refer to the README in the respective directory.",
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
