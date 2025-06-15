import logging
from kaspa_rest_proxy.config import args

try:
    from colorlog import ColoredFormatter

    _has_colorlog = True
except ImportError:
    _has_colorlog = False

LOG_LEVELS = {
    "critical": logging.CRITICAL,
    "error": logging.ERROR,
    "warning": logging.WARNING,
    "info": logging.INFO,
    "debug": logging.DEBUG,
}


def setup_logging():
    log_level = LOG_LEVELS[args.log_level]
    handler = logging.StreamHandler()

    if not args.log_no_color and _has_colorlog:
        formatter = ColoredFormatter(
            fmt="%(asctime)s [%(log_color)s%(levelname)-8s%(reset)s] %(name)-30.30s - %(message)s",
            log_colors={
                "DEBUG": "cyan",
                "INFO": "green",
                "WARNING": "yellow",
                "ERROR": "red",
                "CRITICAL": "bold_red",
            },
            force_color=True,
        )
    else:
        formatter = logging.Formatter(fmt="%(asctime)s [%(levelname)-8s] %(name)-30.30s - %(message)s")

    handler.setFormatter(formatter)

    # Clear existing handlers to prevent duplicated output or conflict
    root = logging.getLogger()
    root.handlers.clear()
    root.setLevel(log_level)
    root.addHandler(handler)
