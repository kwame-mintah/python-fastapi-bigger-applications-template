from typing import List

from fastapi import APIRouter, Depends, status

from app.services.demo_service import DemoService
from app.dependencies import get_demo_service
from app.models.models import Message

router = APIRouter(prefix="/demo", tags=["demo"])


@router.get(
    path="",
    operation_id="getDemoRoot",
    summary="Demonstrating GET Request",
    response_model=List[Message],
    status_code=status.HTTP_200_OK,
)
async def demo_get(
    service: DemoService = Depends(get_demo_service),
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
async def demo_post(
    message: Message,
    service: DemoService = Depends(get_demo_service),
) -> List[Message]:
    """
    An example `POST` endpoint to return a response
    :param message:
    :param service:
    :return: List of Messages stored
    """
    return service.create_additional_stub_data(message)


@router.delete(
    path="/{message_id}",
    operation_id="deleteDemoRoot",
    summary="Demonstrating DEL Request",
    response_model=None,
    status_code=status.HTTP_204_NO_CONTENT,
)
async def demo_delete(
    message_id: int,
    service: DemoService = Depends(get_demo_service),
) -> None:
    """
    An example `DELETE` endpoint to remove a message from
    stub data
    :param message_id: The `messageId` to delete
    :param service: DemoService
    :return: successfully processed the request
    """
    print(message_id)
    return service.remove_stub_data(message_id)
