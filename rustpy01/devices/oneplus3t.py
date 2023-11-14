"""Code related to a OnePlus 3T."""

from __future__ import annotations

from rustpy01.common import LOSDevice

# class OP3TError(Exception):
#     """Error class unique to OP3T objects."""


class OP3T(LOSDevice):
    """OnePlus 3T object."""

    def __init__(self) -> None:
        """Initialize the OP3T."""
        super().__init__("")

    # @classmethod
    # def main(cls) -> None:
    #     """OP3T main method.
    #     """

    # @staticmethod
    # def create() -> None:
    #     """Build a shell.
    #     """
