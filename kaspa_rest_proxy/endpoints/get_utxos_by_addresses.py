from asyncio import wait_for

from fastapi import APIRouter, Query, Body

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_utxos_by_addresses")
async def get_utxos_by_addresses(addresses: str = Query(description="Use comma as separator")):
    """
    Requests all current UTXOs for the given node addresses
    """
    _logger.debug(f"get_utxos_by_addresses: {addresses}")
    rpc_client = await kaspad_rpc_client()
    request = {"addresses": addresses.split(",")}
    return await wait_for(rpc_client.get_utxos_by_addresses(request), 60)


@router.post("/get_utxos_by_addresses")
async def get_utxos_by_addresses_post(addresses: str = Body(embed=False, description="Use comma as separator")):
    """
    Requests all current UTXOs for the given node addresses
    """
    _logger.debug(f"get_utxos_by_addresses_post: {addresses}")
    rpc_client = await kaspad_rpc_client()
    request = {"addresses": addresses.split(",")}
    return await wait_for(rpc_client.get_utxos_by_addresses(request), 60)
