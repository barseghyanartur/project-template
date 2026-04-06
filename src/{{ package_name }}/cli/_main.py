"""
{{ project_name }} CLI.

.. TODO: Document your CLI commands here.
"""

from __future__ import annotations

import argparse
import sys


def main() -> int | None:
    """CLI entry point."""
    parser = argparse.ArgumentParser(
        prog="{{ project_name }}",
        description="{{ project_description }}",
    )
    parser.add_argument(
        "input",
        help="Input file or data",
    )
    parser.add_argument(
        "--verbose", "-v",
        action="store_true",
        help="Enable verbose output",
    )

    args = parser.parse_args()

    # TODO: Implement your CLI logic here.
    print(f"Processing: {args.input}")
    if args.verbose:
        print("Verbose mode enabled")

    return 0


if __name__ == "__main__":
    sys.exit(main() or 0)
