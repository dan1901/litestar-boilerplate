"""Litestar Boilerplate Collection.

다양한 프로젝트 구조 패턴을 제공하는 Litestar 보일러플레이트 모음
"""

__version__ = "0.1.0"
__author__ = "Gabriel Ki"
__email__ = "edc1010@gmail.com"

from typing import Final

# 지원하는 템플릿 타입
SUPPORTED_TEMPLATES: Final[list[str]] = [
    "layered",
    "ddd-lite",
    "feature-based",
]

__all__ = [
    "SUPPORTED_TEMPLATES",
    "__author__",
    "__email__",
    "__version__",
]
