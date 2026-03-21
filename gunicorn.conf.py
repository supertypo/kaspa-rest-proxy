import logging

from kaspa_rest_proxy.config import args
from kaspa_rest_proxy.logging import make_formatter


def on_starting(server):
    """Re-apply the colorlog formatter to gunicorn's own loggers."""
    formatter = make_formatter(no_color=args.log_no_color)
    for name in ("gunicorn.error", "gunicorn.access"):
        for handler in logging.getLogger(name).handlers:
            handler.setFormatter(formatter)
