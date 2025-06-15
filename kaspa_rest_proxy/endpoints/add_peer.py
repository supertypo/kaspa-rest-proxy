import logging
from asyncio import wait_for

from fastapi import APIRouter

from kaspa_rest_proxy.kaspad.kaspad_rpc_client import kaspad_rpc_client

_logger = logging.getLogger(__name__)


router = APIRouter()


@router.get("/add_peer")
async def add_peer(peer_address: str, is_permanent: bool = True):
    """
    Adds a peer to the node's outgoing connection list
    """
    _logger.debug(f"add_peer: {peer_address}, {is_permanent}")
    rpc_client = await kaspad_rpc_client()
    request = {
        "peerAddress": {"ip": peer_address.split(":")[0], "port": int(peer_address.split(":")[1])},
        "isPermanent": is_permanent,
    }
    return await wait_for(rpc_client.add_peer(request), 10)
