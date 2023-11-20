"""
CLI for VaxCollapse.

Copyright 2023 Aleksander Pałkowski.
"""

import argparse

from vaxcollapse import vaxcollapse

if __name__ == "__main__":
    description = "VaxCollapse: A framework for specific design of mRNA vaccine targets"
    parser = argparse.ArgumentParser(description=description)

    parser.add_argument(
        "--number",
        type=int,
        required=True,
        metavar="INT",
        help="Some number, I don't know",
    )
    parser.add_argument("--verbose", action="store_true", help="Set verbose mode")

    args = parser.parse_args()

    vaxcollapse(args.number, verbose=args.verbose)
