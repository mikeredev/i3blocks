import subprocess
from functions import check_config

# read config
config = check_config(["microphone", "webcam", "bluetooth"])
check_mic = config.get("microphone", "unknown")
check_webcam = config.get("webcam", "unknown")
check_bluetooth = config.get("bluetooth", "unknown")


def is_microphone_enabled():
    cmd1 = ["/usr/bin/pacmd", "list-sources"]
    cmd2 = [
        "awk",
        "/\\* index/{getline; print; for(i=1;i<=10;i++) {getline; print}}",
    ]
    cmd3 = ["grep", "-i", "muted"]
    cmd4 = ["cut", "-d:", "-f2"]
    cmd5 = ["awk", "{$1=$1};1"]
    p1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(cmd3, stdin=p2.stdout, stdout=subprocess.PIPE)
    p4 = subprocess.Popen(cmd4, stdin=p3.stdout, stdout=subprocess.PIPE)
    p5 = subprocess.Popen(cmd5, stdin=p4.stdout, stdout=subprocess.PIPE)
    output, _ = p5.communicate()
    for p in [p1, p2, p3, p4, p5]:
        p.stdout.close()
    return "no" in output.decode().lower()


def is_webcam_enabled():
    cmd = ["lsof", "/dev/video*", "/dev/media0"]  # path to webcam devices
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return_code = process.wait()
    process.stdout.close()
    process.stderr.close()
    return return_code == 0


def is_bluetooth_enabled():
    cmd = ["bluetoothctl", "show"]
    process1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    cmd = ["grep", "Powered"]
    process2 = subprocess.Popen(cmd, stdin=process1.stdout, stdout=subprocess.PIPE)
    process1.stdout.close()
    output, _ = process2.communicate()
    process2.stdout.close()
    return "yes" in output.decode().lower()


str_output = "<span>"

if check_mic:
    mic_icon = (
        "\uf130"
        if is_microphone_enabled()
        else "<span foreground='#666666'>\uf130</span>"
    )
    str_output += f"{mic_icon}"

if check_webcam:
    webcam_icon = (
        "\uf03d" if is_webcam_enabled() else "<span foreground='#666666'>\uf03d</span>"
    )
    str_output += f"{webcam_icon}"

if check_bluetooth:
    bluetooth_icon = (
        "\uf294"
        if is_bluetooth_enabled()
        else "<span foreground='#666666'>\uf294</span>"
    )
    str_output += f"{bluetooth_icon}"

str_output += "</span>"

print(str_output)
