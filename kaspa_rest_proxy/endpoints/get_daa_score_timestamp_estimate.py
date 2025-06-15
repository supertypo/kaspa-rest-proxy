from asyncio import wait_for

from fastapi import APIRouter
from fastapi.params import Query, Body

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_daa_score_timestamp_estimate")
async def get_daa_score_timestamp_estimate(
    daa_scores: str = Query(description="Use comma as separator"),
):
    """
    Get DAA Score timestamp estimate
    """
    _logger.debug(f"get_daa_score_timestamp_estimate: {daa_scores}")
    rpc_client = await kaspad_rpc_client()
    request = {"daaScores": [int(d) for d in daa_scores.split(",")]}
    return await wait_for(rpc_client.get_daa_score_timestamp_estimate(request), 10)


@router.post("/get_daa_score_timestamp_estimate")
async def get_daa_score_timestamp_estimate_post(
    daa_scores: str = Body(embed=False, description="Use comma as separator"),
):
    """
    Get DAA Score timestamp estimate
    """
    _logger.debug(f"get_daa_score_timestamp_estimate_post: {daa_scores}")
    rpc_client = await kaspad_rpc_client()
    request = {"daaScores": [int(d) for d in daa_scores.split(",")]}
    return await wait_for(rpc_client.get_daa_score_timestamp_estimate(request), 10)
