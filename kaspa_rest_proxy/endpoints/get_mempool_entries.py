from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_mempool_entries")
async def get_mempool_entries(include_orphan_pool: bool = True, filter_transaction_pool: bool = True):
    """
    Requests information about a specific transaction in the mempool.
    """
    _logger.debug(f"get_mempool_entries: {include_orphan_pool}, {filter_transaction_pool}")
    rpc_client = await kaspad_rpc_client()
    request = {
        "includeOrphanPool": include_orphan_pool,
        "filterTransactionPool": filter_transaction_pool,
    }
    return await wait_for(rpc_client.get_mempool_entries(request), 10)
