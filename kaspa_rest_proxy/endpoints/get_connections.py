from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_connections")
async def get_connections(include_profile_data: bool = True):
    """
    Get current number of active TCP connections
    """
    _logger.debug(f"get_connections: {include_profile_data}")
    rpc_client = await kaspad_rpc_client()
    request = {"includeProfileData": include_profile_data}
    return await wait_for(rpc_client.get_connections(request), 10)
