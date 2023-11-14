"""Logging code."""

from __future__ import annotations

import logging
import sys


def get_logger(
    name: str,
    fmt: str = (
        "%(asctime)s %(name)-8s %(levelname)-8s {%(module)s} [%(funcName)s] %(message)s"
    ),
    terminator: str = "\n",
) -> logging.Logger:
    """Create a logger allow setting output formats and line terminators.

    :param name: Name of logger
    :param fmt: Format of output message
    :param terminator: Line terminator (Use an empty string "" to log w/o line endings)
    :return: Desired logger object
    """
    # If we use StreamHandler() without specifying sys.stdout, it defaults to sys.stderr
    # By using sys.stdout, stdout on console output should have both stdout & stderr
    handler = logging.StreamHandler(sys.stdout)
    # See https://github.com/python/mypy/issues/2427
    handler.flush = sys.stdout.flush  # type: ignore[method-assign]
    handler.terminator = terminator
    handler.setFormatter(logging.Formatter(fmt=fmt, datefmt="%b %d %H:%M:%S"))

    logger = logging.getLogger(name)
    logger.addHandler(handler)
    logger.propagate = False
    return logger
