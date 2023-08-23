""" check_gpu.py
monitors:   GPU temperature, GPU VRAM utilization%
requires:   nvidia-smi
usage:      /path/to/i3blocks.py --check gpu --warning 70 --critical 80
"""

# import modules
import subprocess
import sys

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
color_ok = read_configuration(conf, "i3blocks", 0, "formatting", 0, "color_ok")
color_warn = read_configuration(conf, "i3blocks", 0, "formatting", 0, "color_warn")
color_nok = read_configuration(conf, "i3blocks", 0, "formatting", 0, "color_nok")

# load check specifics from configuration file
gpu_type = read_configuration(conf, "i3blocks", 0, "gpu", 0, "gpu_type")
gpu_temp_unit = read_configuration(conf, "i3blocks", 0, "gpu", 0, "gpu_temp_unit")


# function to return GPU temperature
def get_gpu_temperature(gpu_type):
    if gpu_type.lower() == "nvidia":
        cmd_temperature = "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader"
        proc_temperature = subprocess.Popen(
            cmd_temperature, shell=True, stdout=subprocess.PIPE
        )
        output_temperature = proc_temperature.communicate()[0].decode().strip()
        proc_temperature.stdout.close()
    else:
        print(f"GPU [{gpu_type}] not supported")
        sys.exit(1)
    return int(output_temperature)


# function to return GPU VRAM utilization
def get_gpu_vram_utilized(gpu_type):
    if gpu_type.lower() == "nvidia":
        cmd_vram_utilization = "nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader | awk -F, '{printf(\"%.0f%%\", $1/$2*100)}'"
        proc_vram_utilization = subprocess.Popen(
            cmd_vram_utilization, shell=True, stdout=subprocess.PIPE
        )
        output_vram_utilization = proc_vram_utilization.communicate()[0].decode()
        proc_vram_utilization.stdout.close()
    else:
        print(f"GPU [{gpu_type}] not supported")
        sys.exit(1)
    return output_vram_utilization


# function to return a temperature icon representing GPU temperature
def get_icon(value):
    icons = {
        range(75, 101): "\uf2c7",  # thermometer full
        range(50, 75): "\uf2c8",  # thermometer 3/4
        range(25, 50): "\uf2c9",  # thermometer 1/2
        range(0, 25): "\uf2ca",  # thermometer 1/4
    }
    default_icon = "\uf2cb"  # thermometer empty
    for value_range, icon in icons.items():
        if value in value_range:
            return icon
    return default_icon


# i3blocks_check function called by i3blocks.py
def i3blocks_check(warning, critical):
    # gather check data
    gpu_temperature = get_gpu_temperature(gpu_type)
    gpu_vram_utilized = get_gpu_vram_utilized(gpu_type)

    # compare results to thresholds
    check_results = perform_check(
        gpu_temperature, "int", warning, critical, "gt", color_ok, color_warn, color_nok
    )
    color = check_results["color"]
    result = check_results["result"]
    icon = get_icon(gpu_temperature)

    # print output
    print(
        #f"{gpu_vram_utilized} {gpu_temperature}{gpu_temp_unit} <span font='FontAwesome' foreground='{color}'>{icon}</span>"
        f"{gpu_vram_utilized} \uf080 <span font='FontAwesome' foreground='{color}'>{icon}</span>"
    )
