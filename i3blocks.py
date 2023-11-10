#!/usr/bin/env python3

# import required modules
import argparse
from importlib import import_module

# define checks and corresponding modules
i3blocks = {
    "load": "check_load",
    "memory": "check_memory",
    "gpu": "check_gpu",
    "time": "check_time",
    "volume": "check_volume",
    "wifi": "check_wifi"
}


def main():
    parser = argparse.ArgumentParser(description="i3blocks control script")
    parser.add_argument("--check", choices=i3blocks.keys(), required=True, help="check to perform")
    parser.add_argument("--warning", type=float, help="warning threshold")
    parser.add_argument("--critical", type=float, help="critical threshold")
    args = parser.parse_args()

    check_module = import_module(f"modules.{i3blocks[args.check]}")
    check_module.i3blocks_check(args.warning, args.critical)


if __name__ == "__main__":
    main()
