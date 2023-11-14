"""Sample code involving truncation."""

from collections import deque
from itertools import islice
from pathlib import Path
from typing import TYPE_CHECKING
from typing import Any

# pylint: disable=no-name-in-module
from rustpy01._rustpy01 import truncate_file_lines

if TYPE_CHECKING:
    from collections.abc import Callable
    from collections.abc import Iterable


def py_truncate_file_lines(filename: Path | str, lines: int) -> None:
    """Truncate files to the desired number of lines.

    Adapted from https://stackoverflow.com/a/27672002

    :param filename: Filename of file to truncate
    :param lines: Desired number of lines to retain
    """
    with Path(filename).open("r+", encoding="utf-8", errors="surrogateescape") as f:
        blackhole: Callable[[Iterable[Any]], None] = deque((), 0).extend
        file_iterator = iter(f.readline, "")
        blackhole(islice(file_iterator, lines))
        f.truncate(f.tell())


def sample_truncation() -> None:
    """Sample truncation."""
    root_folder = Path(__file__).parents[2]
    desired_file = root_folder / "pydocs-v3pt12-210-copies-over-23M-lines.txt"

    if desired_file.is_file():
        # Swap this with py_truncate_file_lines or vice versa
        truncate_file_lines(desired_file, 1000000)


sample_truncation()
