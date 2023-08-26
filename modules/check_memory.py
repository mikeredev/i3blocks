""" check_memory.py
monitors:   RAM utilization%
requires:   psutil
usage:      /path/to/i3blocks.py --check memory --warning 70 --critical 90
"""

# import modules
import psutil
import sys

# import custom modules
try:
    from functions.generic import (
        load_configuration,
        read_configuration,
        perform_check,
    )
except:
    print(f"Failed to load custom modules. Call this script via i3blocks.py only.")
    sys.exit(1)

# load configuration file
conf = load_configuration()
color_ok = read_configuration(conf, "i3blocks", 0, "formatting", 0, "color_ok")
color_warn = read_configuration(
    conf, "i3blocks", 0, "formatting", 0, "color_warn")
color_nok = read_configuration(
    conf, "i3blocks", 0, "formatting", 0, "color_nok")


# i3blocks_check function called by i3blocks.py
def i3blocks_check(warning, critical):
    # gather check data
    memory_utilization = round(psutil.virtual_memory().percent)

    # compare results to thresholds
    check_results = perform_check(
        memory_utilization,
        "int",
        warning,
        critical,
        "gt",
        color_ok,
        color_warn,
        color_nok,
    )
    color = check_results["color"]
    result = check_results["result"]

    # print output
    icon = f"<span font='FontAwesome' foreground='{color}'>\uf201</span>"
    print(f"{memory_utilization}% {icon}")
