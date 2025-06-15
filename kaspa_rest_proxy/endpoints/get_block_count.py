from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_block_count")
async def get_block_count():
    """
    Requests the current number of blocks in this node
    """
    _logger.debug("get_block_count")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.get_block_count(), 10)
