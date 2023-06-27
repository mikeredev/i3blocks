#!/usr/bin/env python3
"""
i3blocks.py
desc:         A script for controlling i3blocks and performing checks.
usage:        python i3blocks.py [--check CHECK] [--warning WARNING] [--critical CRITICAL] [--compare COMPARE] [--datatype DATATYPE]
requirements: argparse, importlib
function:     This script allows you to control i3blocks and perform checks by specifying the check to be performed, along with optional warning and critical thresholds, comparison type, and data type.
arguments:
    --check CHECK: The check to perform. Available options are 'battery', 'gpu', 'media', 'memory', 'perf', 'time', and 'wifi'.
    --warning WARNING: The warning threshold for the check.
    --critical CRITICAL: The critical threshold for the check.
    --compare COMPARE: The type of comparison to perform. Available options are 'lt' (less than) and 'gt' (greater than).
    --datatype DATATYPE: The data type to use for comparisons. Available options are 'int' and 'float'.
returns:      None
notes:        The script loads the specified module from the 'modules' package and calls its 'i3blocks_check' function, passing the provided arguments. If an error occurs, the exception is printed.
example:      python i3blocks.py --check battery --warning 20 --critical 10
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
