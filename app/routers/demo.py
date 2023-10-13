from fastapi import APIRouter, Depends

from app.services.demo_service import DemoService
from ..dependencies import get_demo_service

router = APIRouter(prefix="/demo", tags=["dashboard"])


@router.get("/", operation_id="demoRoot", summary="Demonstrating Bigger Applications")
async def root(
    service: DemoService = Depends(get_demo_service()),
) -> dict:
    return service.return_stub_data()
