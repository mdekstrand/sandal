import logging
import sys

import progress_api
from colorlog import ColoredFormatter
from enlighten import Manager

formatter = ColoredFormatter(
    "[%(blue)s%(asctime)s%(reset)s] %(log_color)s%(levelname)-8s%(reset)s %(cyan)s%(logger)s %(blue)s%(message)s",
    datefmt="%H:%M:%S",
    reset=True,
    log_colors={
        "DEBUG": "cyan",
        "INFO": "green",
        "WARNING": "yellow",
        "ERROR": "red",
        "CRITICAL": "red,bg_white",
    },
    secondary_log_colors={},
    style="%",
)


def setup_logging(verbose: int | bool | None = None):
    """
    Initialize logging for a CLI environment.
    """
    global emgr

    if verbose is None:
        verbose = 0
    if verbose is True:
        verbose = 1

    level = logging.INFO
    if verbose < 0:
        level = logging.WARN
    elif verbose > 0:
        level = logging.DEBUG

    handler = logging.StreamHandler(stream=sys.stderr)
    handler.setFormatter(formatter)
    root = logging.getLogger()
    root.setLevel(level)
    root.addHandler(handler)

    emgr = Manager(stream=sys.stderr)
    progress_api.set_backend("enlighten", emgr)
