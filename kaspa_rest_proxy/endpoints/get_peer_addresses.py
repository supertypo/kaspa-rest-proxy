from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_peer_addresses")
async def get_peer_addresses():
    """
    Returns a list of all the addresses (IP, port) this Kaspad knows
    and a list of all addresses that are currently banned by this Kaspad
    """
    _logger.debug("get_peer_addresses")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.get_peer_addresses(), 10)
