from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_sink")
async def get_sink():
    """
    Returns the hash of the current selected tip block of the DAG
    """
    _logger.debug("get_sink")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.get_sink(), 10)
