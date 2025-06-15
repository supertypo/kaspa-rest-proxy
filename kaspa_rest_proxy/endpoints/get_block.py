from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_block")
async def get_block(hash: str, include_transactions: bool = True):
    """
    Requests info on a block corresponding to a given block hash
    """
    _logger.debug(f"get_block: {get_block}, {include_transactions}")
    rpc_client = await kaspad_rpc_client()
    request = {"hash": hash, "includeTransactions": include_transactions}
    return await wait_for(rpc_client.get_block(request), 10)
