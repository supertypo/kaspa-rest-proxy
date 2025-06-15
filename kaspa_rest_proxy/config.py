import argparse
import os
import sys
from typing import Optional


class Config(argparse.Namespace):
    rpc_url: Optional[str]
    network: str
    base_path: str
    log_level: str
    log_no_color: bool


def parse_args():
    parser = argparse.ArgumentParser(description="REST to Kaspad wRPC Proxy")

    parser.add_argument(
        "-s",
        "--rpc-url",
        help="RPC url to a kaspad instance, e.g 'ws://localhost:17110'. Leave empty to use the Kaspa PNN",
    )
    parser.add_argument("-n", "--network", default="mainnet", help="The network type and suffix, e.g. 'testnet-10'")
    parser.add_argument("-b", "--base-path", default="/", help="Web server base path")
    parser.add_argument(
        "-l",
        "--log-level",
        choices=["critical", "error", "warning", "info", "debug", "notset"],
        default="info",
        help="Set log level",
    )
    parser.add_argument("--log-no-color", action="store_true", help="Disable colored output")
    parser.add_argument(
        "--version", action="version", version=os.getenv("VERSION") or "dev", help="Show program version and exit"
    )

    if "--" in sys.argv:
        idx = sys.argv.index("--")
        app_args = sys.argv[idx + 1 :]
    else:
        app_args = []

    try:
        return parser.parse_args(app_args, namespace=Config())
    except SystemExit:
        sys.exit(1)


args: Config = parse_args()
