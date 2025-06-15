from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client


import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_block_dag_info")
async def get_block_dag_info():
    """
    Returns info on the current state of the DAG
    """
    _logger.debug("get_block_dag_info")
    rpc_client = await kaspad_rpc_client()
    return await wait_for(rpc_client.get_block_dag_info(), 10)
