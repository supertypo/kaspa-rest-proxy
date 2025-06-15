from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_subnetwork")
async def get_subnetwork(subnetwork_id: str):
    """
    Requests information about a specific subnetwork
    """
    _logger.debug(f"get_subnetwork: {subnetwork_id}")
    rpc_client = await kaspad_rpc_client()
    request = {"subnetworkId": subnetwork_id}
    return await wait_for(rpc_client.get_subnetwork(request), 10)
