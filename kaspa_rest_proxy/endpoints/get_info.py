from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_info")
async def get_info():
    """
    Get generic node information
    """
    _logger.debug("get_info")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.get_info(), 10)
