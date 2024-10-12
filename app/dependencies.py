from app.services.demo_service import DemoService


def get_demo_service() -> DemoService:
    """
    Dependency injection example.
    :return: DemoService
    """
    return DemoService()
