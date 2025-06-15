from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/estimate_network_hashes_per_second")
async def estimate_network_hashes_per_second(window_size: int, start_hash: str):
    """ """
    _logger.debug(f"estimate_network_hashes_per_second: {window_size}, {start_hash}")
    rpc_client = await kaspad_rpc_client()
    request = {
        "windowSize": window_size,
        "startHash": start_hash,
    }
    return await wait_for(rpc_client.estimate_network_hashes_per_second(request), 10)
