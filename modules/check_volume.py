try:
    from .check_value import check_value
    import subprocess
except ImportError as e:
    print(f"Check failed: {e}")


def check(warning, critical):
    def get_output(cmd):
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        output, error = proc.communicate()
        if error:
            print(f"Command failed: {cmd}.\nError message: {error.decode()}")
        return output.decode().strip()

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

    volume = is_volume_enabled()
    if is_audio_enabled():
        audio_icon = "\uf028" if volume > 40 else "\uf027"
    else:
        audio_icon = "<span foreground='#666666'>\uf6a9</span>"
    color = check_value(volume, "int", warning, critical, "gt")
    print(
        f"{volume}% <span font='FontAwesome' foreground='{color}'>{audio_icon}</span>"
    )
