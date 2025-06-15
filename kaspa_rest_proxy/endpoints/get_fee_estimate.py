from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_fee_estimate")
async def get_fee_estimate():
    """
    For all buckets, feerate values represent fee/mass of a transaction in `sompi/gram` units.<br>
    Given a feerate value recommendation, calculate the required fee by
    taking the transaction mass and multiplying it by feerate: `fee = feerate * mass(tx)`
    """
    _logger.debug("get_fee_estimate")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.get_fee_estimate({}), 10)
