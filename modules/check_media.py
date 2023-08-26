""" check_media.py
monitors:   volume level
optional:   device monitoring (mic, webcam, bluetooth)
requires:   pulsectl
usage:      /path/to/i3blocks.py --check media --warning 100 --critical 120
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
        handle_click,
    )

    sys.path.append(
        f"/home/{os.getlogin()}/data/scripts/i3blocks/venv/lib/python3.11/site-packages"
    )
    import pulsectl
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

# load check specifics from configuration file
audio_sink = read_configuration(conf, "i3blocks", 0, "system", 0, "audio_sink")
microphone = read_configuration(
    conf, "i3blocks", 0, "devices", 0, "microphone")
webcam = read_configuration(conf, "i3blocks", 0, "devices", 0, "webcam")
bluetooth = read_configuration(conf, "i3blocks", 0, "devices", 0, "bluetooth")

# load device status colors
device_inactive = read_configuration(
    conf, "i3blocks", 0, "formatting", 0, "device_inactive"
)


# load click handler
handle_click("check_media", 0)


def get_audio_status(sink_name):
    pulse = pulsectl.Pulse()
    sink_list = pulse.sink_list()

    active_sink = None
    for sink_info in sink_list:
        if sink_info.name == sink_name:
            active_sink = sink_info
            break

    if active_sink:
        muted = active_sink.mute == 1
        volume_level = active_sink.volume.values[0] * 100
        volume_level = round(volume_level)
        return muted, volume_level
    else:
        return None, None


# i3blocks_check function called by i3blocks.py
def i3blocks_check(warning, critical):
    # gather check data
    muted_status, volume_level = get_audio_status(audio_sink)

    # compare results to thresholds
    check_results = perform_check(
        volume_level, "int", warning, critical, "gt", color_ok, color_warn, color_nok
    )
    color = check_results["color"]
    result = check_results["result"]

    # select font awesome icon based on volume level
    if muted_status:
        icon = "\uf6a9"
    elif volume_level == 0:
        icon = "\uf026"
    elif volume_level <= 40:
        icon = "\uf027"
    else:
        icon = "\uf028"

    # set icon color based on muted status
    foreground_color = device_inactive if muted_status else color

    # print output
    output = f"{volume_level}% <span foreground='{foreground_color}'>{icon}</span>"
    print(output)
