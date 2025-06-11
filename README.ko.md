<p align="right">
  <a href="README.md">🇺🇸 English</a> | 
  <strong>🇰🇷 한국어</strong>
</p>

# Litestar 보일러플레이트 컬렉션

Litestar 기반의 3가지 프로젝트 구조 보일러플레이트 모음입니다.

## 구조 유형

### 1. Layered + Controller 중심 구조 (`layered/`)
전통적인 레이어드 아키텍처와 컨트롤러 중심의 구조
- 명확한 계층 분리 (Controller, Service, Repository, Model)
- MVC 패턴 기반
- 간단하고 이해하기 쉬운 구조

### 2. DDD-lite (`ddd-lite/`)
도메인 주도 설계의 핵심 개념을 적용한 경량화된 구조
- 도메인 중심 모델링
- 애그리게이트와 도메인 서비스
- 헥사고날 아키텍처 요소

### 3. Feature-based Modular (`feature-based/`)
기능별 모듈화된 구조
- 기능별 완전한 캡슐화
- 수직적 슬라이싱
- 마이크로서비스 전환 용이

## 다국어 지원

이 CLI 도구는 한국어와 영어를 지원합니다:

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
- [`README.ko.md`](README.ko.md) - 🇰🇷 한국어

## 사용법

```bash
# CLI 도구 설치
pip install -e .

# 새 프로젝트 생성
litestar-boilerplate create --type layered --name my-project
litestar-boilerplate create --type ddd-lite --name my-project
litestar-boilerplate create --type feature-based --name my-project

# 템플릿 목록 보기
litestar-boilerplate list-templates

# 도움말
litestar-boilerplate --help
```

## 요구사항

- Python 3.11+
- Litestar 2.0+
- SQLAlchemy 2.0+
- Alembic
- Pydantic V2

## 개발환경 설정

```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 의존성 설치
pip install -r requirements.txt

# 개발 의존성 설치
pip install -r requirements-dev.txt
```

각 구조별 상세 문서는 해당 디렉토리의 README를 참고하세요.
