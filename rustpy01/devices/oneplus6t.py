"""Code related to a OnePlus 6T."""

from __future__ import annotations

from rustpy01.common import LOSDevice

# class OP6TError(Exception):
#     """Error class unique to OP6T objects."""


class OP6T(LOSDevice):
    """OnePlus 6T object."""

    def __init__(self) -> None:
        """Initialize the OP6T."""
        super().__init__("")

    # @classmethod
    # def main(cls) -> None:
    #     """OP6T main method.
    #     """

    # @staticmethod
    # def create() -> None:
    #     """Build a shell.
    #     """
