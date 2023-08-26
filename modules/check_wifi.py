""" check_wifi.py
monitors:   signal strength% of connected wireless network
requires:   nmcli
usage:      /path/to/i3blocks.py --check wifi --warning 40 --critical 20
"""

# import modules
import subprocess
import sys

# import custom modules
try:
    from functions.generic import (
        load_configuration,
        read_configuration,
        perform_check,
        handle_click,
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

# load device status colors
device_disabled = read_configuration(
    conf, "i3blocks", 0, "formatting", 0, "device_disabled"
)

# load click handler
handle_click("check_wifi", 0)


# i3blocks_check function called by i3blocks.py
def i3blocks_check(warning, critical):
    # gather check data
    cmd_signal_strength = "nmcli -f SIGNAL,IN-USE dev wifi"
    proc_signal_strength = subprocess.Popen(
        cmd_signal_strength, shell=True, stdout=subprocess.PIPE
    )
    output_signal_strength = proc_signal_strength.communicate()[0]
    proc_signal_strength.stdout.close()

    lines = output_signal_strength.decode().strip().split("\n")
    signal_strength = next((line.split()[0]
                           for line in lines if "*" in line), None)

    # compare results to thresholds
    if signal_strength is not None:
        check_results = perform_check(
            int(signal_strength),
            "int",
            warning,
            critical,
            "lt",
            color_ok,
            color_warn,
            color_nok,
        )
        color = check_results["color"]
        result = check_results["result"]

        # print output
        print(
            f"{signal_strength}% <span font='FontAwesome' foreground='{color}'>\uf1eb</span>"
        )

    # or print inactive icon
    else:
        print(
            f"<span font='FontAwesome' foreground='{device_disabled}'>\uf1eb</span>")
