from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_utxo_return_address")
async def get_utxo_return_address(txid: str, accepting_block_daa_score: int):
    """
    Get UTXO Return Addresses
    """
    _logger.debug(f"get_utxo_return_address: {txid}, {accepting_block_daa_score}")
    rpc_client = await kaspad_rpc_client()
    request = {"txid": txid, "acceptingBlockDaaScore": accepting_block_daa_score}
    return await wait_for(rpc_client.get_utxo_return_address(request), 10)
