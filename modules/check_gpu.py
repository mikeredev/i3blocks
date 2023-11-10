# import required functions/modules
from functions.run_shell_command import run_shell_command as run

# required escaped shell commands (escape any braces or double quotes)
cmd_vram_util = "nvidia-smi --query-gpu=memory.used,memory.total --format=csv,noheader,nounits | awk -F',' '{{printf \"%.0f\\n\", $1 / $2 * 100}}'"
cmd_gpu_temp = "nvidia-smi --query-gpu=temperature.gpu --format=csv,noheader,nounits"
cmd_fan_speed = "nvidia-smi --query-gpu=fan.speed --format=csv,noheader,nounits"

# get required values
vram_util = int(run(cmd_vram_util))
gpu_temp = int(run(cmd_gpu_temp))
fan_speed= int(run(cmd_fan_speed))


# check and display output
def i3blocks_check(warning, critical):
    icon = "\uf2c7" if gpu_temp >=60 else "\uf2cb" # fontawesome thermometer icons
    status_color = "#FB4934" if gpu_temp >= int(critical) else ("#FABD2F" if gpu_temp >= int(warning) else "#FFFFFF")
    fan_color = "#FFFFFF" if fan_speed >= 40 else ("#A9A9A9" if fan_speed >= 20 else "#666666")
    print(f"{vram_util}% <span color='{fan_color}'>\uf863</span> <span color='{status_color}'>{icon}</span>")
