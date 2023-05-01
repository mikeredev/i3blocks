try:
    from .check_value import check_value
    import os
    import subprocess
except ImportError as e:
    print(f"Check failed: {e}")

INCLUDE_FAN = False  # disabled on desktop
PATH_TO_FAN = "/sys/devices/platform/asus-nb-wmi/fan_boost_mode"


def get_fan_status():
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


def check(warning, critical):
    load_avg = os.getloadavg()
    cores = os.cpu_count()
    load = round(load_avg[0] / cores, 1)
    color = check_value(load, "float", warning, critical, "gt")

    if INCLUDE_FAN:
        fan_mode = get_fan_status()
        if fan_mode is not None:
            print(
                f"{load} <span font='FontAwesome' foreground='{color}'>\uf0e4</span> {fan_mode}"
            )
        else:
            print(f"{load} <span font='FontAwesome' foreground='{color}'>\uf0e4</span>")
    else:
        print(f"{load} <span font='FontAwesome' foreground='{color}'>\uf0e4</span>")
