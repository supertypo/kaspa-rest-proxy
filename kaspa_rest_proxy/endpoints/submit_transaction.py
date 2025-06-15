import json
import logging
from asyncio import wait_for
from typing import List

from fastapi import APIRouter
from kaspa import (
    Transaction,
    TransactionInput,
    TransactionOutpoint,
    TransactionOutput,
    ScriptPublicKey,
    Hash,
)
from pydantic import BaseModel

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

_logger = logging.getLogger(__name__)


router = APIRouter()


class SubmitTxOutpoint(BaseModel):
    transactionId: str
    index: int


class SubmitTxInput(BaseModel):
    previousOutpoint: SubmitTxOutpoint
    signatureScript: str
    sequence: int
    sigOpCount: int


class SubmitTxScriptPublicKey(BaseModel):
    version: int
    scriptPublicKey: str


class SubmitTxOutput(BaseModel):
    amount: int
    scriptPublicKey: SubmitTxScriptPublicKey


class SubmitTxModel(BaseModel):
    version: int
    inputs: List[SubmitTxInput]
    outputs: List[SubmitTxOutput]
    lockTime: int | None
    subnetworkId: str | None
    gas: int | None
    payload: str | None
    mass: int | None


class SubmitTransactionRequest(BaseModel):
    transaction: SubmitTxModel
    allowOrphan: bool = False


class SubmitTransactionResponse(BaseModel):
    transactionId: str | None
    error: str | None


@router.post("/submit_transaction")
async def submit_transaction(body: SubmitTransactionRequest):
    """
    Submits a transaction to the mempool
    """
    _logger.debug("submit_transaction: %s", json.dumps(body.dict(), indent=2))
    rpc_client = await kaspad_rpc_client()
    transaction = convert_from_legacy_transaction(body.transaction)
    request = {"allow_orphan": body.allowOrphan, "transaction": transaction}
    return await wait_for(rpc_client.submit_transaction(request), 10)


def convert_from_legacy_transaction(transaction: SubmitTxModel) -> Transaction | None:
    if not transaction:
        return None
    return Transaction(
        transaction.version,
        [
            TransactionInput(
                TransactionOutpoint(Hash(i.previousOutpoint.transactionId), i.previousOutpoint.index),
                i.signatureScript,
                i.sequence,
                i.sigOpCount,
            )
            for i in transaction.inputs
        ],
        [
            TransactionOutput(o.amount, ScriptPublicKey(o.scriptPublicKey.version, o.scriptPublicKey.scriptPublicKey))
            for o in transaction.outputs
        ],
        transaction.lockTime or 0,
        transaction.subnetworkId or "0000000000000000000000000000000000000000",
        transaction.gas or 0,
        transaction.payload or "",
        transaction.mass or 0,
    )
