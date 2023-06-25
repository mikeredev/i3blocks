#!/usr/bin/env python3
# requires chmod +x
# v2
import argparse
from importlib import import_module

i3blocks = {
    "time": "check_time",
    "gpu": "check_gpu",
    "perf": "check_perf",
    "memory": "check_memory",
    "wifi": "check_wifi",
    "media": "check_media",
}


def main():
    parser = argparse.ArgumentParser(description="i3blocks control script")
    parser.add_argument(
        "--check", choices=i3blocks.keys(), required=True, help="check to perform"
    )
    parser.add_argument("--warning", type=float, help="warning threshold")
    parser.add_argument("--critical", type=float, help="critical threshold")
    parser.add_argument("--compare", choices=["lt", "gt"], help="comparison")
    parser.add_argument("--datatype", choices=["int", "float"], help="int or float")
    args = parser.parse_args()

    try:
        check_module = import_module(f"modules.{i3blocks[args.check]}")
        check_module.i3blocks_check(args.warning, args.critical)
    except Exception as e:
        print(f"{args.check}: {e}")


if __name__ == "__main__":
    main()
