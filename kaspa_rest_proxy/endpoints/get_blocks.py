from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_blocks")
async def get_blocks(low_hash: str, include_blocks: bool, include_transactions: bool):
    """
    Requests blocks between a certain block low_hash up to this node's current virtual.
    """
    _logger.debug(f"get_blocks: {low_hash}, {include_blocks}, {include_transactions}")
    rpc_client = await kaspad_rpc_client()
    request = {"lowHash": low_hash, "includeBlocks": include_blocks, "includeTransactions": include_transactions}
    try:
        return await wait_for(rpc_client.get_blocks(request), 60)
    except Exception:
        return {"blockHashes": [], "blocks": []}
