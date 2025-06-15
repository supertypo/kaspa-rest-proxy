from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_current_block_color")
async def get_current_block_color(hash: str):
    """
    Block color determination by iterating DAG
    """
    _logger.debug(f"get_current_block_color: {hash}")
    rpc_client = await kaspad_rpc_client()
    request = {"hash": hash}
    return await wait_for(rpc_client.get_current_block_color(request), 10)
