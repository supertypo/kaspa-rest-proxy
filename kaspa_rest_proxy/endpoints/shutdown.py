from fastapi import APIRouter, HTTPException


import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/shutdown", deprecated=True)
async def shutdown():
    """
    Instructs this node to shut down

    **Note:** This endpoint is not yet implemented.
    """
    _logger.debug("shutdown")
    raise HTTPException(status_code=501, detail="Not implemented")
