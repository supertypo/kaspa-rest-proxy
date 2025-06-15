from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_sync_status")
async def get_sync_status():
    """
    Get the current sync status of the node
    """
    _logger.debug("get_sync_status")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.get_sync_status(), 10)
