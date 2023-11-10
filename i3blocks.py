#!/usr/bin/env python3

# import required modules
import argparse
from importlib import import_module

# define a dictionary mapping i3blocks indicators to their corresponding module names
i3blocks = {
    "gpu": "check_gpu",
    "load": "check_load",
    "memory": "check_memory",
    "time": "check_time",
    "volume": "check_volume",
    "wifi": "check_wifi"
}

# define the main function for handling command-line arguments and invoking module checks
def main():
    # create an argument parser
    parser = argparse.ArgumentParser(description="i3blocks control script")

    # define command-line arguments
    parser.add_argument("--check", choices=i3blocks.keys(), required=True, help="check to perform")
    parser.add_argument("--warning", type=float, help="warning threshold")
    parser.add_argument("--critical", type=float, help="critical threshold")

    # parse command-line arguments
    args = parser.parse_args()

    # import the module dynamically based on the specified check and invoke its i3blocks_check function
    check_module = import_module(f"modules.{i3blocks[args.check]}")
    check_module.i3blocks_check(args.warning, args.critical)

# entry point to the script
if __name__ == "__main__":
    main()
