from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_virtual_chain_from_block")
async def get_virtual_chain_from_block(start_hash: str, include_accepted_transaction_ids: bool = True):
    """
    Requests the virtual selected parent chain from some start_hash to this node's current virtual
    """
    _logger.debug(f"get_virtual_chain_from_block: {start_hash}, {include_accepted_transaction_ids}")
    rpc_client = await kaspad_rpc_client()
    request = {"startHash": start_hash, "includeAcceptedTransactionIds": include_accepted_transaction_ids}
    return await wait_for(rpc_client.get_virtual_chain_from_block(request), 60)
