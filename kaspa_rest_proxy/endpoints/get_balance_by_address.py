from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_balance_by_address")
async def get_balance_by_address(address: str):
    """
    Get a balance for a given address
    """
    _logger.debug(f"get_balance_by_address: {address}")
    rpc_client = await kaspad_rpc_client()
    request = {"address": address}
    return await wait_for(rpc_client.get_balance_by_address(request), 10)
