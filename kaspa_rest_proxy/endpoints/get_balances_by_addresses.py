from asyncio import wait_for

from fastapi import APIRouter
from fastapi.params import Query, Body

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_balances_by_addresses")
async def get_balances_by_addresses(addresses: str = Query(description="Use comma as separator")):
    """
    Get a balance for a number of addresses
    """
    _logger.debug(f"get_balances_by_addresses: {addresses}")
    rpc_client = await kaspad_rpc_client()
    request = {"addresses": addresses.split(",")}
    return await wait_for(rpc_client.get_balances_by_addresses(request), 10)


@router.post("/get_balances_by_addresses")
async def get_balances_by_addresses_post(addresses: str = Body(embed=False, description="Use comma as separator")):
    """
    Get a balance for a number of addresses
    """
    _logger.debug(f"get_balances_by_addresses_post: {addresses}")
    rpc_client = await kaspad_rpc_client()
    request = {"addresses": addresses.split(",")}
    return await wait_for(rpc_client.get_balances_by_addresses(request), 10)
