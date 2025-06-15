from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client


import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/ping")
async def ping():
    """
    Ping the node to check if connection is alive
    """
    _logger.debug("ping")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.ping(), 10)
