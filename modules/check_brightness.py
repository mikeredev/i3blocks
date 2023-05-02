try:
    import configparser
    import subprocess
    from .functions import check_config, check_value
except ImportError as e:
    print(f"Check failed: {e}")

# read monitor name from config
config = check_config(["monitor"])
MONITOR = config.get("monitor", "unknown")


def check(warning=None, critical=None):
    cmd = ["xrandr", "--verbose"]
    cmd2 = ["grep", MONITOR, "-A", "6"]
    cmd3 = ["grep", "-oP", "(?<=Brightness: )[^ ]+"]

    p1 = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    p2 = subprocess.Popen(cmd2, stdin=p1.stdout, stdout=subprocess.PIPE)
    p3 = subprocess.Popen(cmd3, stdin=p2.stdout, stdout=subprocess.PIPE)

    output = p3.communicate()[0].decode("utf-8").strip()
    color = check_value(output, "float", warning, critical, "gt")

    if float(output) > 0.7:
        icon = f"<span font='FontAwesome' color='{color}'>\uf042</span>"
    else:
        icon = f"<span font='FontAwesome' color='{color}'>\uf042</span>"
    print(f"{output} {icon}")
