import sys

import fastapi
from fastapi import APIRouter
from packaging import version

router = APIRouter(prefix="/version", tags=["versions"])


@router.get("/python", operation_id="pythonVersion", summary="Python version installed")
async def python_version() -> str:
    return str(sys.version_info)


@router.get(
    "/fastapi", operation_id="fastapiVersion", summary="FastAPI version installed"
)
async def fastapi_version() -> str:
    return version.parse(fastapi.__version__).base_version
