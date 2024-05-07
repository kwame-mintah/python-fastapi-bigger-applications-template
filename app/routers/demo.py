from fastapi import APIRouter, Depends, status

from app.services.demo_service import DemoService
from ..dependencies import get_demo_service
from ..models.models import Message

router = APIRouter(prefix="/demo", tags=["dashboard"])


@router.get(
    "/",
    operation_id="demoRoot",
    summary="Demonstrating Bigger Applications",
    response_model=Message,
    status_code=status.HTTP_200_OK,
)
async def root(
    service: DemoService = Depends(get_demo_service()),
) -> Message:
    """
    An example `GET` endpoint to return a response
    :param service:
    :return: Message
    """
    return service.return_stub_data()
