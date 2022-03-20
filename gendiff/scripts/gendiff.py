# -*- coding: utf-8 -*-

import argparse

from gendiff import generate_diff


def main():
    parser = argparse.ArgumentParser(description="Generate diff")
    parser.add_argument("first_file", type=str)
    parser.add_argument("second_file", type=str)
    parser.add_argument(
        "-f", "--format", default="stylish", help="set format of output", type=str
    )
    args = parser.parse_args()

    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == "__main__":
    main()
