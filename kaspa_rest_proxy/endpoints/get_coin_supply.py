from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_coin_supply")
async def get_coinsupply():
    """
    Get current issuance supply
    """
    _logger.debug("get_coin_supply")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.get_coin_supply(), 10)
