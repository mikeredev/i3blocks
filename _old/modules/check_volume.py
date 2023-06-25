try:
    import subprocess
    from .functions import check_config, check_value, get_output
except ImportError as e:
    print(f"Check failed: {e}")

# read config
config = check_config(["microphone", "webcam", "bluetooth"])
check_mic = config.get("microphone", "unknown")
check_webcam = config.get("webcam", "unknown")
check_bluetooth = config.get("bluetooth", "unknown")


def is_volume_enabled():
    output = get_output(["pacmd", "list-sinks"])
    sinks = output.split("* index")
    sum = 0
    for sink in sinks[1:]:
        if "volume:" in sink:
            volumes = sink.split("volume:")[1].split("/")
            for volume in volumes:
                vol = volume.strip()
                if vol.endswith("%"):
                    sum += int(vol[:-1])
    avg = sum / 2
    return int(avg)


def is_audio_enabled():
    output = get_output(["pacmd", "list-sinks"])
    sinks = output.split("* index")
    muted = False
    for sink in sinks[1:]:
        if "muted:" in sink:
            muted_str = sink.split("muted:")[1].split("\n")[0].strip()
            muted = muted or (muted_str == "yes")
    return not muted


def is_microphone_enabled():
    pacmd_cmd = ["/usr/bin/pacmd", "list-sources"]
    awk_cmd = [
        "awk",
        "/\\* index/{getline; print; for(i=1;i<=10;i++) {getline; print}}",
    ]
    grep_cmd = ["grep", "-i", "muted"]
    cut_cmd = ["cut", "-d:", "-f2"]
    awk2_cmd = ["awk", "{$1=$1};1"]

    pacmd_output = subprocess.Popen(pacmd_cmd, stdout=subprocess.PIPE)
    awk_output = subprocess.Popen(
        awk_cmd, stdin=pacmd_output.stdout, stdout=subprocess.PIPE
    )
    grep_output = subprocess.Popen(
        grep_cmd, stdin=awk_output.stdout, stdout=subprocess.PIPE
    )
    cut_output = subprocess.Popen(
        cut_cmd, stdin=grep_output.stdout, stdout=subprocess.PIPE
    )
    awk2_output = subprocess.Popen(
        awk2_cmd, stdin=cut_output.stdout, stdout=subprocess.PIPE
    )

    output, _ = awk2_output.communicate()
    for p in [pacmd_output, awk_output, grep_output, cut_output, awk2_output]:
        p.stdout.close()

    return "no" in output.decode().lower()


def is_webcam_enabled():
    lsof_cmd = ["/usr/bin/lsof", "/dev/video0", "/dev/media0"]
    grep_cmd = ["grep", "-q", "."]
    lsof_output = subprocess.Popen(lsof_cmd, stdout=subprocess.PIPE)
    grep_output = subprocess.Popen(
        grep_cmd, stdin=lsof_output.stdout, stdout=subprocess.PIPE
    )
    lsof_output.stdout.close()
    grep_output.communicate()
    grep_output.stdout.close()
    return grep_output.returncode == 0


def is_bluetooth_enabled():
    cmd = ["bluetoothctl", "show"]
    process1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    cmd = ["grep", "Powered"]
    process2 = subprocess.Popen(cmd, stdin=process1.stdout, stdout=subprocess.PIPE)
    process1.stdout.close()
    output, _ = process2.communicate()
    process2.stdout.close()
    return "yes" in output.decode().lower()


def check(warning, critical):
    if check_mic.lower() == "true":
        try:
            if is_microphone_enabled():
                mic_icon = "<span font='FontAwesome' foreground='#FFFFFF'>\uf130</span>"
            else:
                mic_icon = "<span font='FontAwesome' foreground='#666666'>\uf130</span>"
        except:
            mic_icon = "<span font='FontAwesome' foreground='#dd2222'>\uf130</span>"

    if check_bluetooth.lower() == "true":
        try:
            if is_bluetooth_enabled():
                bluetooth_icon = (
                    "<span font='FontAwesome' foreground='#FFFFFF'>\uf294</span>"
                )
            else:
                bluetooth_icon = (
                    "<span font='FontAwesome' foreground='#666666'>\uf294</span>"
                )
        except:
            bluetooth_icon = (
                "<span font='FontAwesome' foreground='#dd2222'>\uf294</span>"
            )

    if check_webcam.lower() == "true":
        try:
            if is_webcam_enabled():
                webcam_icon = (
                    "<span font='FontAwesome' foreground='#FFFFFF'>\uf03d</span>"
                )
            else:
                webcam_icon = (
                    "<span font='FontAwesome' foreground='#666666'>\uf03d</span>"
                )
        except:
            webcam_icon = "<span font='FontAwesome' foreground='#dd2222'>\uf03d</span>"

    volume = is_volume_enabled()
    if is_audio_enabled():
        audio_icon = "\uf028" if volume > 40 else "\uf027"
    else:
        audio_icon = "<span foreground='#666666'>\uf6a9</span>"
    color = check_value(volume, "int", warning, critical, "gt")

    output = (
        f"{volume}% <span font='FontAwesome' foreground='{color}'>{audio_icon}</span>"
    )
    if check_mic.lower() == "true":
        output += f" {mic_icon}"
    if check_bluetooth.lower() == "true":
        output += f" {bluetooth_icon}"
    if check_webcam.lower() == "true":
        output += f" {webcam_icon}"
    print(output)
