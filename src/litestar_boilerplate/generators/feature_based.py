"""Feature-based Modular 구조 제너레이터."""

from pathlib import Path
from typing import Any

from .base import BaseGenerator


class FeatureBasedGenerator(BaseGenerator):
    """Feature-based Modular 구조를 생성하는 제너레이터."""

    def generate(self, project_name: str, output_path: Path) -> None:
        """Feature-based 구조 프로젝트를 생성합니다."""
        # 기본 디렉토리 구조 생성
        structure = self._get_directory_structure(project_name)
        self._create_directory_structure(output_path, structure)

        # 파일들 생성
        self._create_project_files(project_name, output_path)

    def _get_directory_structure(self, project_name: str) -> dict[str, Any]:
        """Feature-based 디렉토리 구조를 반환합니다."""
        return {
            f"{project_name}": {
                "__init__.py": None,
                "shared": {
                    "__init__.py": None,
                    "database": {
                        "__init__.py": None,
                        "base.py": None,
                        "session.py": None,
                    },
                    "config": {
                        "__init__.py": None,
                        "settings.py": None,
                    },
                    "exceptions": {
                        "__init__.py": None,
                        "base.py": None,
                    },
                    "schemas": {
                        "__init__.py": None,
                        "base.py": None,
                    },
                    "security": {
                        "__init__.py": None,
                        "auth.py": None,
                        "password.py": None,
                    },
                    "utils": {
                        "__init__.py": None,
                        "pagination.py": None,
                        "validators.py": None,
                    },
                },
                "features": {
                    "__init__.py": None,
                    "health": {
                        "__init__.py": None,
                        "router.py": None,
                        "schemas.py": None,
                    },
                    "users": {
                        "__init__.py": None,
                        "models": {
                            "__init__.py": None,
                            "user.py": None,
                        },
                        "schemas": {
                            "__init__.py": None,
                            "user_schemas.py": None,
                        },
                        "services": {
                            "__init__.py": None,
                            "user_service.py": None,
                        },
                        "repositories": {
                            "__init__.py": None,
                            "user_repository.py": None,
                        },
                        "routers": {
                            "__init__.py": None,
                            "user_router.py": None,
                        },
                        "dependencies": {
                            "__init__.py": None,
                            "user_deps.py": None,
                        },
                        "exceptions": {
                            "__init__.py": None,
                            "user_exceptions.py": None,
                        },
                    },
                    "auth": {
                        "__init__.py": None,
                        "models": {
                            "__init__.py": None,
                            "token.py": None,
                        },
                        "schemas": {
                            "__init__.py": None,
                            "auth_schemas.py": None,
                        },
                        "services": {
                            "__init__.py": None,
                            "auth_service.py": None,
                        },
                        "routers": {
                            "__init__.py": None,
                            "auth_router.py": None,
                        },
                        "dependencies": {
                            "__init__.py": None,
                            "auth_deps.py": None,
                        },
                    },
                },
                "app.py": None,
            },
            "tests": {
                "__init__.py": None,
                "features": {
                    "__init__.py": None,
                    "health": {
                        "__init__.py": None,
                        "test_health_router.py": None,
                    },
                    "users": {
                        "__init__.py": None,
                        "test_user_service.py": None,
                        "test_user_repository.py": None,
                        "test_user_router.py": None,
                    },
                    "auth": {
                        "__init__.py": None,
                        "test_auth_service.py": None,
                        "test_auth_router.py": None,
                    },
                },
                "conftest.py": None,
            },
            "alembic": {
                "versions": {},
                "env.py": None,
                "script.py.mako": None,
            },
            "requirements.txt": self._get_common_requirements(),
            "requirements-dev.txt": self._get_common_dev_requirements(),
            ".env.example": self._get_common_env_example(),
            ".gitignore": self._get_common_gitignore(),
            "alembic.ini": None,
            "README.md": None,
        }

    def _create_project_files(self, project_name: str, output_path: Path) -> None:
        """프로젝트 파일들을 생성합니다."""
        # Main app.py
        self._create_file(output_path / f"{project_name}" / "app.py", self._get_app_content(project_name))

        # README.md
        self._create_file(output_path / "README.md", self._get_readme_content(project_name))

        # Shared components
        self._create_shared_files(project_name, output_path)

        # Feature modules
        self._create_feature_files(project_name, output_path)

    def _get_app_content(self, project_name: str) -> str:
        """메인 애플리케이션 파일 내용을 반환합니다."""
        return f'''"""메인 애플리케이션 진입점."""

from litestar import Litestar
from litestar.logging import StructLoggingConfig

from {project_name}.features.health.router import health_router
from {project_name}.features.users.routers.user_router import user_router
from {project_name}.features.auth.routers.auth_router import auth_router
from {project_name}.shared.config.settings import get_settings

settings = get_settings()

app = Litestar(
    route_handlers=[
        health_router,
        user_router,
        auth_router,
    ],
    debug=settings.debug,
    logging_config=StructLoggingConfig(),
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
'''

    def _get_readme_content(self, project_name: str) -> str:
        """README 내용을 반환합니다."""
        return f"""# {project_name.title()}

Feature-based Modular 구조로 구성된 Litestar 프로젝트입니다.

## 프로젝트 구조

```
{project_name}/
├── {project_name}/                 # 메인 애플리케이션 패키지
│   ├── shared/               # 공유 컴포넌트
│   │   ├── database/        # 데이터베이스 설정
│   │   ├── config/          # 애플리케이션 설정
│   │   ├── exceptions/      # 공통 예외
│   │   ├── schemas/         # 공통 스키마
│   │   ├── security/        # 보안 관련
│   │   └── utils/           # 유틸리티
│   ├── features/            # 기능별 모듈
│   │   ├── health/          # 헬스체크 기능
│   │   ├── users/           # 사용자 관리 기능
│   │   │   ├── models/      # 사용자 모델
│   │   │   ├── schemas/     # 사용자 스키마
│   │   │   ├── services/    # 사용자 서비스
│   │   │   ├── repositories/ # 사용자 리포지토리
│   │   │   ├── routers/     # 사용자 라우터
│   │   │   ├── dependencies/ # 사용자 의존성
│   │   │   └── exceptions/  # 사용자 예외
│   │   └── auth/            # 인증/인가 기능
│   │       ├── models/      # 인증 모델
│   │       ├── schemas/     # 인증 스키마
│   │       ├── services/    # 인증 서비스
│   │       ├── routers/     # 인증 라우터
│   │       └── dependencies/ # 인증 의존성
│   └── app.py              # 애플리케이션 진입점
├── tests/                   # 테스트 코드
│   └── features/           # 기능별 테스트
│       ├── health/         # 헬스체크 테스트
│       ├── users/          # 사용자 관리 테스트
│       └── auth/           # 인증 테스트
└── alembic/                # 데이터베이스 마이그레이션
```

## 아키텍처 특징

### 수직적 슬라이싱
- 각 기능이 완전히 독립된 모듈로 구성
- 기능별로 모든 계층 포함 (모델, 서비스, 라우터 등)
- 기능 간 의존성 최소화

### 기능 캡슐화
- **모델**: 각 기능의 데이터 모델 정의
- **스키마**: 입출력 데이터 검증 및 직렬화
- **서비스**: 비즈니스 로직 구현
- **리포지토리**: 데이터 접근 계층
- **라우터**: HTTP 엔드포인트 정의
- **의존성**: 의존성 주입 관리

### 공유 컴포넌트
- **Database**: 데이터베이스 연결 및 세션 관리
- **Config**: 애플리케이션 설정
- **Security**: 인증/인가 공통 기능
- **Utils**: 범용 유틸리티 함수

## 설치 및 실행

```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Linux/Mac

# 의존성 설치
pip install -r requirements.txt
pip install -r requirements-dev.txt

# 환경변수 설정
cp .env.example .env
# .env 파일을 수정하여 데이터베이스 연결 정보 등을 설정

# 데이터베이스 마이그레이션
alembic upgrade head

# 애플리케이션 실행
litestar run --reload
```

## API 엔드포인트

### Health
- `GET /health` - 헬스체크

### Users
- `GET /users` - 사용자 목록 조회
- `POST /users` - 사용자 생성
- `GET /users/{{id}}` - 특정 사용자 조회
- `PUT /users/{{id}}` - 사용자 정보 수정
- `DELETE /users/{{id}}` - 사용자 삭제

### Auth
- `POST /auth/login` - 로그인
- `POST /auth/refresh` - 토큰 갱신
- `POST /auth/logout` - 로그아웃

## 개발 가이드

### 새로운 기능 추가

1. **기능 모듈 생성**: `features/{{feature_name}}/` 디렉토리 생성

2. **기본 구조 설정**:
   ```
   features/{{feature_name}}/
   ├── models/
   ├── schemas/
   ├── services/
   ├── repositories/
   ├── routers/
   ├── dependencies/
   └── exceptions/
   ```

3. **구현 순서**:
   - 모델 정의 (`models/`)
   - 스키마 정의 (`schemas/`)
   - 리포지토리 구현 (`repositories/`)
   - 서비스 로직 구현 (`services/`)
   - 의존성 설정 (`dependencies/`)
   - 라우터 구현 (`routers/`)
   - 예외 처리 (`exceptions/`)

4. **메인 앱에 등록**: `app.py`에 라우터 추가

### 기능 간 통신

- **직접 의존성**: 다른 기능의 서비스를 직접 import
- **이벤트 기반**: 공유 이벤트 시스템 사용 (필요시)
- **공유 컴포넌트**: `shared/` 모듈 활용

### 테스트 전략

```bash
# 특정 기능 테스트
pytest tests/features/users/

# 전체 기능 테스트
pytest tests/features/

# 커버리지 포함
pytest --cov={project_name}
```

### 마이크로서비스 전환

각 기능 모듈은 독립적인 마이크로서비스로 쉽게 분리 가능:

1. 기능 모듈을 별도 프로젝트로 복사
2. 공유 컴포넌트를 해당 서비스에 복사 또는 라이브러리화
3. 서비스 간 통신을 HTTP API 또는 메시지 큐로 변경

## 장점

- **모듈성**: 기능별 완전한 분리
- **개발 효율성**: 팀별 병렬 개발 가능
- **유지보수성**: 변경 영향 범위가 명확
- **확장성**: 새 기능 추가가 간단
- **재사용성**: 기능 모듈의 독립적 재사용
- **마이크로서비스 준비**: 쉬운 서비스 분리

## 단점

- **코드 중복**: 기능 간 유사한 코드 중복 가능
- **일관성 관리**: 기능별 구현 방식 차이 발생 가능
- **의존성 관리**: 기능 간 의존성 복잡해질 수 있음
- **초기 복잡성**: 작은 프로젝트에는 과도할 수 있음

## 적합한 사용 사례

- 대규모 팀이 개발하는 프로젝트
- 독립적인 기능들로 구성된 애플리케이션
- 마이크로서비스 아키텍처로의 전환 계획이 있는 경우
- 기능별 배포가 필요한 경우
- 여러 제품/서비스를 하나의 플랫폼에서 관리하는 경우
"""

    def _create_shared_files(self, project_name: str, output_path: Path) -> None:
        """공유 컴포넌트 파일들을 생성합니다."""
        # Settings
        settings_content = '''"""애플리케이션 설정."""

from functools import lru_cache
from typing import Optional

from pydantic import Field
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """애플리케이션 설정 클래스."""

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    # Application
    app_name: str = Field(default="FeatureApp", description="애플리케이션 이름")
    debug: bool = Field(default=False, description="디버그 모드")
    secret_key: str = Field(description="JWT 서명용 비밀키")

    # Database
    database_url: str = Field(description="데이터베이스 연결 URL")

    # Redis
    redis_url: str = Field(default="redis://localhost:6379/0", description="Redis 연결 URL")


@lru_cache()
def get_settings() -> Settings:
    """설정 인스턴스를 반환합니다 (캐시됨)."""
    return Settings()
'''
        self._create_file(output_path / f"{project_name}" / "shared" / "config" / "settings.py", settings_content)

    def _create_feature_files(self, project_name: str, output_path: Path) -> None:
        """기능별 파일들을 생성합니다."""
        # Health feature
        health_router_content = '''"""헬스체크 라우터."""

from litestar import Router, get


@get("/health")
async def health_check() -> dict[str, str]:
    """헬스체크 엔드포인트."""
    return {"status": "healthy", "service": "feature-based-app"}


health_router = Router(path="", route_handlers=[health_check])
'''
        self._create_file(output_path / f"{project_name}" / "features" / "health" / "router.py", health_router_content)

        # User feature - simplified
        user_router_content = '''"""사용자 라우터."""

from litestar import Router, get, post


@get("/users")
async def get_users() -> list[dict]:
    """사용자 목록 조회."""
    return []


@post("/users")
async def create_user(data: dict) -> dict:
    """사용자 생성."""
    return {"message": "User created", "data": data}


user_router = Router(path="/users", route_handlers=[get_users, create_user])
'''
        self._create_file(output_path / f"{project_name}" / "features" / "users" / "routers" / "user_router.py", user_router_content)

        # Auth feature - simplified
        auth_router_content = '''"""인증 라우터."""

from litestar import Router, post


@post("/login")
async def login(credentials: dict) -> dict:
    """로그인."""
    return {"access_token": "fake-token", "token_type": "bearer"}


@post("/refresh")
async def refresh_token() -> dict:
    """토큰 갱신."""
    return {"access_token": "new-fake-token", "token_type": "bearer"}


auth_router = Router(path="/auth", route_handlers=[login, refresh_token])
'''
        self._create_file(output_path / f"{project_name}" / "features" / "auth" / "routers" / "auth_router.py", auth_router_content)
