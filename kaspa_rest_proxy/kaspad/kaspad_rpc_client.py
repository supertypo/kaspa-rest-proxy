import logging
from asyncio import wait_for

from kaspa import RpcClient, Resolver

from kaspa_rest_proxy.config import args

_logger = logging.getLogger(__name__)


async def kaspad_rpc_client() -> RpcClient:
    if not hasattr(kaspad_rpc_client, "client"):
        if args.rpc_url is None:
            kaspad_rpc_client.client = RpcClient(resolver=Resolver(), network_id=args.network)
        else:
            kaspad_rpc_client.client = RpcClient(url=args.rpc_url)

    if not kaspad_rpc_client.client.is_connected:
        try:
            await wait_for(kaspad_rpc_client.client.connect(), 10 if args.rpc_url is None else 5)
            if kaspad_rpc_client.client.is_connected:
                info = await wait_for(kaspad_rpc_client.client.get_block_dag_info(), 10)
                _logger.info(f"Successfully connected to Kaspad {info['network']} ({args.rpc_url or 'resolver'})")
        except Exception:
            pass
        if not kaspad_rpc_client.client.is_connected:
            delattr(kaspad_rpc_client, "client")
            raise RuntimeError(f"Connection to Kaspad ({args.rpc_url}) failed.")

    return kaspad_rpc_client.client
