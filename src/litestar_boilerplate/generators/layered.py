"""Layered + Controller 중심 구조 제너레이터."""

from pathlib import Path
from typing import Any

from .base import BaseGenerator


class LayeredGenerator(BaseGenerator):
    """Layered + Controller 중심 구조를 생성하는 제너레이터."""

    def generate(self, project_name: str, output_path: Path) -> None:
        """Layered 구조 프로젝트를 생성합니다.

        Args:
            project_name: 프로젝트 이름
            output_path: 출력 경로
        """
        # 기본 디렉토리 구조 생성
        structure = self._get_directory_structure(project_name)
        self._create_directory_structure(output_path, structure)

        # 파일들 생성
        self._create_project_files(project_name, output_path)

    def _get_directory_structure(self, project_name: str) -> dict[str, Any]:
        """디렉토리 구조를 반환합니다."""
        return {
            f"{project_name}": {
                "__init__.py": None,
                "controllers": {
                    "__init__.py": None,
                    "user_controller.py": None,
                    "health_controller.py": None,
                },
                "services": {
                    "__init__.py": None,
                    "user_service.py": None,
                    "base_service.py": None,
                },
                "repositories": {
                    "__init__.py": None,
                    "user_repository.py": None,
                    "base_repository.py": None,
                },
                "models": {
                    "__init__.py": None,
                    "user.py": None,
                    "base.py": None,
                },
                "schemas": {
                    "__init__.py": None,
                    "user.py": None,
                    "common.py": None,
                },
                "core": {
                    "__init__.py": None,
                    "config.py": None,
                    "database.py": None,
                    "logger.py": None,
                    "security.py": None,
                },
                "exceptions": {
                    "__init__.py": None,
                    "base.py": None,
                    "user.py": None,
                },
                "utils": {
                    "__init__.py": None,
                    "helpers.py": None,
                },
                "app.py": None,
            },
            "tests": {
                "__init__.py": None,
                "conftest.py": None,
                "test_controllers": {
                    "__init__.py": None,
                    "test_user_controller.py": None,
                },
                "test_services": {
                    "__init__.py": None,
                    "test_user_service.py": None,
                },
                "test_repositories": {
                    "__init__.py": None,
                    "test_user_repository.py": None,
                },
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

        # Core files
        self._create_core_files(project_name, output_path)

        # Model files
        self._create_model_files(project_name, output_path)

        # Schema files
        self._create_schema_files(project_name, output_path)

        # Repository files
        self._create_repository_files(project_name, output_path)

        # Service files
        self._create_service_files(project_name, output_path)

        # Controller files
        self._create_controller_files(project_name, output_path)

        # Test files
        self._create_test_files(project_name, output_path)

        # Alembic files
        self._create_alembic_files(project_name, output_path)

    def _get_app_content(self, project_name: str) -> str:
        """메인 애플리케이션 파일 내용을 반환합니다."""
        return f'''"""메인 애플리케이션 진입점."""

from litestar import Litestar
from litestar.logging import StructLoggingConfig

from {project_name}.controllers import health_controller, user_controller
from {project_name}.core.config import get_settings
from {project_name}.core.database import get_db_config

settings = get_settings()

app = Litestar(
    route_handlers=[
        health_controller.router,
        user_controller.router,
    ],
    debug=settings.debug,
    logging_config=StructLoggingConfig(),
    plugins=[get_db_config()],
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
'''

    def _get_readme_content(self, project_name: str) -> str:
        """README 내용을 반환합니다."""
        return f"""# {project_name.title()}

Layered + Controller 중심 구조로 구성된 Litestar 프로젝트입니다.

## 프로젝트 구조

```
{project_name}/
├── {project_name}/                 # 메인 애플리케이션 패키지
│   ├── controllers/           # 컨트롤러 계층 (HTTP 요청 처리)
│   ├── services/             # 서비스 계층 (비즈니스 로직)
│   ├── repositories/         # 리포지토리 계층 (데이터 접근)
│   ├── models/              # 데이터베이스 모델
│   ├── schemas/             # Pydantic 스키마
│   ├── core/                # 핵심 설정 및 유틸리티
│   ├── exceptions/          # 예외 클래스
│   ├── utils/               # 공통 유틸리티
│   └── app.py              # 애플리케이션 진입점
├── tests/                   # 테스트 코드
├── alembic/                # 데이터베이스 마이그레이션
└── requirements.txt        # 의존성 목록
```

## 아키텍처 특징

### 계층 구조
- **Controller**: HTTP 요청/응답 처리, 입력 검증
- **Service**: 비즈니스 로직 구현, 트랜잭션 관리
- **Repository**: 데이터 접근 추상화, ORM 쿼리
- **Model**: 데이터베이스 엔티티 정의

### 의존성 방향
```
Controller → Service → Repository → Model
```

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

- `GET /health` - 헬스체크
- `GET /users` - 사용자 목록 조회
- `POST /users` - 사용자 생성
- `GET /users/{{id}}` - 특정 사용자 조회
- `PUT /users/{{id}}` - 사용자 정보 수정
- `DELETE /users/{{id}}` - 사용자 삭제

## 개발 가이드

### 새로운 기능 추가

1. **모델 정의**: `models/` 디렉토리에 데이터베이스 모델 추가
2. **스키마 정의**: `schemas/` 디렉토리에 Pydantic 스키마 추가
3. **리포지토리 구현**: `repositories/` 디렉토리에 데이터 접근 로직 추가
4. **서비스 구현**: `services/` 디렉토리에 비즈니스 로직 추가
5. **컨트롤러 구현**: `controllers/` 디렉토리에 HTTP 엔드포인트 추가
6. **테스트 작성**: `tests/` 디렉토리에 각 계층별 테스트 추가

### 테스트 실행

```bash
# 전체 테스트 실행
pytest

# 커버리지 포함 테스트
pytest --cov={project_name}

# 특정 테스트 파일 실행
pytest tests/test_controllers/test_user_controller.py
```

### 코드 품질 관리

```bash
# 코드 포맷팅
ruff format .

# 린트 검사
ruff check .

# 타입 검사
mypy {project_name}/
```

## 장점

- 명확한 책임 분리
- 이해하기 쉬운 구조
- 테스트 작성 용이
- 소규모 팀에 적합

## 단점

- 복잡한 비즈니스 로직 처리 한계
- 계층 간 데이터 전달 오버헤드
- 도메인 모델의 빈약함
"""

    def _create_core_files(self, project_name: str, output_path: Path) -> None:
        """핵심 설정 파일들을 생성합니다."""
        # Config
        config_content = '''"""애플리케이션 설정."""

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
    app_name: str = Field(default="MyApp", description="애플리케이션 이름")
    debug: bool = Field(default=False, description="디버그 모드")
    secret_key: str = Field(description="JWT 서명용 비밀키")

    # Database
    database_url: str = Field(description="데이터베이스 연결 URL")

    # Redis
    redis_url: str = Field(default="redis://localhost:6379/0", description="Redis 연결 URL")

    # Logging
    log_level: str = Field(default="INFO", description="로그 레벨")


@lru_cache()
def get_settings() -> Settings:
    """설정 인스턴스를 반환합니다 (캐시됨)."""
    return Settings()
'''
        self._create_file(output_path / f"{project_name}" / "core" / "config.py", config_content)

        # Database
        database_content = f'''"""데이터베이스 설정."""

from litestar.plugins.sqlalchemy import SQLAlchemyAsyncConfig, SQLAlchemyPlugin
from sqlalchemy.ext.asyncio import AsyncSession

from {project_name}.core.config import get_settings

settings = get_settings()

async_config = SQLAlchemyAsyncConfig(
    connection_string=settings.database_url,
    metadata=None,  # 자동 테이블 생성 비활성화
    create_all=False,
)


def get_db_config() -> SQLAlchemyPlugin:
    """데이터베이스 플러그인 설정을 반환합니다."""
    return SQLAlchemyPlugin(config=async_config)


async def get_db_session() -> AsyncSession:
    """비동기 데이터베이스 세션을 반환합니다."""
    # 실제 구현에서는 의존성 주입을 통해 세션을 가져옵니다
    raise NotImplementedError("의존성 주입을 통해 세션을 가져오세요")
'''
        self._create_file(output_path / f"{project_name}" / "core" / "database.py", database_content)

        # Logger
        logger_content = '''"""로깅 설정."""

import structlog

logger = structlog.get_logger()


def setup_logging() -> None:
    """로깅을 설정합니다."""
    structlog.configure(
        processors=[
            structlog.stdlib.filter_by_level,
            structlog.stdlib.add_logger_name,
            structlog.stdlib.add_log_level,
            structlog.stdlib.PositionalArgumentsFormatter(),
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.processors.UnicodeDecoder(),
            structlog.processors.JSONRenderer()
        ],
        context_class=dict,
        logger_factory=structlog.stdlib.LoggerFactory(),
        wrapper_class=structlog.stdlib.BoundLogger,
        cache_logger_on_first_use=True,
    )
'''
        self._create_file(output_path / f"{project_name}" / "core" / "logger.py", logger_content)

        # Security
        security_content = '''"""보안 관련 유틸리티."""

from datetime import datetime, timedelta
from typing import Any, Dict, Optional

import jwt
from passlib.context import CryptContext

from .config import get_settings

settings = get_settings()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def create_access_token(data: Dict[str, Any], expires_delta: Optional[timedelta] = None) -> str:
    """JWT 액세스 토큰을 생성합니다."""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, settings.secret_key, algorithm="HS256")
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """비밀번호를 검증합니다."""
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """비밀번호를 해시화합니다."""
    return pwd_context.hash(password)
'''
        self._create_file(output_path / f"{project_name}" / "core" / "security.py", security_content)

    def _create_model_files(self, project_name: str, output_path: Path) -> None:
        """모델 파일들을 생성합니다."""
        # Base model
        base_content = '''"""기본 모델 클래스."""

from datetime import datetime
from typing import Optional

from sqlalchemy import DateTime, func
from sqlalchemy.ext.declarative import declared_attr
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


class Base(DeclarativeBase):
    """모든 모델의 기본 클래스."""

    @declared_attr.directive
    def __tablename__(cls) -> str:
        """테이블 이름을 클래스 이름의 snake_case로 자동 생성합니다."""
        return cls.__name__.lower() + "s"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False
    )
    updated_at: Mapped[Optional[datetime]] = mapped_column(
        DateTime(timezone=True),
        onupdate=func.now(),
        nullable=True
    )
'''
        self._create_file(output_path / f"{project_name}" / "models" / "base.py", base_content)

        # User model
        user_model_content = f'''"""사용자 모델."""

from typing import Optional

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from {project_name}.models.base import Base


class User(Base):
    """사용자 모델."""

    __tablename__ = "users"

    username: Mapped[str] = mapped_column(String(50), unique=True, index=True, nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, index=True, nullable=False)
    full_name: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    hashed_password: Mapped[str] = mapped_column(String(255), nullable=False)
    is_active: Mapped[bool] = mapped_column(default=True, nullable=False)

    def __repr__(self) -> str:
        """문자열 표현을 반환합니다."""
        return f"<User(id={{self.id}}, username={{self.username}}, email={{self.email}})>"
'''
        self._create_file(output_path / f"{project_name}" / "models" / "user.py", user_model_content)

    def _create_schema_files(self, project_name: str, output_path: Path) -> None:
        """스키마 파일들을 생성합니다."""
        # Common schemas
        common_content = '''"""공통 스키마."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class BaseSchema(BaseModel):
    """기본 스키마 클래스."""

    model_config = ConfigDict(from_attributes=True)


class TimestampMixin(BaseModel):
    """타임스탬프 믹스인."""

    created_at: datetime
    updated_at: Optional[datetime] = None


class PaginationParams(BaseModel):
    """페이지네이션 파라미터."""

    page: int = 1
    size: int = 10

    @property
    def offset(self) -> int:
        """오프셋을 반환합니다."""
        return (self.page - 1) * self.size


class PaginatedResponse(BaseModel):
    """페이지네이션 응답."""

    items: list
    total: int
    page: int
    size: int
    pages: int

    @classmethod
    def create(cls, items: list, total: int, page: int, size: int) -> "PaginatedResponse":
        """페이지네이션 응답을 생성합니다."""
        return cls(
            items=items,
            total=total,
            page=page,
            size=size,
            pages=(total + size - 1) // size
        )
'''
        self._create_file(output_path / f"{project_name}" / "schemas" / "common.py", common_content)

        # User schemas
        user_schema_content = f'''"""사용자 스키마."""

from typing import Optional

from pydantic import BaseModel, EmailStr, Field

from {project_name}.schemas.common import BaseSchema, TimestampMixin


class UserBase(BaseModel):
    """사용자 기본 스키마."""

    username: str = Field(..., min_length=3, max_length=50)
    email: EmailStr
    full_name: Optional[str] = Field(None, max_length=100)


class UserCreate(UserBase):
    """사용자 생성 스키마."""

    password: str = Field(..., min_length=8, max_length=100)


class UserUpdate(BaseModel):
    """사용자 수정 스키마."""

    username: Optional[str] = Field(None, min_length=3, max_length=50)
    email: Optional[EmailStr] = None
    full_name: Optional[str] = Field(None, max_length=100)
    password: Optional[str] = Field(None, min_length=8, max_length=100)


class UserResponse(UserBase, BaseSchema, TimestampMixin):
    """사용자 응답 스키마."""

    id: int
    is_active: bool


class UserListResponse(BaseModel):
    """사용자 목록 응답 스키마."""

    users: list[UserResponse]
    total: int
'''
        self._create_file(output_path / f"{project_name}" / "schemas" / "user.py", user_schema_content)

    def _create_repository_files(self, project_name: str, output_path: Path) -> None:
        """리포지토리 파일들을 생성합니다."""
        # Base repository
        base_repo_content = '''"""기본 리포지토리 클래스."""

from typing import Any, Dict, Generic, List, Optional, Type, TypeVar

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import DeclarativeBase

ModelType = TypeVar("ModelType", bound=DeclarativeBase)


class BaseRepository(Generic[ModelType]):
    """기본 리포지토리 클래스."""

    def __init__(self, model: Type[ModelType], session: AsyncSession) -> None:
        """리포지토리를 초기화합니다."""
        self.model = model
        self.session = session

    async def get(self, id: Any) -> Optional[ModelType]:
        """ID로 엔티티를 조회합니다."""
        result = await self.session.execute(
            select(self.model).where(self.model.id == id)
        )
        return result.scalar_one_or_none()

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[ModelType]:
        """모든 엔티티를 조회합니다."""
        result = await self.session.execute(
            select(self.model)
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())

    async def create(self, obj_in: Dict[str, Any]) -> ModelType:
        """새 엔티티를 생성합니다."""
        db_obj = self.model(**obj_in)
        self.session.add(db_obj)
        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def update(self, db_obj: ModelType, obj_in: Dict[str, Any]) -> ModelType:
        """엔티티를 수정합니다."""
        for field, value in obj_in.items():
            if hasattr(db_obj, field):
                setattr(db_obj, field, value)

        await self.session.commit()
        await self.session.refresh(db_obj)
        return db_obj

    async def delete(self, id: Any) -> bool:
        """엔티티를 삭제합니다."""
        db_obj = await self.get(id)
        if db_obj:
            await self.session.delete(db_obj)
            await self.session.commit()
            return True
        return False

    async def count(self) -> int:
        """전체 엔티티 수를 반환합니다."""
        result = await self.session.execute(
            select(func.count()).select_from(self.model)
        )
        return result.scalar() or 0
'''
        self._create_file(output_path / f"{project_name}" / "repositories" / "base_repository.py", base_repo_content)

        # User repository
        user_repo_content = f'''"""사용자 리포지토리."""

from typing import Optional

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from {project_name}.models.user import User
from {project_name}.repositories.base_repository import BaseRepository


class UserRepository(BaseRepository[User]):
    """사용자 리포지토리."""

    def __init__(self, session: AsyncSession) -> None:
        """사용자 리포지토리를 초기화합니다."""
        super().__init__(User, session)

    async def get_by_username(self, username: str) -> Optional[User]:
        """사용자명으로 사용자를 조회합니다."""
        result = await self.session.execute(
            select(User).where(User.username == username)
        )
        return result.scalar_one_or_none()

    async def get_by_email(self, email: str) -> Optional[User]:
        """이메일로 사용자를 조회합니다."""
        result = await self.session.execute(
            select(User).where(User.email == email)
        )
        return result.scalar_one_or_none()

    async def get_active_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        """활성 사용자 목록을 조회합니다."""
        result = await self.session.execute(
            select(User)
            .where(User.is_active == True)
            .offset(skip)
            .limit(limit)
        )
        return list(result.scalars().all())
'''
        self._create_file(output_path / f"{project_name}" / "repositories" / "user_repository.py", user_repo_content)

    def _create_service_files(self, project_name: str, output_path: Path) -> None:
        """서비스 파일들을 생성합니다."""
        # Base service
        base_service_content = '''"""기본 서비스 클래스."""

from typing import Any, Dict, Generic, List, Optional, TypeVar

from sqlalchemy.ext.asyncio import AsyncSession

from .base_repository import BaseRepository

RepositoryType = TypeVar("RepositoryType", bound=BaseRepository)


class BaseService(Generic[RepositoryType]):
    """기본 서비스 클래스."""

    def __init__(self, repository: RepositoryType) -> None:
        """서비스를 초기화합니다."""
        self.repository = repository

    async def get(self, id: Any) -> Optional[Any]:
        """ID로 엔티티를 조회합니다."""
        return await self.repository.get(id)

    async def get_all(self, skip: int = 0, limit: int = 100) -> List[Any]:
        """모든 엔티티를 조회합니다."""
        return await self.repository.get_all(skip=skip, limit=limit)

    async def create(self, obj_in: Dict[str, Any]) -> Any:
        """새 엔티티를 생성합니다."""
        return await self.repository.create(obj_in)

    async def update(self, id: Any, obj_in: Dict[str, Any]) -> Optional[Any]:
        """엔티티를 수정합니다."""
        db_obj = await self.repository.get(id)
        if not db_obj:
            return None
        return await self.repository.update(db_obj, obj_in)

    async def delete(self, id: Any) -> bool:
        """엔티티를 삭제합니다."""
        return await self.repository.delete(id)
'''
        self._create_file(output_path / f"{project_name}" / "services" / "base_service.py", base_service_content)

        # User service
        user_service_content = f'''"""사용자 서비스."""

from typing import Optional

from {project_name}.core.security import get_password_hash, verify_password
from {project_name}.models.user import User
from {project_name}.repositories.user_repository import UserRepository
from {project_name}.schemas.user import UserCreate, UserUpdate
from {project_name}.services.base_service import BaseService


class UserService(BaseService[UserRepository]):
    """사용자 서비스."""

    def __init__(self, repository: UserRepository) -> None:
        """사용자 서비스를 초기화합니다."""
        super().__init__(repository)

    async def create_user(self, user_create: UserCreate) -> User:
        """새 사용자를 생성합니다."""
        # 사용자명 중복 확인
        existing_user = await self.repository.get_by_username(user_create.username)
        if existing_user:
            raise ValueError("이미 사용 중인 사용자명입니다.")

        # 이메일 중복 확인
        existing_email = await self.repository.get_by_email(user_create.email)
        if existing_email:
            raise ValueError("이미 사용 중인 이메일입니다.")

        # 비밀번호 해시화
        hashed_password = get_password_hash(user_create.password)

        user_data = user_create.model_dump(exclude={{"password"}})
        user_data["hashed_password"] = hashed_password

        return await self.repository.create(user_data)

    async def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        """사용자 정보를 수정합니다."""
        user = await self.repository.get(user_id)
        if not user:
            return None

        update_data = user_update.model_dump(exclude_unset=True)

        # 사용자명 중복 확인
        if "username" in update_data:
            existing_user = await self.repository.get_by_username(update_data["username"])
            if existing_user and existing_user.id != user_id:
                raise ValueError("이미 사용 중인 사용자명입니다.")

        # 이메일 중복 확인
        if "email" in update_data:
            existing_email = await self.repository.get_by_email(update_data["email"])
            if existing_email and existing_email.id != user_id:
                raise ValueError("이미 사용 중인 이메일입니다.")

        # 비밀번호 해시화
        if "password" in update_data:
            update_data["hashed_password"] = get_password_hash(update_data.pop("password"))

        return await self.repository.update(user, update_data)

    async def authenticate_user(self, username: str, password: str) -> Optional[User]:
        """사용자 인증을 수행합니다."""
        user = await self.repository.get_by_username(username)
        if not user or not verify_password(password, user.hashed_password):
            return None
        return user

    async def get_active_users(self, skip: int = 0, limit: int = 100) -> list[User]:
        """활성 사용자 목록을 조회합니다."""
        return await self.repository.get_active_users(skip=skip, limit=limit)
'''
        self._create_file(output_path / f"{project_name}" / "services" / "user_service.py", user_service_content)

    def _create_controller_files(self, project_name: str, output_path: Path) -> None:
        """컨트롤러 파일들을 생성합니다."""
        # Health controller
        health_controller_content = '''"""헬스체크 컨트롤러."""

from litestar import Controller, get
from litestar.response import Response


class HealthController(Controller):
    """헬스체크 컨트롤러."""

    path = "/health"

    @get("/")
    async def health_check(self) -> dict[str, str]:
        """헬스체크 엔드포인트."""
        return {"status": "healthy", "service": "litestar-app"}


router = HealthController
'''
        self._create_file(output_path / f"{project_name}" / "controllers" / "health_controller.py", health_controller_content)

        # User controller
        user_controller_content = f'''"""사용자 컨트롤러."""

from typing import List

from litestar import Controller, delete, get, patch, post
from litestar.di import Provide
from litestar.exceptions import NotFoundException, ValidationException
from litestar.params import Parameter
from sqlalchemy.ext.asyncio import AsyncSession

from {project_name}.repositories.user_repository import UserRepository
from {project_name}.schemas.user import UserCreate, UserResponse, UserUpdate
from {project_name}.services.user_service import UserService


async def get_user_service(db_session: AsyncSession) -> UserService:
    """사용자 서비스 의존성을 제공합니다."""
    repository = UserRepository(db_session)
    return UserService(repository)


class UserController(Controller):
    """사용자 컨트롤러."""

    path = "/users"
    dependencies = {{"user_service": Provide(get_user_service)}}

    @get("/")
    async def get_users(
        self,
        user_service: UserService,
        skip: int = Parameter(default=0, ge=0),
        limit: int = Parameter(default=10, ge=1, le=100),
    ) -> List[UserResponse]:
        """사용자 목록을 조회합니다."""
        users = await user_service.get_active_users(skip=skip, limit=limit)
        return [UserResponse.model_validate(user) for user in users]

    @post("/")
    async def create_user(
        self,
        user_service: UserService,
        data: UserCreate,
    ) -> UserResponse:
        """새 사용자를 생성합니다."""
        try:
            user = await user_service.create_user(data)
            return UserResponse.model_validate(user)
        except ValueError as e:
            raise ValidationException(detail=str(e)) from e

    @get("/{{user_id:int}}")
    async def get_user(
        self,
        user_service: UserService,
        user_id: int,
    ) -> UserResponse:
        """특정 사용자를 조회합니다."""
        user = await user_service.get(user_id)
        if not user:
            raise NotFoundException(detail=f"사용자 ID {{user_id}}를 찾을 수 없습니다.")
        return UserResponse.model_validate(user)

    @patch("/{{user_id:int}}")
    async def update_user(
        self,
        user_service: UserService,
        user_id: int,
        data: UserUpdate,
    ) -> UserResponse:
        """사용자 정보를 수정합니다."""
        try:
            user = await user_service.update_user(user_id, data)
            if not user:
                raise NotFoundException(detail=f"사용자 ID {{user_id}}를 찾을 수 없습니다.")
            return UserResponse.model_validate(user)
        except ValueError as e:
            raise ValidationException(detail=str(e)) from e

    @delete("/{{user_id:int}}")
    async def delete_user(
        self,
        user_service: UserService,
        user_id: int,
    ) -> dict[str, str]:
        """사용자를 삭제합니다."""
        success = await user_service.delete(user_id)
        if not success:
            raise NotFoundException(detail=f"사용자 ID {{user_id}}를 찾을 수 없습니다.")
        return {{"message": "사용자가 성공적으로 삭제되었습니다."}}


router = UserController
'''
        self._create_file(output_path / f"{project_name}" / "controllers" / "user_controller.py", user_controller_content)

    def _create_test_files(self, project_name: str, output_path: Path) -> None:
        """테스트 파일들을 생성합니다."""
        # conftest.py
        conftest_content = f'''"""테스트 설정."""

from typing import TYPE_CHECKING, AsyncGenerator

import pytest
from httpx import AsyncClient
from litestar import Litestar
from litestar.testing import AsyncTestClient
from sqlalchemy import NullPool
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker

from {project_name}.app import app
from {project_name}.models.base import Base

if TYPE_CHECKING:
    from _pytest.fixtures import FixtureRequest
    from pytest_mock.plugin import MockerFixture

# 테스트용 인메모리 데이터베이스
TEST_DATABASE_URL = "sqlite+aiosqlite:///:memory:"


@pytest.fixture
async def engine():
    """테스트용 데이터베이스 엔진을 생성합니다."""
    test_engine = create_async_engine(
        TEST_DATABASE_URL,
        echo=False,
        poolclass=NullPool,
    )

    async with test_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    yield test_engine

    await test_engine.dispose()


@pytest.fixture
async def db_session(engine) -> AsyncGenerator[AsyncSession, None]:
    """테스트용 데이터베이스 세션을 생성합니다."""
    async_session = sessionmaker(
        engine, class_=AsyncSession, expire_on_commit=False
    )

    async with async_session() as session:
        yield session


@pytest.fixture
async def client() -> AsyncGenerator[AsyncClient, None]:
    """테스트 클라이언트를 생성합니다."""
    async with AsyncTestClient(app=app) as test_client:
        yield test_client


@pytest.fixture
def mock_user_data() -> dict:
    """테스트용 사용자 데이터를 반환합니다."""
    return {{
        "username": "testuser",
        "email": "test@example.com",
        "full_name": "Test User",
        "password": "testpassword123"
    }}
'''
        self._create_file(output_path / "tests" / "conftest.py", conftest_content)

        # User controller test
        user_controller_test = '''"""사용자 컨트롤러 테스트."""

from typing import TYPE_CHECKING

import pytest
from httpx import AsyncClient

if TYPE_CHECKING:
    from pytest_mock.plugin import MockerFixture


class TestUserController:
    """사용자 컨트롤러 테스트 클래스."""

    @pytest.mark.asyncio
    async def test_get_users_empty(self, client: AsyncClient) -> None:
        """빈 사용자 목록 조회 테스트."""
        response = await client.get("/users")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)
        assert len(data) == 0

    @pytest.mark.asyncio
    async def test_create_user_success(
        self,
        client: AsyncClient,
        mock_user_data: dict
    ) -> None:
        """사용자 생성 성공 테스트."""
        response = await client.post("/users", json=mock_user_data)
        assert response.status_code == 201

        data = response.json()
        assert data["username"] == mock_user_data["username"]
        assert data["email"] == mock_user_data["email"]
        assert data["full_name"] == mock_user_data["full_name"]
        assert "password" not in data
        assert "hashed_password" not in data
        assert "id" in data

    @pytest.mark.asyncio
    async def test_create_user_invalid_data(self, client: AsyncClient) -> None:
        """잘못된 데이터로 사용자 생성 테스트."""
        invalid_data = {
            "username": "a",  # 너무 짧음
            "email": "invalid-email",  # 잘못된 이메일 형식
            "password": "123"  # 너무 짧음
        }

        response = await client.post("/users", json=invalid_data)
        assert response.status_code == 400

    @pytest.mark.asyncio
    async def test_get_user_not_found(self, client: AsyncClient) -> None:
        """존재하지 않는 사용자 조회 테스트."""
        response = await client.get("/users/999")
        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_update_user_not_found(self, client: AsyncClient) -> None:
        """존재하지 않는 사용자 수정 테스트."""
        update_data = {"full_name": "Updated Name"}
        response = await client.patch("/users/999", json=update_data)
        assert response.status_code == 404

    @pytest.mark.asyncio
    async def test_delete_user_not_found(self, client: AsyncClient) -> None:
        """존재하지 않는 사용자 삭제 테스트."""
        response = await client.delete("/users/999")
        assert response.status_code == 404
'''
        self._create_file(output_path / "tests" / "test_controllers" / "test_user_controller.py", user_controller_test)

    def _create_alembic_files(self, project_name: str, output_path: Path) -> None:
        """Alembic 설정 파일들을 생성합니다."""
        # alembic.ini
        alembic_ini_content = f"""# A generic, single database configuration.

[alembic]
# path to migration scripts
script_location = alembic

# template used to generate migration file names; The default value is %%(rev)s_%%(slug)s
# Uncomment the line below if you want the files to be prepended with date and time
# file_template = %%Y%%m%%d_%%H%%M_%%rev%%s_%%(slug)s

# sys.path path, will be prepended to sys.path if present.
# defaults to the current working directory.
prepend_sys_path = .

# timezone to use when rendering the date within the migration file
# as well as the filename.
# If specified, requires the python-dateutil library that can be
# installed by adding `alembic[tz]` to the pip requirements
# string value is passed to dateutil.tz.gettz()
# leave blank for localtime
# timezone =

# max length of characters to apply to the
# "slug" field
# truncate_slug_length = 40

# set to 'true' to run the environment during
# the 'revision' command, regardless of autogenerate
# revision_environment = false

# set to 'true' to allow .pyc and .pyo files without
# a source .py file to be detected as revisions in the
# versions/ directory
# sourceless = false

# version path separator; As mentioned above, this is the character used to split
# version_locations. The default within new alembic.ini files is "os", which uses
# os.pathsep. If this key is omitted entirely, it falls back to the legacy
# behavior of splitting on spaces and/or commas.
# Valid values for version_path_separator are:
#
# version_path_separator = :
# version_path_separator = ;
# version_path_separator = space
version_path_separator = os

# set to 'true' to search source files recursively
# in each "version_locations" directory
# new in Alembic version 1.10
# recursive_version_locations = false

# the output encoding used when revision files
# are written from script.py.mako
# output_encoding = utf-8

sqlalchemy.url = postgresql+asyncpg://user:password@localhost:5432/{project_name}


[post_write_hooks]
# post_write_hooks defines scripts or Python functions that are run
# on newly generated revision scripts.  See the documentation for further
# detail and examples

# format using "black" - use the console_scripts runner, against the "black" entrypoint
# hooks = black
# black.type = console_scripts
# black.entrypoint = black
# black.options = -l 79 REVISION_SCRIPT_FILENAME

# lint with attempts to fix using "ruff" - use the exec runner, execute a binary
# hooks = ruff
# ruff.type = exec
# ruff.executable = %(here)s/.venv/bin/ruff
# ruff.options = --fix REVISION_SCRIPT_FILENAME

# Logging configuration
[loggers]
keys = root,sqlalchemy,alembic

[handlers]
keys = console

[formatters]
keys = generic

[logger_root]
level = WARN
handlers = console
qualname =

[logger_sqlalchemy]
level = WARN
handlers =
qualname = sqlalchemy.engine

[logger_alembic]
level = INFO
handlers =
qualname = alembic

[handler_console]
class = StreamHandler
args = (sys.stderr,)
level = NOTSET
formatter = generic

[formatter_generic]
format = %%(levelname)-5.5s [%%(name)s] %%(message)s
datefmt = %%H:%%M:%%S
"""
        self._create_file(output_path / "alembic.ini", alembic_ini_content)

        # env.py
        env_content = f'''"""Alembic 환경 설정."""

import asyncio
from logging.config import fileConfig

from alembic import context
from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from {project_name}.core.config import get_settings
from {project_name}.models.base import Base

# Alembic Config 객체
config = context.config

# 설정 파일에서 로깅 설정
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# 모델의 메타데이터 추가
target_metadata = Base.metadata

# 환경변수에서 데이터베이스 URL 가져오기
settings = get_settings()
config.set_main_option("sqlalchemy.url", settings.database_url)


def run_migrations_offline() -> None:
    """오프라인 모드에서 마이그레이션 실행."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={{"paramstyle": "named"}},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    """연결을 사용하여 마이그레이션 실행."""
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """비동기 엔진에서 마이그레이션 실행."""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {{}}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """온라인 모드에서 마이그레이션 실행."""
    asyncio.run(run_async_migrations())


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
'''
        self._create_file(output_path / "alembic" / "env.py", env_content)
