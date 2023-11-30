"""Truncation tests."""

# ruff: noqa: S101

from __future__ import annotations

from filecmp import cmp
from typing import TYPE_CHECKING

# pylint: disable=no-name-in-module
from rustpy01._rustpy01 import truncate_file_lines
from rustpy01.truncate import fast_py_truncate_file_lines
from rustpy01.truncate import py_truncate_file_lines

if TYPE_CHECKING:
    from pathlib import Path

DESIRED_ENCODING_A = "utf-8"
EXPECTED_FILE_TEXT_A = "123\n456\n"
EXPECTED_FILENAME_A = "expected_a.txt"
INPUT_TEXT_A = "123\n456\n78"
NUM_OF_LINES_WANTED = 2
NEWLINE_A = "\n"
TEST_FILENAME_A = "a.txt"


def test_py_truncate_file_lines(tmp_path: Path) -> None:
    """Test the py_truncate_file_lines function.

    :param tmp_path: Fixture from pytest for creating a temporary directory
    """
    temp_file_a = tmp_path / TEST_FILENAME_A
    temp_file_a.write_text(INPUT_TEXT_A, encoding=DESIRED_ENCODING_A, newline=NEWLINE_A)
    py_truncate_file_lines(temp_file_a, NUM_OF_LINES_WANTED)

    expected_file_a = tmp_path / EXPECTED_FILENAME_A
    expected_file_a.write_text(
        EXPECTED_FILE_TEXT_A, encoding=DESIRED_ENCODING_A, newline=NEWLINE_A
    )

    assert cmp(temp_file_a, expected_file_a)


def test_fast_py_truncate_file_lines(tmp_path: Path) -> None:
    """Test the fast_py_truncate_file_lines function.

    :param tmp_path: Fixture from pytest for creating a temporary directory
    """
    temp_file_a = tmp_path / TEST_FILENAME_A
    temp_file_a.write_text(INPUT_TEXT_A, encoding=DESIRED_ENCODING_A, newline=NEWLINE_A)
    fast_py_truncate_file_lines(temp_file_a, NUM_OF_LINES_WANTED)

    expected_file_a = tmp_path / EXPECTED_FILENAME_A
    expected_file_a.write_text(
        EXPECTED_FILE_TEXT_A, encoding=DESIRED_ENCODING_A, newline=NEWLINE_A
    )

    assert cmp(temp_file_a, expected_file_a)


def test_truncate_file_lines(tmp_path: Path) -> None:
    """Test the truncate_file_lines Rust function.

    :param tmp_path: Fixture from pytest for creating a temporary directory
    """
    temp_file_a = tmp_path / TEST_FILENAME_A
    temp_file_a.write_text(INPUT_TEXT_A, encoding=DESIRED_ENCODING_A, newline=NEWLINE_A)
    truncate_file_lines(temp_file_a, NUM_OF_LINES_WANTED)

    expected_file_a = tmp_path / EXPECTED_FILENAME_A
    expected_file_a.write_text(
        EXPECTED_FILE_TEXT_A, encoding=DESIRED_ENCODING_A, newline=NEWLINE_A
    )

    assert cmp(temp_file_a, expected_file_a)
