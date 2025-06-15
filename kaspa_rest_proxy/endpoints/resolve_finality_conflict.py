from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/resolve_finality_conflict")
async def resolve_finality_conflict(finality_block_hash: str):
    """ """
    _logger.debug(f"resolve_finality_conflict: {finality_block_hash}")
    rpc_client = await kaspad_rpc_client()
    request = {"finalityBlockHash": finality_block_hash}
    return await wait_for(rpc_client.resolve_finality_conflict(request), 10)
