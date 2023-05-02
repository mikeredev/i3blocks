try:
    import configparser
    import os
    import subprocess
    from .functions import check_config, check_value
except ImportError as e:
    print(f"Check failed: {e}")


# read GPU manufacturer and temperature unit from config
config = check_config(["gpu", "gpu_temp_unit"])
GPU = config.get("gpu", "unknown")
TEMP_UNIT = config.get("gpu_temp_unit", "unknown")


ICONS = {
    range(75, 101): "\uf2c7",  # thermometer full
    range(50, 75): "\uf2c8",  # thermometer 3/4
    range(25, 50): "\uf2c9",  # thermometer 1/2
    range(0, 25): "\uf2ca",  # thermometer 1/4
}
DEFAULT_ICON = "\uf2cb"  # thermometer empty


def get_temperature_icon(temperature):
    for value_range, icon in ICONS.items():
        if temperature in value_range:
            return icon
    return DEFAULT_ICON


def get_gpu_temperature():
    if GPU == "nvidia":
        cmd = ["nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader"]
        proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    output = proc.communicate()[0].decode().strip()
    return int(output)


def get_gpu_vram_utilized():
    if GPU == "nvidia":
        cmd1 = [
            "nvidia-smi",
            "--query-gpu=memory.used,memory.total",
            "--format=csv,noheader",
        ]
        cmd2 = ["awk", "-F,", '{printf("%.0f%%", $1/$2*100)}']
        proc1 = subprocess.Popen(cmd1, stdout=subprocess.PIPE)
        proc = subprocess.Popen(cmd2, stdin=proc1.stdout, stdout=subprocess.PIPE)
    output = proc.communicate()[0].decode()
    return output


def check(warning, critical):
    value = get_gpu_temperature()
    vram = get_gpu_vram_utilized()
    icon = get_temperature_icon(value)
    color = check_value(value, "int", warning, critical, "gt")
    print(
        f"{vram} {value}{TEMP_UNIT} <span font='FontAwesome' foreground='{color}'>{icon}</span>"
    )
