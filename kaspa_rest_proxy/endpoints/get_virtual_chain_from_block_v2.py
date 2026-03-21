from asyncio import wait_for
from enum import Enum
from typing import Optional

from fastapi import APIRouter, Query

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


class DataVerbosityLevel(str, Enum):
    none = "None"
    low = "Low"
    high = "High"
    full = "Full"


@router.get("/get_virtual_chain_from_block_v2")
async def get_virtual_chain_from_block_v2(
    start_hash: str = Query(description="The block hash to start the virtual chain traversal from."),
    data_verbosity_level: Optional[DataVerbosityLevel] = Query(
        default=None,
        description=(
            "Controls how much data is populated in each chainBlockAcceptedTransactions entry.\n\n"
            "- **None** (default): only block hashes; no header or transaction fields.\n\n"
            "- **Low**: chain block header includes version, timestamp, bits, nonce, DAA score, blue work, blue score; "
            "accepted transactions include transaction ID, block hash, block time, hash, output amounts, output script public keys, "
            "input signature scripts, verbose data (script public key type/address, compute mass).\n\n"
            "- **High**: everything in Low, plus header includes parents-by-level, hash merkle root, accepted ID merkle root; "
            "transactions include payload, mass, input sequence, sig op count, previous outpoint, input UTXO amount/script/is-coinbase.\n\n"
            "- **Full**: everything in High, plus header includes UTXO commitment and pruning point; "
            "transactions include version, lock time, subnetwork ID, gas, and UTXO entry DAA score."
        ),
    ),
    min_confirmation_count: Optional[int] = Query(
        default=None,
        description="Minimum number of confirmations a block must have to be included in the response. Omit to return all blocks.",
    ),
):
    """
    Requests the virtual selected parent chain from some start_hash to this node's current virtual (v2).
    """
    _logger.debug(f"get_virtual_chain_from_block_v2: {start_hash}, {data_verbosity_level}, {min_confirmation_count}")
    rpc_client = await kaspad_rpc_client()
    request = {
        "startHash": start_hash,
        "dataVerbosityLevel": data_verbosity_level.value if data_verbosity_level is not None else None,
        "minConfirmationCount": min_confirmation_count,
    }
    return await wait_for(rpc_client.get_virtual_chain_from_block_v2(request), 120)
