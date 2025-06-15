from asyncio import wait_for

from fastapi import APIRouter
from fastapi.params import Query, Body

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_mempool_entries_by_addresses")
async def get_mempool_entries_by_addresses(
    addresses: str = Query(description="Use comma as separator"),
    include_orphan_pool: bool = True,
    filter_transaction_pool: bool = True,
):
    """
    Get a list of mempool entries that belong to specific addresses
    """
    _logger.debug(f"get_mempool_entries_by_addresses: {addresses}, {include_orphan_pool}, {filter_transaction_pool}")
    rpc_client = await kaspad_rpc_client()
    request = {
        "addresses": addresses.split(","),
        "includeOrphanPool": include_orphan_pool,
        "filterTransactionPool": filter_transaction_pool,
    }
    return await wait_for(rpc_client.get_mempool_entries(request), 10)


@router.post("/get_mempool_entries_by_addresses")
async def get_mempool_entries_by_addresses_post(
    addresses: str = Body(embed=False, description="Use comma as separator"),
    include_orphan_pool: bool = True,
    filter_transaction_pool: bool = True,
):
    """
    Get a list of mempool entries that belong to specific addresses
    """
    _logger.debug(
        f"get_mempool_entries_by_addresses_post: {addresses}, {include_orphan_pool}, {filter_transaction_pool}"
    )
    rpc_client = await kaspad_rpc_client()
    request = {
        "addresses": addresses.split(","),
        "includeOrphanPool": include_orphan_pool,
        "filterTransactionPool": filter_transaction_pool,
    }
    return await wait_for(rpc_client.get_mempool_entries(request), 10)
