import logging
from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/shutdown")
async def shutdown():
    """
    Instructs this node to shut down
    """
    _logger.debug("shutdown")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.shutdown(), 10)
