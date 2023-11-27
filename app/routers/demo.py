from fastapi import APIRouter, Depends

from app.services.demo_service import DemoService
from ..dependencies import get_demo_service
from ..models.models import Message

router = APIRouter(prefix="/demo", tags=["dashboard"])


@router.get(
    "/",
    operation_id="demoRoot",
    summary="Demonstrating Bigger Applications",
    response_model=Message,
)
async def root(
    service: DemoService = Depends(get_demo_service()),
) -> Message:
    return service.return_stub_data()
