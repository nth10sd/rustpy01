"""Begin running package code."""

from __future__ import annotations

from logging import INFO as INFO_LOG_LEVEL

# pylint: disable=no-name-in-module
from rustpy01._rustpy01 import print_something
from rustpy01._rustpy01 import sum_as_string
from rustpy01.util.logging import get_logger
from rustpy01.util.utils import add_one

RUN_LOG = get_logger(__name__)
RUN_LOG.setLevel(INFO_LOG_LEVEL)


def main() -> None:
    """Start."""
    RUN_LOG.warning(add_one(2))
    RUN_LOG.error("foo")

    RUN_LOG.info("Rust functions below:")
    print_something()
    RUN_LOG.info(sum_as_string(2, 3))
