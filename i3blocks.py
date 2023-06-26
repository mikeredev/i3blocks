#!/usr/bin/env python3
""" i3blocks.py
usage:  i3blocks.py [-h] --check {time,gpu,perf,memory,wifi,media} [--warning WARNING] [--critical CRITICAL] [--compare {lt,gt}] [--datatype {int,float}]
options:
    -h, --help                                show this help message and exit
    --check {time,gpu,perf,memory,wifi,media} check to perform
    --warning WARNING                         warning threshold
    --critical CRITICAL                       critical threshold
    --compare {lt,gt}                         comparison
    --datatype {int,float}                    int or float
"""

# import modules
import argparse
from importlib import import_module

# define modules/check_name.py
i3blocks = {
    "battery": "check_battery",
    "gpu": "check_gpu",
    "media": "check_media",
    "memory": "check_memory",
    "perf": "check_perf",
    "time": "check_time",
    "wifi": "check_wifi",
}


def main():
    # setup argparse
    parser = argparse.ArgumentParser(description="i3blocks control script")
    parser.add_argument(
        "--check", choices=i3blocks.keys(), required=True, help="check to perform"
    )
    parser.add_argument("--warning", type=float, help="warning threshold")
    parser.add_argument("--critical", type=float, help="critical threshold")
    parser.add_argument("--compare", choices=["lt", "gt"], help="comparison")
    parser.add_argument("--datatype", choices=["int", "float"], help="int or float")
    args = parser.parse_args()

    # remove the try/catch if debugging
    try:
        # load the module called in the argument
        check_module = import_module(f"modules.{i3blocks[args.check]}")

        # call the module's `i3blocks_check` function
        check_module.i3blocks_check(args.warning, args.critical)
    except Exception as e:
        print(f"{args.check}: {e}")


if __name__ == "__main__":
    main()
