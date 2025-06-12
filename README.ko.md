<p align="right">
  <a href="README.md">🇺🇸 English</a> |
  <strong>🇰🇷 한국어</strong>
</p>

# Litestar 보일러플레이트 컬렉션

🚀 현대적이고 확장 가능한 Python 웹 애플리케이션을 위한 프로덕션 레디 보일러플레이트

[![CI/CD Pipeline](https://github.com/your-username/litestar-boilerplate/workflows/CI%2FCD%20Pipeline/badge.svg)](https://github.com/your-username/litestar-boilerplate/actions)
[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![Litestar](https://img.shields.io/badge/Litestar-2.0+-green.svg)](https://litestar.dev/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Code style: ruff](https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json)](https://github.com/astral-sh/ruff)
[![Checked with mypy](https://www.mypy-lang.org/static/mypy_badge.svg)](https://mypy-lang.org/)

Litestar 기반의 3가지 프로젝트 구조 보일러플레이트 모음입니다.

## ✨ 주요 특징

- 🏗️ **3가지 아키텍처 패턴**: Layered, DDD-lite, Feature-based 구조 지원
- 🌍 **다국어 CLI**: 한국어/영어 지원으로 글로벌 개발팀 친화적
- ⚡ **즉시 사용 가능**: 완전한 CRUD, 인증, 테스트 구조 포함
- 🔧 **현대적 스택**: Litestar 2.0, SQLAlchemy 2.0, Pydantic V2 기반
- 📚 **풍부한 문서**: 각 아키텍처별 상세 가이드 제공
- 🧪 **테스트 우선**: pytest 기반 완전한 테스트 환경 구성

## 🏛️ 아키텍처 유형

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

## 🚀 사용법

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

## 🌍 다국어 지원

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

## 📋 요구사항

- Python 3.11+
- Litestar 2.0+
- SQLAlchemy 2.0+
- Alembic
- Pydantic V2

## 🛠️ 개발환경 설정

```bash
# 가상환경 생성
python -m venv venv
source venv/bin/activate  # Linux/Mac
# venv\Scripts\activate  # Windows

# 의존성과 개발 의존성 설치
pip install -e ".[dev]"
```

## 🧩 Litestar 관련 리소스

### 📖 공식 문서 및 리포지토리
- [**Litestar 공식 문서**](https://docs.litestar.dev/) - 완전한 API 문서와 가이드
- [**Litestar GitHub**](https://github.com/litestar-org/litestar) - 메인 리포지토리
- [**Litestar Fullstack 예제**](https://github.com/litestar-org/litestar-fullstack) - 실제 프로덕션 예제

### 🎓 학습 자료
- [**Awesome Litestar**](https://github.com/litestar-org/awesome-litestar) - 큐레이션된 Litestar 리소스 모음
- [**Litestar 튜토리얼**](https://docs.litestar.dev/latest/tutorials/) - 단계별 학습 가이드
- [**Litestar 예제 모음**](https://github.com/litestar-org/litestar/tree/main/docs/examples) - 다양한 사용 사례 예제

### 🛠️ 도구 및 플러그인
- [**Litestar CLI**](https://docs.litestar.dev/latest/usage/cli/) - 강력한 명령줄 도구
- [**Advanced Alchemy**](https://github.com/litestar-org/advanced-alchemy) - SQLAlchemy 확장
- [**Litestar Users**](https://github.com/litestar-org/litestar-users) - 사용자 관리 플러그인

## 📚 상세 문서

각 구조별 상세 문서와 예제는 해당 디렉토리의 README를 참고하세요.

## 🤝 기여하기

이 프로젝트에 기여하고 싶으시다면 이슈를 생성하거나 풀 리퀘스트를 보내주세요. 모든 기여를 환영합니다!

## 📄 라이선스

이 프로젝트는 MIT 라이선스 하에 배포됩니다.
