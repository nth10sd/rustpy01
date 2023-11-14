"""Place utility functions here."""

from __future__ import annotations

from logging import INFO as INFO_LOG_LEVEL

from rustpy01.util.logging import get_logger

UTIL_RUN_LOG = get_logger(__name__, fmt="%(message)s")
UTIL_RUN_LOG.setLevel(INFO_LOG_LEVEL)


def add_one(inp: int) -> int:
    """Return input added one.

    :param inp: Input number
    :return: Input added one
    """
    UTIL_RUN_LOG.info("Adding one...")
    return inp + 1
