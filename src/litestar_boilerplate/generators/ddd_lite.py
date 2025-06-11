"""DDD-lite 구조 제너레이터."""

from pathlib import Path
from typing import Any

from .base import BaseGenerator


class DddLiteGenerator(BaseGenerator):
    """DDD-lite 구조를 생성하는 제너레이터."""

    def generate(self, project_name: str, output_path: Path) -> None:
        """DDD-lite 구조 프로젝트를 생성합니다."""
        # 기본 디렉토리 구조 생성
        structure = self._get_directory_structure(project_name)
        self._create_directory_structure(output_path, structure)

        # 파일들 생성
        self._create_project_files(project_name, output_path)

    def _get_directory_structure(self, project_name: str) -> dict[str, Any]:
        """DDD-lite 디렉토리 구조를 반환합니다."""
        return {
            f"{project_name}": {
                "__init__.py": None,
                "domain": {
                    "__init__.py": None,
                    "user": {
                        "__init__.py": None,
                        "entities": {
                            "__init__.py": None,
                            "user.py": None,
                        },
                        "value_objects": {
                            "__init__.py": None,
                            "email.py": None,
                            "user_name.py": None,
                        },
                        "repositories": {
                            "__init__.py": None,
                            "user_repository.py": None,
                        },
                        "services": {
                            "__init__.py": None,
                            "user_domain_service.py": None,
                        },
                        "events": {
                            "__init__.py": None,
                            "user_events.py": None,
                        },
                    },
                    "shared": {
                        "__init__.py": None,
                        "base_entity.py": None,
                        "base_value_object.py": None,
                        "domain_event.py": None,
                        "exceptions.py": None,
                    },
                },
                "application": {
                    "__init__.py": None,
                    "user": {
                        "__init__.py": None,
                        "commands": {
                            "__init__.py": None,
                            "create_user.py": None,
                            "update_user.py": None,
                            "delete_user.py": None,
                        },
                        "queries": {
                            "__init__.py": None,
                            "get_user.py": None,
                            "list_users.py": None,
                        },
                        "handlers": {
                            "__init__.py": None,
                            "user_command_handler.py": None,
                            "user_query_handler.py": None,
                            "user_event_handler.py": None,
                        },
                        "dtos": {
                            "__init__.py": None,
                            "user_dto.py": None,
                        },
                    },
                    "shared": {
                        "__init__.py": None,
                        "command_bus.py": None,
                        "query_bus.py": None,
                        "event_bus.py": None,
                    },
                },
                "infrastructure": {
                    "__init__.py": None,
                    "persistence": {
                        "__init__.py": None,
                        "models": {
                            "__init__.py": None,
                            "user_model.py": None,
                            "base_model.py": None,
                        },
                        "repositories": {
                            "__init__.py": None,
                            "sqlalchemy_user_repository.py": None,
                        },
                        "database.py": None,
                    },
                    "web": {
                        "__init__.py": None,
                        "controllers": {
                            "__init__.py": None,
                            "user_controller.py": None,
                            "health_controller.py": None,
                        },
                        "middleware": {
                            "__init__.py": None,
                        },
                    },
                    "config": {
                        "__init__.py": None,
                        "settings.py": None,
                        "container.py": None,
                    },
                    "external": {
                        "__init__.py": None,
                        "email_service.py": None,
                    },
                },
                "app.py": None,
            },
            "tests": {
                "__init__.py": None,
                "unit": {
                    "__init__.py": None,
                    "domain": {
                        "__init__.py": None,
                        "test_user_entity.py": None,
                        "test_user_domain_service.py": None,
                    },
                    "application": {
                        "__init__.py": None,
                        "test_user_handlers.py": None,
                    },
                },
                "integration": {
                    "__init__.py": None,
                    "test_user_repository.py": None,
                },
                "e2e": {
                    "__init__.py": None,
                    "test_user_api.py": None,
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

        # Domain layer files
        self._create_domain_files(project_name, output_path)

        # Application layer files
        self._create_application_files(project_name, output_path)

        # Infrastructure layer files
        self._create_infrastructure_files(project_name, output_path)

        # Test files
        self._create_test_files(project_name, output_path)

    def _get_app_content(self, project_name: str) -> str:
        """메인 애플리케이션 파일 내용을 반환합니다."""
        return f'''"""메인 애플리케이션 진입점."""

from litestar import Litestar
from litestar.logging import StructLoggingConfig

from {project_name}.infrastructure.web.controllers import health_controller, user_controller
from {project_name}.infrastructure.config.container import get_container
from {project_name}.infrastructure.config.settings import get_settings

settings = get_settings()
container = get_container()

app = Litestar(
    route_handlers=[
        health_controller.router,
        user_controller.router,
    ],
    debug=settings.debug,
    logging_config=StructLoggingConfig(),
    dependencies={{"container": container}},
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
'''

    def _get_readme_content(self, project_name: str) -> str:
        """README 내용을 반환합니다."""
        return f"""# {project_name.title()}

DDD-lite 구조로 구성된 Litestar 프로젝트입니다.

## 프로젝트 구조

```
{project_name}/
├── {project_name}/                 # 메인 애플리케이션 패키지
│   ├── domain/                # 도메인 계층
│   │   ├── user/             # 사용자 도메인
│   │   │   ├── entities/     # 엔티티
│   │   │   ├── value_objects/ # 값 객체
│   │   │   ├── repositories/ # 도메인 리포지토리 인터페이스
│   │   │   ├── services/     # 도메인 서비스
│   │   │   └── events/       # 도메인 이벤트
│   │   └── shared/           # 공유 도메인 컴포넌트
│   ├── application/          # 애플리케이션 계층
│   │   ├── user/            # 사용자 애플리케이션 서비스
│   │   │   ├── commands/    # 명령
│   │   │   ├── queries/     # 쿼리
│   │   │   ├── handlers/    # 핸들러
│   │   │   └── dtos/        # 데이터 전송 객체
│   │   └── shared/          # 공유 애플리케이션 컴포넌트
│   ├── infrastructure/      # 인프라스트럭처 계층
│   │   ├── persistence/     # 데이터베이스 관련
│   │   ├── web/            # 웹 관련 (컨트롤러, 미들웨어)
│   │   ├── config/         # 설정 및 DI 컨테이너
│   │   └── external/       # 외부 서비스 연동
│   └── app.py              # 애플리케이션 진입점
├── tests/                   # 테스트 코드
│   ├── unit/               # 단위 테스트
│   ├── integration/        # 통합 테스트
│   └── e2e/                # E2E 테스트
└── alembic/                # 데이터베이스 마이그레이션
```

## 아키텍처 특징

### DDD-lite 원칙
- **도메인 중심 설계**: 비즈니스 로직이 도메인 계층에 집중
- **계층 분리**: Domain → Application → Infrastructure
- **의존성 역전**: 인터페이스를 통한 느슨한 결합
- **애그리게이트**: 일관성 경계 정의
- **도메인 이벤트**: 도메인 변경 사항 전파

### CQRS 패턴
- **Command**: 상태 변경 작업
- **Query**: 데이터 조회 작업
- **분리된 모델**: 읽기/쓰기 최적화

### 헥사고날 아키텍처 요소
- **포트**: 인터페이스 정의
- **어댑터**: 외부 시스템 연동
- **의존성 주입**: 설정 가능한 구성요소

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
- `GET /users` - 사용자 목록 조회 (Query)
- `POST /users` - 사용자 생성 (Command)
- `GET /users/{{id}}` - 특정 사용자 조회 (Query)
- `PUT /users/{{id}}` - 사용자 정보 수정 (Command)
- `DELETE /users/{{id}}` - 사용자 삭제 (Command)

## 개발 가이드

### 새로운 애그리게이트 추가

1. **도메인 계층**:
   - `domain/{{aggregate_name}}/entities/` - 엔티티 추가
   - `domain/{{aggregate_name}}/value_objects/` - 값 객체 추가
   - `domain/{{aggregate_name}}/repositories/` - 리포지토리 인터페이스 추가
   - `domain/{{aggregate_name}}/services/` - 도메인 서비스 추가

2. **애플리케이션 계층**:
   - `application/{{aggregate_name}}/commands/` - 명령 추가
   - `application/{{aggregate_name}}/queries/` - 쿼리 추가
   - `application/{{aggregate_name}}/handlers/` - 핸들러 추가

3. **인프라스트럭처 계층**:
   - `infrastructure/persistence/models/` - 데이터 모델 추가
   - `infrastructure/persistence/repositories/` - 리포지토리 구현 추가
   - `infrastructure/web/controllers/` - 컨트롤러 추가

### 테스트 전략

```bash
# 단위 테스트 (도메인 로직)
pytest tests/unit/

# 통합 테스트 (리포지토리, 외부 연동)
pytest tests/integration/

# E2E 테스트 (전체 시나리오)
pytest tests/e2e/

# 전체 테스트 + 커버리지
pytest --cov={project_name}
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

- **비즈니스 로직 중심**: 도메인 중심의 명확한 구조
- **테스트 용이성**: 계층별 독립적인 테스트 가능
- **확장성**: 새로운 기능 추가가 체계적
- **유지보수성**: 변경 영향 범위가 명확

## 단점

- **복잡성**: 초기 설계와 구현이 복잡
- **학습 곡선**: DDD 개념 이해 필요
- **오버엔지니어링 위험**: 단순한 CRUD에는 과도할 수 있음

## 적합한 사용 사례

- 복잡한 비즈니스 로직을 가진 애플리케이션
- 장기간 유지보수가 필요한 프로젝트
- 여러 팀이 협업하는 대규모 프로젝트
- 도메인 전문가와의 긴밀한 협업이 필요한 경우
"""

    def _create_domain_files(self, project_name: str, output_path: Path) -> None:
        """도메인 계층 파일들을 생성합니다."""
        # Shared domain components
        self._create_shared_domain_files(project_name, output_path)

        # User domain files
        self._create_user_domain_files(project_name, output_path)

    def _create_shared_domain_files(self, project_name: str, output_path: Path) -> None:
        """공유 도메인 파일들을 생성합니다."""
        # Base Entity
        base_entity_content = '''"""기본 엔티티 클래스."""

from abc import ABC
from typing import Any, List
from uuid import UUID, uuid4

from .domain_event import DomainEvent


class BaseEntity(ABC):
    """모든 엔티티의 기본 클래스."""

    def __init__(self, id: UUID | None = None) -> None:
        """엔티티를 초기화합니다."""
        self._id = id or uuid4()
        self._domain_events: List[DomainEvent] = []

    @property
    def id(self) -> UUID:
        """엔티티 ID를 반환합니다."""
        return self._id

    def add_domain_event(self, event: DomainEvent) -> None:
        """도메인 이벤트를 추가합니다."""
        self._domain_events.append(event)

    def clear_domain_events(self) -> None:
        """도메인 이벤트를 지웁니다."""
        self._domain_events.clear()

    def get_domain_events(self) -> List[DomainEvent]:
        """도메인 이벤트 목록을 반환합니다."""
        return self._domain_events.copy()

    def __eq__(self, other: Any) -> bool:
        """엔티티 동등성을 확인합니다."""
        if not isinstance(other, BaseEntity):
            return False
        return self._id == other._id

    def __hash__(self) -> int:
        """엔티티 해시값을 반환합니다."""
        return hash(self._id)
'''
        self._create_file(output_path / f"{project_name}" / "domain" / "shared" / "base_entity.py", base_entity_content)

        # Base Value Object
        base_vo_content = '''"""기본 값 객체 클래스."""

from abc import ABC
from typing import Any, Tuple


class BaseValueObject(ABC):
    """모든 값 객체의 기본 클래스."""

    def __eq__(self, other: Any) -> bool:
        """값 객체 동등성을 확인합니다."""
        if not isinstance(other, self.__class__):
            return False
        return self._get_atomic_values() == other._get_atomic_values()

    def __hash__(self) -> int:
        """값 객체 해시값을 반환합니다."""
        return hash(self._get_atomic_values())

    def _get_atomic_values(self) -> Tuple[Any, ...]:
        """원자적 값들을 반환합니다. 하위 클래스에서 구현해야 합니다."""
        raise NotImplementedError("하위 클래스에서 _get_atomic_values()를 구현해야 합니다.")
'''
        self._create_file(output_path / f"{project_name}" / "domain" / "shared" / "base_value_object.py", base_vo_content)

        # Domain Event
        domain_event_content = '''"""도메인 이벤트 기본 클래스."""

from abc import ABC
from datetime import datetime
from typing import Any, Dict
from uuid import UUID, uuid4


class DomainEvent(ABC):
    """모든 도메인 이벤트의 기본 클래스."""

    def __init__(self, aggregate_id: UUID) -> None:
        """도메인 이벤트를 초기화합니다."""
        self.event_id = uuid4()
        self.aggregate_id = aggregate_id
        self.occurred_on = datetime.utcnow()

    def to_dict(self) -> Dict[str, Any]:
        """이벤트를 딕셔너리로 변환합니다."""
        return {
            "event_id": str(self.event_id),
            "event_type": self.__class__.__name__,
            "aggregate_id": str(self.aggregate_id),
            "occurred_on": self.occurred_on.isoformat(),
            "data": self._get_event_data(),
        }

    def _get_event_data(self) -> Dict[str, Any]:
        """이벤트 데이터를 반환합니다. 하위 클래스에서 구현해야 합니다."""
        return {}
'''
        self._create_file(output_path / f"{project_name}" / "domain" / "shared" / "domain_event.py", domain_event_content)

        # Domain Exceptions
        exceptions_content = '''"""도메인 예외 클래스들."""

from typing import Any, Optional


class DomainException(Exception):
    """도메인 계층의 기본 예외 클래스."""

    def __init__(self, message: str, details: Optional[Dict[str, Any]] = None) -> None:
        """도메인 예외를 초기화합니다."""
        super().__init__(message)
        self.message = message
        self.details = details or {}


class BusinessRuleViolationException(DomainException):
    """비즈니스 규칙 위반 예외."""
    pass


class AggregateNotFoundException(DomainException):
    """애그리게이트를 찾을 수 없을 때 발생하는 예외."""
    pass


class InvalidValueObjectException(DomainException):
    """잘못된 값 객체 생성 시 발생하는 예외."""
    pass
'''
        self._create_file(output_path / f"{project_name}" / "domain" / "shared" / "exceptions.py", exceptions_content)

    def _create_user_domain_files(self, project_name: str, output_path: Path) -> None:
        """사용자 도메인 파일들을 생성합니다."""
        # Value Objects
        self._create_user_value_objects(project_name, output_path)

        # User Entity
        user_entity_content = f'''"""사용자 엔티티."""

from typing import Optional
from uuid import UUID

from {project_name}.domain.shared.base_entity import BaseEntity
from {project_name}.domain.shared.exceptions import BusinessRuleViolationException
from {project_name}.domain.user.value_objects.email import Email
from {project_name}.domain.user.value_objects.user_name import UserName
from {project_name}.domain.user.events.user_events import UserCreatedEvent, UserUpdatedEvent


class User(BaseEntity):
    """사용자 애그리게이트 루트."""

    def __init__(
        self,
        user_name: UserName,
        email: Email,
        hashed_password: str,
        id: UUID | None = None,
        full_name: Optional[str] = None,
        is_active: bool = True,
    ) -> None:
        """사용자를 초기화합니다."""
        super().__init__(id)
        self._user_name = user_name
        self._email = email
        self._full_name = full_name
        self._hashed_password = hashed_password
        self._is_active = is_active

    @property
    def user_name(self) -> UserName:
        """사용자명을 반환합니다."""
        return self._user_name

    @property
    def email(self) -> Email:
        """이메일을 반환합니다."""
        return self._email

    @property
    def full_name(self) -> Optional[str]:
        """전체 이름을 반환합니다."""
        return self._full_name

    @property
    def hashed_password(self) -> str:
        """해시된 비밀번호를 반환합니다."""
        return self._hashed_password

    @property
    def is_active(self) -> bool:
        """활성 상태를 반환합니다."""
        return self._is_active

    @classmethod
    def create(
        cls,
        user_name: UserName,
        email: Email,
        hashed_password: str,
        full_name: Optional[str] = None,
    ) -> "User":
        """새 사용자를 생성합니다."""
        user = cls(
            user_name=user_name,
            email=email,
            hashed_password=hashed_password,
            full_name=full_name,
        )

        # 도메인 이벤트 추가
        user.add_domain_event(UserCreatedEvent(user.id, user_name.value, email.value))

        return user

    def update_profile(
        self,
        user_name: Optional[UserName] = None,
        email: Optional[Email] = None,
        full_name: Optional[str] = None,
    ) -> None:
        """사용자 프로필을 업데이트합니다."""
        if user_name is not None:
            self._user_name = user_name

        if email is not None:
            self._email = email

        if full_name is not None:
            self._full_name = full_name

        # 도메인 이벤트 추가
        self.add_domain_event(UserUpdatedEvent(self.id))

    def change_password(self, new_hashed_password: str) -> None:
        """비밀번호를 변경합니다."""
        if not new_hashed_password:
            raise BusinessRuleViolationException("비밀번호는 필수입니다.")

        self._hashed_password = new_hashed_password
        self.add_domain_event(UserUpdatedEvent(self.id))

    def activate(self) -> None:
        """사용자를 활성화합니다."""
        if self._is_active:
            raise BusinessRuleViolationException("이미 활성화된 사용자입니다.")

        self._is_active = True
        self.add_domain_event(UserUpdatedEvent(self.id))

    def deactivate(self) -> None:
        """사용자를 비활성화합니다."""
        if not self._is_active:
            raise BusinessRuleViolationException("이미 비활성화된 사용자입니다.")

        self._is_active = False
        self.add_domain_event(UserUpdatedEvent(self.id))

    def __repr__(self) -> str:
        """문자열 표현을 반환합니다."""
        return f"User(id={{self.id}}, user_name={{self.user_name.value}}, email={{self.email.value}})"
'''
        self._create_file(output_path / f"{project_name}" / "domain" / "user" / "entities" / "user.py", user_entity_content)

        # User Repository Interface
        user_repo_interface_content = f'''"""사용자 리포지토리 인터페이스."""

from abc import ABC, abstractmethod
from typing import List, Optional
from uuid import UUID

from {project_name}.domain.user.entities.user import User
from {project_name}.domain.user.value_objects.email import Email
from {project_name}.domain.user.value_objects.user_name import UserName


class UserRepository(ABC):
    """사용자 리포지토리 인터페이스."""

    @abstractmethod
    async def save(self, user: User) -> None:
        """사용자를 저장합니다."""
        pass

    @abstractmethod
    async def find_by_id(self, user_id: UUID) -> Optional[User]:
        """ID로 사용자를 조회합니다."""
        pass

    @abstractmethod
    async def find_by_user_name(self, user_name: UserName) -> Optional[User]:
        """사용자명으로 사용자를 조회합니다."""
        pass

    @abstractmethod
    async def find_by_email(self, email: Email) -> Optional[User]:
        """이메일로 사용자를 조회합니다."""
        pass

    @abstractmethod
    async def find_all(self, skip: int = 0, limit: int = 100) -> List[User]:
        """모든 사용자를 조회합니다."""
        pass

    @abstractmethod
    async def delete(self, user: User) -> None:
        """사용자를 삭제합니다."""
        pass

    @abstractmethod
    async def exists_by_user_name(self, user_name: UserName) -> bool:
        """사용자명 존재 여부를 확인합니다."""
        pass

    @abstractmethod
    async def exists_by_email(self, email: Email) -> bool:
        """이메일 존재 여부를 확인합니다."""
        pass
'''
        self._create_file(
            output_path / f"{project_name}" / "domain" / "user" / "repositories" / "user_repository.py", user_repo_interface_content
        )

    def _create_user_value_objects(self, project_name: str, output_path: Path) -> None:
        """사용자 값 객체들을 생성합니다."""
        # Email Value Object
        email_vo_content = rf'''"""이메일 값 객체."""

import re
from typing import Tuple, Any

from {project_name}.domain.shared.base_value_object import BaseValueObject
from {project_name}.domain.shared.exceptions import InvalidValueObjectException


class Email(BaseValueObject):
    """이메일 값 객체."""

    EMAIL_PATTERN = re.compile(
        r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{{2,}}$"
    )

    def __init__(self, value: str) -> None:
        """이메일을 초기화합니다."""
        if not value:
            raise InvalidValueObjectException("이메일은 필수입니다.")

        if not self.EMAIL_PATTERN.match(value):
            raise InvalidValueObjectException("유효하지 않은 이메일 형식입니다.")

        self._value = value.lower()

    @property
    def value(self) -> str:
        """이메일 값을 반환합니다."""
        return self._value

    def _get_atomic_values(self) -> Tuple[Any, ...]:
        """원자적 값들을 반환합니다."""
        return (self._value,)

    def __str__(self) -> str:
        """문자열 표현을 반환합니다."""
        return self._value
'''
        self._create_file(output_path / f"{project_name}" / "domain" / "user" / "value_objects" / "email.py", email_vo_content)

        # UserName Value Object
        username_vo_content = f'''"""사용자명 값 객체."""

from typing import Tuple, Any

from {project_name}.domain.shared.base_value_object import BaseValueObject
from {project_name}.domain.shared.exceptions import InvalidValueObjectException


class UserName(BaseValueObject):
    """사용자명 값 객체."""

    MIN_LENGTH = 3
    MAX_LENGTH = 50

    def __init__(self, value: str) -> None:
        """사용자명을 초기화합니다."""
        if not value:
            raise InvalidValueObjectException("사용자명은 필수입니다.")

        if len(value) < self.MIN_LENGTH:
            raise InvalidValueObjectException(f"사용자명은 최소 {{self.MIN_LENGTH}}자 이상이어야 합니다.")

        if len(value) > self.MAX_LENGTH:
            raise InvalidValueObjectException(f"사용자명은 최대 {{self.MAX_LENGTH}}자 이하여야 합니다.")

        # 영문, 숫자, 언더스코어만 허용
        if not value.replace("_", "").isalnum():
            raise InvalidValueObjectException("사용자명은 영문, 숫자, 언더스코어만 사용할 수 있습니다.")

        self._value = value

    @property
    def value(self) -> str:
        """사용자명 값을 반환합니다."""
        return self._value

    def _get_atomic_values(self) -> Tuple[Any, ...]:
        """원자적 값들을 반환합니다."""
        return (self._value,)

    def __str__(self) -> str:
        """문자열 표현을 반환합니다."""
        return self._value
'''
        self._create_file(output_path / f"{project_name}" / "domain" / "user" / "value_objects" / "user_name.py", username_vo_content)

        # User Events
        user_events_content = f'''"""사용자 도메인 이벤트."""

from typing import Any, Dict
from uuid import UUID

from {project_name}.domain.shared.domain_event import DomainEvent


class UserCreatedEvent(DomainEvent):
    """사용자 생성 이벤트."""

    def __init__(self, user_id: UUID, username: str, email: str) -> None:
        """사용자 생성 이벤트를 초기화합니다."""
        super().__init__(user_id)
        self.username = username
        self.email = email

    def _get_event_data(self) -> Dict[str, Any]:
        """이벤트 데이터를 반환합니다."""
        return {{
            "username": self.username,
            "email": self.email,
        }}


class UserUpdatedEvent(DomainEvent):
    """사용자 수정 이벤트."""

    def __init__(self, user_id: UUID) -> None:
        """사용자 수정 이벤트를 초기화합니다."""
        super().__init__(user_id)


class UserDeletedEvent(DomainEvent):
    """사용자 삭제 이벤트."""

    def __init__(self, user_id: UUID) -> None:
        """사용자 삭제 이벤트를 초기화합니다."""
        super().__init__(user_id)
'''
        self._create_file(output_path / f"{project_name}" / "domain" / "user" / "events" / "user_events.py", user_events_content)

    def _create_application_files(self, project_name: str, output_path: Path) -> None:
        """애플리케이션 계층 파일들을 생성합니다."""
        # Command Bus (simplified)
        command_bus_content = '''"""명령 버스."""

from typing import Any, Dict, Type
from abc import ABC, abstractmethod


class Command(ABC):
    """명령 인터페이스."""
    pass


class CommandHandler(ABC):
    """명령 핸들러 인터페이스."""

    @abstractmethod
    async def handle(self, command: Command) -> Any:
        """명령을 처리합니다."""
        pass


class CommandBus:
    """명령 버스."""

    def __init__(self) -> None:
        """명령 버스를 초기화합니다."""
        self._handlers: Dict[Type[Command], CommandHandler] = {{}}

    def register(self, command_type: Type[Command], handler: CommandHandler) -> None:
        """명령 핸들러를 등록합니다."""
        self._handlers[command_type] = handler

    async def execute(self, command: Command) -> Any:
        """명령을 실행합니다."""
        command_type = type(command)
        if command_type not in self._handlers:
            raise ValueError(f"{{command_type.__name__}}에 대한 핸들러가 등록되지 않았습니다.")

        handler = self._handlers[command_type]
        return await handler.handle(command)
'''
        self._create_file(output_path / f"{project_name}" / "application" / "shared" / "command_bus.py", command_bus_content)

        # Create User Command
        create_user_command_content = f'''"""사용자 생성 명령."""

from typing import Optional

from {project_name}.application.shared.command_bus import Command


class CreateUserCommand(Command):
    """사용자 생성 명령."""

    def __init__(
        self,
        username: str,
        email: str,
        password: str,
        full_name: Optional[str] = None,
    ) -> None:
        """사용자 생성 명령을 초기화합니다."""
        self.username = username
        self.email = email
        self.password = password
        self.full_name = full_name
'''
        self._create_file(
            output_path / f"{project_name}" / "application" / "user" / "commands" / "create_user.py", create_user_command_content
        )

    def _create_infrastructure_files(self, project_name: str, output_path: Path) -> None:
        """인프라스트럭처 계층 파일들을 생성합니다."""
        # Settings
        settings_content = '''"""애플리케이션 설정."""

from functools import lru_cache
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
    app_name: str = Field(default="DDD-Lite App", description="애플리케이션 이름")
    debug: bool = Field(default=False, description="디버그 모드")
    secret_key: str = Field(description="JWT 서명용 비밀키")

    # Database
    database_url: str = Field(description="데이터베이스 연결 URL")


@lru_cache()
def get_settings() -> Settings:
    """설정 인스턴스를 반환합니다 (캐시됨)."""
    return Settings()
'''
        self._create_file(output_path / f"{project_name}" / "infrastructure" / "config" / "settings.py", settings_content)

        # Container (simplified DI)
        container_content = '''"""의존성 주입 컨테이너."""

from typing import Any, Dict, TypeVar, Type

T = TypeVar('T')


class Container:
    """간단한 DI 컨테이너."""

    def __init__(self) -> None:
        """컨테이너를 초기화합니다."""
        self._services: Dict[Type, Any] = {{}}
        self._singletons: Dict[Type, Any] = {{}}

    def register(self, interface: Type[T], implementation: Any) -> None:
        """서비스를 등록합니다."""
        self._services[interface] = implementation

    def register_singleton(self, interface: Type[T], implementation: Any) -> None:
        """싱글톤 서비스를 등록합니다."""
        self._singletons[interface] = implementation

    def resolve(self, interface: Type[T]) -> T:
        """서비스를 해결합니다."""
        if interface in self._singletons:
            return self._singletons[interface]

        if interface in self._services:
            return self._services[interface]

        raise ValueError(f"{{interface.__name__}}에 대한 구현이 등록되지 않았습니다.")


_container = Container()


def get_container() -> Container:
    """컨테이너 인스턴스를 반환합니다."""
    return _container
'''
        self._create_file(output_path / f"{project_name}" / "infrastructure" / "config" / "container.py", container_content)

        # User Controller (simplified)
        user_controller_content = '''"""사용자 컨트롤러."""

from litestar import Controller, get, post


class UserController(Controller):
    """사용자 컨트롤러."""

    path = "/users"

    @get("/")
    async def list_users(self) -> list[dict]:
        """사용자 목록을 조회합니다."""
        return []

    @post("/")
    async def create_user(self, data: dict) -> dict:
        """사용자를 생성합니다."""
        return {"message": "User created", "data": data}


router = UserController
'''
        self._create_file(
            output_path / f"{project_name}" / "infrastructure" / "web" / "controllers" / "user_controller.py", user_controller_content
        )

        # Health Controller
        health_controller_content = '''"""헬스체크 컨트롤러."""

from litestar import Controller, get


class HealthController(Controller):
    """헬스체크 컨트롤러."""

    path = "/health"

    @get("/")
    async def health_check(self) -> dict[str, str]:
        """헬스체크 엔드포인트."""
        return {"status": "healthy", "service": "ddd-lite-app"}


router = HealthController
'''
        self._create_file(
            output_path / f"{project_name}" / "infrastructure" / "web" / "controllers" / "health_controller.py", health_controller_content
        )

    def _create_test_files(self, project_name: str, output_path: Path) -> None:
        """테스트 파일들을 생성합니다."""
        # Test conftest
        conftest_content = f'''"""테스트 설정."""

import pytest
from httpx import AsyncClient
from litestar.testing import AsyncTestClient

from {project_name}.app import app


@pytest.fixture
async def client() -> AsyncClient:
    """테스트 클라이언트를 생성합니다."""
    async with AsyncTestClient(app=app) as test_client:
        yield test_client
'''
        self._create_file(output_path / "tests" / "conftest.py", conftest_content)

        # Domain test example
        user_entity_test = f'''"""사용자 엔티티 테스트."""

import pytest
from uuid import uuid4

from {project_name}.domain.user.entities.user import User
from {project_name}.domain.user.value_objects.email import Email
from {project_name}.domain.user.value_objects.user_name import UserName
from {project_name}.domain.shared.exceptions import BusinessRuleViolationException


class TestUser:
    """사용자 엔티티 테스트 클래스."""

    def test_create_user_success(self) -> None:
        """사용자 생성 성공 테스트."""
        user_name = UserName("testuser")
        email = Email("test@example.com")
        hashed_password = "hashed_password"

        user = User.create(user_name, email, hashed_password, "Test User")

        assert user.user_name == user_name
        assert user.email == email
        assert user.hashed_password == hashed_password
        assert user.full_name == "Test User"
        assert user.is_active is True
        assert len(user.get_domain_events()) == 1

    def test_user_change_password_success(self) -> None:
        """비밀번호 변경 성공 테스트."""
        user = User.create(
            UserName("testuser"),
            Email("test@example.com"),
            "old_password"
        )
        user.clear_domain_events()

        user.change_password("new_password")

        assert user.hashed_password == "new_password"
        assert len(user.get_domain_events()) == 1

    def test_user_change_password_empty_fails(self) -> None:
        """빈 비밀번호로 변경 실패 테스트."""
        user = User.create(
            UserName("testuser"),
            Email("test@example.com"),
            "old_password"
        )

        with pytest.raises(BusinessRuleViolationException):
            user.change_password("")
'''
        self._create_file(output_path / "tests" / "unit" / "domain" / "test_user_entity.py", user_entity_test)
