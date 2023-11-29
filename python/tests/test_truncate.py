"""Truncation tests."""

# ruff: noqa: S101

from __future__ import annotations

from filecmp import cmp
from typing import TYPE_CHECKING

from rustpy01.truncate import fast_py_truncate_file_lines

if TYPE_CHECKING:
    from pathlib import Path


def test_fast_py_truncate_file_lines(tmp_path: Path) -> None:
    """Test the fast_py_truncate_file_lines() function.

    :param tmp_path: Fixture from pytest for creating a temporary directory
    """
    temp_file = tmp_path / "a.txt"
    temp_file.write_text("123\n456\n78", encoding="utf-8")
    fast_py_truncate_file_lines(temp_file, 2)

    expected_file = tmp_path / "expected.txt"
    expected_file.write_text("123\n456\n", encoding="utf-8")

    assert cmp(temp_file, expected_file)
