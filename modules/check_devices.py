# wip

import subprocess

try:
    from .check_value import check_value
except ImportError as e:
    print(f"Check failed: {e}")


def check(warning, critical):
    mic_icon = (
        "\uf130"
        if is_microphone_enabled()
        else "<span foreground='#666666'>\uf130</span>"
    )
    webcam_icon = (
        "\uf03d" if is_webcam_enabled() else "<span foreground='#666666'>\uf03d</span>"
    )
    bluetooth_icon = (
        "\uf294"
        if is_bluetooth_enabled()
        else "<span foreground='#666666'>\uf294</span>"
    )
    print(f"{mic_icon}  {webcam_icon}  {bluetooth_icon}")


def get_output(cmd):
    return subprocess.check_output(cmd, shell=True, text=True).strip()


def is_microphone_enabled():
    try:
        output = get_output(
            "pacmd list-sources | awk '/\\* index/{getline; print; for(i=1;i<=10;i++) {getline; print}}' | grep -i 'muted' | cut -d':' -f2 | awk '{$1=$1};1'"
        )
        return "no" in output.lower()
    except:
        print("fail1")


def is_webcam_enabled():
    try:
        cmd = "lsof /dev/video* /dev/media0 2>/dev/null | grep -q ."  # paths to webcam device(s)
        return subprocess.run(cmd, shell=True).returncode == 0
    except:
        print("fail2")


def is_bluetooth_enabled():
    try:
        output = get_output("bluetoothctl show | grep Powered")
        return "yes" in output.lower()
    except:
        print("fail3")
