import logging

from fastapi import APIRouter, HTTPException

_logger = logging.getLogger(__name__)

router = APIRouter()


@router.get("/get_headers", deprecated=True)
async def get_headers(start_hash: str, limit: int, is_ascending: bool = True):
    """
    Requests headers between the given `start_hash` and the current virtual, up to the given limit

    **Note:** This endpoint is not yet implemented in Kaspad.
    """
    _logger.debug(f"get_headers: {start_hash}, {limit}, {is_ascending}")
    raise HTTPException(status_code=501, detail="Not implemented")
    # rpc_client = await kaspad_rpc_client()
    # request = {
    #     "startHash": start_hash,
    #     "limit": limit,
    #     "isAscending": is_ascending,
    # }
    # return await wait_for(rpc_client.get_headers(request), 10)
