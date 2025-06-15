import json
import logging
from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.endpoints.submit_transaction import convert_from_legacy_transaction, SubmitTransactionRequest
from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

_logger = logging.getLogger(__name__)


router = APIRouter()


@router.post("/submit_transaction_replacement")
async def submit_transaction_replacement(body: SubmitTransactionRequest):
    """
    Submits a transaction replacement to the mempool, applying a mandatory Replace by Fee policy.
    """
    _logger.debug("submit_transaction_replacement: %s", json.dumps(body.dict(), indent=2))
    rpc_client = await kaspad_rpc_client()
    transaction = convert_from_legacy_transaction(body.transaction)
    request = {"transaction": transaction}
    return await wait_for(rpc_client.submit_transaction_replacement(request), 10)
