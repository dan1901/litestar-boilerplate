"""제너레이터 팩토리 클래스."""

from typing import TYPE_CHECKING, ClassVar

from .ddd_lite import DddLiteGenerator
from .feature_based import FeatureBasedGenerator
from .layered import LayeredGenerator

if TYPE_CHECKING:
    from .base import BaseGenerator


class GeneratorFactory:
    """프로젝트 구조 제너레이터 팩토리."""

    _generators: ClassVar[dict[str, type["BaseGenerator"]]] = {
        "layered": LayeredGenerator,
        "ddd-lite": DddLiteGenerator,
        "feature-based": FeatureBasedGenerator,
    }

    @classmethod
    def create(cls, template_type: str) -> "BaseGenerator":
        """템플릿 타입에 따라 적절한 제너레이터를 생성합니다.

        Args:
            template_type: 생성할 템플릿 타입

        Returns:
            해당 타입의 제너레이터 인스턴스

        Raises:
            ValueError: 지원하지 않는 템플릿 타입인 경우
        """
        if template_type not in cls._generators:
            available = ", ".join(cls._generators.keys())
            raise ValueError(f"지원하지 않는 템플릿 타입: {template_type}. 사용 가능한 타입: {available}")

        generator_class = cls._generators[template_type]
        return generator_class()

    @classmethod
    def get_available_types(cls) -> list[str]:
        """사용 가능한 템플릿 타입 목록을 반환합니다."""
        return list(cls._generators.keys())
