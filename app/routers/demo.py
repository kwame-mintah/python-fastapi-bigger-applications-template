from typing import List

from fastapi import APIRouter, Depends, status

from app.services.demo_service import DemoService
from app.dependencies import get_demo_service
from app.models.models import Message

router = APIRouter(prefix="/demo", tags=["dashboard"])


@router.get(
    path="",
    operation_id="getDemoRoot",
    summary="Demonstrating GET Request",
    response_model=List[Message],
    status_code=status.HTTP_200_OK,
)
async def root(
    service: DemoService = Depends(get_demo_service()),
) -> List[Message]:
    """
    An example `GET` endpoint to return a response
    :param service:
    :return: Message
    """
    return service.return_stub_data()


@router.post(
    path="",
    operation_id="postDemoRoot",
    summary="Demonstrating POST Request",
    response_model=List[Message],
    status_code=status.HTTP_200_OK,
)
async def root(
    message: Message,
    service: DemoService = Depends(get_demo_service()),
) -> List[Message]:
    """
    An example `POST` endpoint to return a response
    :param message:
    :param service:
    :return: Message
    """
    return service.create_additional_stub_data(message)
