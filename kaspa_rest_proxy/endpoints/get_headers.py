from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_headers")
async def get_headers(start_hash: str, limit: int, is_ascending: bool = True):
    """
    Requests headers between the given `start_hash` and the current virtual, up to the given limit
    """
    _logger.debug(f"get_headers: {start_hash}, {limit}, {is_ascending}")
    rpc_client = await kaspad_rpc_client()
    request = {
        "startHash": start_hash,
        "limit": limit,
        "isAscending": is_ascending,
    }
    return await wait_for(rpc_client.get_headers(request), 10)
