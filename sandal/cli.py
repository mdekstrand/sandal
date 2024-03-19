import logging
import sys
from pathlib import Path

import progress_api
from colorlog import ColoredFormatter
from enlighten import Manager

term_fmt = ColoredFormatter(
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

file_fmt = logging.Formatter(
    "[%(asctime)s] %(levelname)-8s %(processName)s %(logger)s %(message)s",
)


def _vrb_to_level(verbose: int | bool | None) -> int:
    if verbose is None:
        verbose = 0
    if verbose is True:
        verbose = 1

    level = logging.INFO
    if verbose < 0:
        level = logging.WARN
    elif verbose > 0:
        level = logging.DEBUG
    return level


def setup_logging(
    verbose: int | bool | None = None,
    log_file: str | Path | None = None,
    log_file_verbose: int | bool | None = None,
):
    """
    Initialize logging for a CLI environment.
    """
    global emgr

    term_level = _vrb_to_level(verbose)

    handler = logging.StreamHandler(stream=sys.stderr)
    handler.setFormatter(term_fmt)
    handler.setLevel(term_level)
    root = logging.getLogger()
    root.addHandler(handler)
    if log_file:
        if log_file_verbose is not None:
            file_level = _vrb_to_level(log_file_verbose)
        else:
            file_level = term_level
        root.setLevel(min(term_level, file_level))
        fh = logging.FileHandler(log_file, mode="w")
        fh.setLevel(file_level)
        fh.setFormatter(file_fmt)
        root.addHandler(fh)
    else:
        root.setLevel(term_level)

    emgr = Manager(stream=sys.stderr)
    progress_api.set_backend("enlighten", emgr)
