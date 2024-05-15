import sys

import fastapi
from fastapi import APIRouter, status
from packaging import version

from app.models.models import Package

router = APIRouter(prefix="/version", tags=["versions"])


@router.get(
    "/python",
    operation_id="pythonVersion",
    summary="Python version installed",
    response_model=Package,
    status_code=status.HTTP_200_OK,
)
async def python_version() -> Package:
    """
    Get the Python version on the host machine.
    :return: Python version
    """
    return Package(version=str(sys.version_info))


@router.get(
    "/fastapi",
    operation_id="fastapiVersion",
    summary="FastAPI version installed",
    response_model=Package,
    status_code=status.HTTP_200_OK,
)
async def fastapi_version() -> Package:
    """
    Get the FastAPI version installed.
    :return: FastAPI version
    """
    return Package(version=version.parse(fastapi.__version__).base_version)
