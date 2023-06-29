""" check_time.py
monitors:   time
optional:   screen glare
desc:       uses `time` values from config to print day/night icon and `adjust_glare` if selected
requires:   xrandr
usage:      /path/to/i3blocks.py --check time
"""

# import modules
from datetime import datetime
import subprocess

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
monitor = read_configuration(conf, "i3blocks", 0, "system", 0, "monitor")

# load check specifics from configuration file
day = read_configuration(conf, "i3blocks", 0, "time", 0, "day")
night = read_configuration(conf, "i3blocks", 0, "time", 0, "night")
time_format = read_configuration(conf, "i3blocks", 0, "time", 0, "time_format")
adjust_glare = read_configuration(conf, "i3blocks", 0, "time", 0, "adjust_glare")
day_brightness = read_configuration(conf, "i3blocks", 0, "time", 0, "day_brightness")
day_gamma = read_configuration(conf, "i3blocks", 0, "time", 0, "day_gamma")
night_brightness = read_configuration(
    conf, "i3blocks", 0, "time", 0, "night_brightness"
)
night_gamma = read_configuration(conf, "i3blocks", 0, "time", 0, "night_gamma")

# load device status colors
device_inactive = read_configuration(
    conf, "i3blocks", 0, "formatting", 0, "device_inactive"
)
device_active_low = read_configuration(
    conf, "i3blocks", 0, "formatting", 0, "device_active_low"
)
device_active_high = read_configuration(
    conf, "i3blocks", 0, "formatting", 0, "device_active_high"
)


# function to get gamma/brightness level from xrandr
def get_level(level):
    command = f"xrandr --verbose | grep {level}"
    output = subprocess.check_output(command, shell=True, universal_newlines=True)

    lines = output.split("\n")
    for line in lines:
        if f"{level}:" in line:
            level = float(line.split(":")[1].strip())  # Convert value to float
    return level


# function to adjust screen brightness and gamma
def adjust_glare_run(time_of_day):
    gamma_level = get_level("Gamma")  # case sensitive
    if time_of_day == "day" and gamma_level != day_gamma:
        cmd = f"xrandr --output {monitor} --brightness {day_brightness} --gamma {day_gamma}"
        proc = subprocess.Popen(cmd, shell=True)
    elif time_of_day == "night" and gamma_level != night_gamma:
        cmd = f"xrandr --output {monitor} --brightness {night_brightness} --gamma {night_gamma}"
        proc = subprocess.Popen(cmd, shell=True)


# i3blocks_check function called by i3blocks.py
def i3blocks_check(warning=None, critical=None):
    # get the current date and time
    str_datetime = datetime.now().strftime(time_format)

    # set icon color based on brightness level
    brightness = get_level("Brightness")  # case sensitive
    if brightness == 1:
        foreground_color = device_active_high
    elif brightness < 1 and brightness > 0.5:
        foreground_color = device_active_low
    elif brightness == 0.5:
        foreground_color = device_inactive
    else:
        foreground_color = "#444444"

    # assign icon for day/night
    current_hour = datetime.now().hour
    icon = "\uf185"  # Sun icon by default
    time_of_day = "day"
    if current_hour >= int(night) or current_hour < int(day):
        icon = "\uf186"  # Moon icon
        time_of_day = "night"

    # adjust glare if `adjust_glare = True`
    if adjust_glare:
        adjust_glare_run(time_of_day)

    # print output
    print(
        f"{str_datetime.upper()} <span font_desc='FontAwesome' foreground='{foreground_color}'>{icon}</span>"
    )
