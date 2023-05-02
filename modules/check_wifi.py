try:
    import subprocess
    from .functions import check_value
except ImportError as e:
    print(f"Check failed: {e}")


def check(warning, critical):
    cmd = ["nmcli", "-f", "SIGNAL,IN-USE", "dev", "wifi", "list"]
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = proc.communicate()
    if error:
        print(f"Check failed: {error.decode()}")
        return
    proc.stdout.close()

    lines = output.decode().strip().split("\n")
    value = next((line.split()[0] for line in lines if "*" in line), None)
    if value is not None:
        color = check_value(int(value), "int", warning, critical, "lt")
        print(f"{value}% <span font='FontAwesome' foreground='{color}'>\uf1eb</span>")
    else:
        print("<span font='FontAwesome' foreground='#666666'>\uf1eb</span>")
