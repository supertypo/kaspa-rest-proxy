from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/unban")
async def unban(ip: str):
    """
    Unban a specific peer by it's IP address
    """
    _logger.debug(f"unban: {ip}")
    rpc_client = await kaspad_rpc_client()
    request = {"ip": ip}
    return await wait_for(rpc_client.unban(request), 10)
