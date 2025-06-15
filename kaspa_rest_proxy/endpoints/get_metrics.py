from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_metrics")
async def get_metrics(
    process_metrics: bool = True,
    connection_metrics: bool = True,
    bandwidth_metrics: bool = True,
    consensus_metrics: bool = True,
    storage_metrics: bool = True,
    custom_metrics: bool = True,
):
    """
    Get metrics for consensus information and node performance
    """
    _logger.debug(
        "get_metrics: "
        f"{process_metrics}, {connection_metrics}, {bandwidth_metrics}, "
        f"{consensus_metrics}, {storage_metrics}, {custom_metrics}"
    )
    rpc_client = await kaspad_rpc_client()
    request = {
        "processMetrics": process_metrics,
        "connectionMetrics": connection_metrics,
        "bandwidthMetrics": bandwidth_metrics,
        "consensusMetrics": consensus_metrics,
        "storageMetrics": storage_metrics,
        "customMetrics": custom_metrics,
    }
    return await wait_for(rpc_client.get_metrics(request), 10)
