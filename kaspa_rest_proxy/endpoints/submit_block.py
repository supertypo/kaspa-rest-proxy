from fastapi import APIRouter, HTTPException


import logging

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/submit_block", deprecated=True)
async def submit_block():
    """
    Extracts a block out of the request message and attempts to add it to the DAG

    **Note:** This endpoint is not yet implemented.
    """
    _logger.debug("submit_block")
    raise HTTPException(status_code=501, detail="Not implemented")
    # rpc_client = await kaspad_rpc_client()
    # return await wait_for(rpc_client.submit_block(), 10)
