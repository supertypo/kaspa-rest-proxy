from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_server_info")
async def get_server_info():
    """
    Get state information on the node
    """
    _logger.debug("get_server_info")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.get_server_info(), 10)
