try:
    from .check_value import check_value
    import subprocess
except ImportError as e:
    print(f"Check failed: {e}")

MONITOR = "HDMI-0"


def check(warning, critical):
    cmd = ["xrandr", "--verbose"]
    cmd2 = ["grep", MONITOR, "-A", "6"]
    cmd3 = ["grep", "-oP", "(?<=Brightness: )[^ ]+"]

    p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(cmd3, stdin=p2.stdout, stdout=subprocess.PIPE)

    output = p3.communicate()[0].decode("utf-8").strip()

    color = check_value(output, "float", warning, critical, "gt")
    icon = f"<span font='FontAwesome' foreground='{color}'>\uf042</span>"
    print(f"{output} {icon}")
