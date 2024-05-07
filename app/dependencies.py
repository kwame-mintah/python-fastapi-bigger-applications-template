from typing import Type

from app.services.demo_service import DemoService


def get_demo_service() -> Type[DemoService]:
    """
    Dependency injection example.
    :return: DemoService
    """
    return DemoService
