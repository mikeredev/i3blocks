#!/usr/bin/env python3
import argparse
from importlib import import_module

CHECK_MODULES = {
    "battery": "check_battery",
    "brightness": "check_brightness",
    "gpu": "check_gpu",
    "load": "check_load",
    "memory": "check_memory",
    "time": "check_time",
    "volume": "check_volume",
    "wifi": "check_wifi",
}


def main():
    parser = argparse.ArgumentParser(description="i3blocks control script")
    parser.add_argument(
        "--check", choices=CHECK_MODULES.keys(), required=True, help="check to perform"
    )
    parser.add_argument("--warning", type=float, help="warning threshold")
    parser.add_argument("--critical", type=float, help="critical threshold")
    parser.add_argument("--compare", choices=["lt", "gt"], help="comparison")
    parser.add_argument("--datatype", choices=["int", "float"], help="int or float")
    args = parser.parse_args()

    try:
        check_module = import_module(f"modules.{CHECK_MODULES[args.check]}")
        check_module.check(args.warning, args.critical)
    except (ImportError, AttributeError) as e:
        print(f"Check failed: {e}")


if __name__ == "__main__":
    main()
