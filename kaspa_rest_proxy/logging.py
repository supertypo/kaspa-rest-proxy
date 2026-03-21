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


_COLOR_FMT = "%(asctime)s [%(log_color)s%(levelname)-8s%(reset)s] %(name)-30.30s - %(message)s"
_PLAIN_FMT = "%(asctime)s [%(levelname)-8s] %(name)-30.30s - %(message)s"
_LOG_COLORS = {
    "DEBUG": "cyan",
    "INFO": "green",
    "WARNING": "yellow",
    "ERROR": "red",
    "CRITICAL": "bold_red",
}


def make_formatter(no_color=False):
    if not no_color and _has_colorlog:
        return ColoredFormatter(fmt=_COLOR_FMT, log_colors=_LOG_COLORS, force_color=True)
    return logging.Formatter(fmt=_PLAIN_FMT)


def setup_logging():
    log_level = LOG_LEVELS[args.log_level]
    handler = logging.StreamHandler()
    formatter = make_formatter(no_color=args.log_no_color)

    handler.setFormatter(formatter)

    # Clear existing handlers to prevent duplicated output or conflict
    root = logging.getLogger()
    root.handlers.clear()
    root.setLevel(log_level)
    root.addHandler(handler)
