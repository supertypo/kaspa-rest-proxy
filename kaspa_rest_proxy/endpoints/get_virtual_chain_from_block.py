from asyncio import wait_for

from fastapi import APIRouter, Query

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_virtual_chain_from_block")
async def get_virtual_chain_from_block(
    start_hash: str = Query(description="The block hash to start the virtual chain traversal from."),
    include_accepted_transaction_ids: bool = Query(
        default=True,
        description="Whether to include the accepted transaction IDs for each added chain block in the response.",
    ),
    min_confirmation_count: int | None = Query(
        default=None,
        description="Minimum number of confirmations a block must have to be included in the response. Omit to return all blocks.",
    ),
):
    """
    Requests the virtual selected parent chain from some start_hash to this node's current virtual
    """
    _logger.debug(f"get_virtual_chain_from_block: {start_hash}, {include_accepted_transaction_ids}, {min_confirmation_count}")
    rpc_client = await kaspad_rpc_client()
    request = {
        "startHash": start_hash,
        "includeAcceptedTransactionIds": include_accepted_transaction_ids,
        "minConfirmationCount": min_confirmation_count,
    }
    return await wait_for(rpc_client.get_virtual_chain_from_block(request), 60)
