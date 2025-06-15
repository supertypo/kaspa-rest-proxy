from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_current_network")
async def get_current_network():
    """
    Requests the network the node is currently running against
    """
    _logger.debug("get_current_network")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.get_current_network(), 10)
