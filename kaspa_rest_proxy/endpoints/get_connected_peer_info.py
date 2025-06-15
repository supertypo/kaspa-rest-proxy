from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_connected_peer_info")
async def get_connected_peer_info():
    """
    Returns a list of the peers currently connected to this Kaspad, along with some statistics on them
    """
    _logger.debug("get_connected_peer_info")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.get_connected_peer_info(), 10)
