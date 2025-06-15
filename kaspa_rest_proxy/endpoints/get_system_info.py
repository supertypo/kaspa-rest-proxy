from fastapi import APIRouter, HTTPException


import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_system_info", deprecated=True)
async def get_system_info():
    """
    Get system information (RAM available, number of cores, available file descriptors)

    **Note:** This endpoint is not yet implemented.
    """
    _logger.debug("get_system_info")
    raise HTTPException(status_code=501, detail="Not implemented")
    # rpc_client = await kaspad_rpc_client()
    # return await wait_for(rpc_client.get_system_info(), 10)
