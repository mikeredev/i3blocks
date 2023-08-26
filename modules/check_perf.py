""" check_perf.py
monitors:   CPU load
optional:   fan speed
requires:   nvidia-smi
usage:      /path/to/i3blocks.py --check perf --warning 0.7 --critical 1.0
"""

# import modules
import os
import subprocess
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

# load device status colors
device_disabled = read_configuration(
    conf, "i3blocks", 0, "formatting", 0, "device_disabled"
)
device_inactive = read_configuration(
    conf, "i3blocks", 0, "formatting", 0, "device_inactive"
)
device_active_low = read_configuration(
    conf, "i3blocks", 0, "formatting", 0, "device_active_low"
)
device_active_high = read_configuration(
    conf, "i3blocks", 0, "formatting", 0, "device_active_high"
)

# load check specifics from configuration file
fan_present = read_configuration(conf, "i3blocks", 0, "perf", 0, "fan_present")
fan_type = read_configuration(conf, "i3blocks", 0, "perf", 0, "fan_type")


def get_fan_speed(fan_type):
    if fan_type.lower() == "nvidia":
        # Run nvidia-smi and return fan speed% as integer
        cmd_fan_speed = (
            "nvidia-smi --query-gpu=fan.speed --format=csv,noheader | sed 's/ \+%//'"
        )
        proc_fan_speed = subprocess.Popen(
            cmd_fan_speed, shell=True, stdout=subprocess.PIPE
        )

        fan_speed = proc_fan_speed.communicate()[0].decode().strip()
        proc_fan_speed.stdout.close()
        fan_speed = int(fan_speed)

        # color fan icon relevant to fan speed
        if fan_speed < 5:
            fan_mode = (
                f"<span font='FontAwesome' foreground='{device_inactive}'>\uf863</span>"
            )
        elif 5 <= fan_speed <= 40:
            fan_mode = f"<span font='FontAwesome' foreground='{device_active_low}'>\uf863</span>"
        elif 40 <= fan_speed <= 100:
            fan_mode = f"<span font='FontAwesome' foreground='{device_active_high}'>\uf863</span>"
        else:
            fan_mode = (
                f"<span font='FontAwesome' foreground='{device_disabled}'>\uf863</span>"
            )
        return fan_mode

    elif fan_type.lower() == "asus-nb-wmi":
        PATH_TO_FAN = "/sys/devices/platform/asus-nb-wmi/fan_boost_mode"
        try:
            result = subprocess.run(
                ["cat", PATH_TO_FAN], capture_output=True, text=True, check=True
            )
            mode = result.stdout.strip()
        except subprocess.CalledProcessError as e:
            print(f"Fan check failed: {e}")
            return None

        fan_modes = {
            "0": "<span font='FontAwesome' foreground='#666666'>\uf863</span>",
            "1": "<span font='FontAwesome' foreground='#A9A9A9'>\uf863</span>",
            "2": "<span font='FontAwesome' foreground='#FFFFFF'>\uf863</span>",
        }

        fan_mode = fan_modes.get(mode, "")
        return fan_mode

    else:
        print(f"Fan type [{fan_type}] not supported")
        sys.exit(1)


# i3blocks_check function called by i3blocks.py
def i3blocks_check(warning, critical):
    # gather check data
    load_avg = os.getloadavg()
    cores = os.cpu_count()
    load = round(load_avg[0] / cores, 1)

    # compare results to thresholds
    check_results = perform_check(
        load, "float", warning, critical, "gt", color_ok, color_warn, color_nok
    )
    color = check_results["color"]
    result = check_results["result"]

    # print output
    if fan_present:
        fan_mode = get_fan_speed(fan_type)
        print(
            f"{load} <span font='FontAwesome' foreground='{color}'>\uf3fd</span> {fan_mode}"
        )
    else:
        print(f"{load} <span font='FontAwesome' foreground='{color}'>\uf3fd</span>")
