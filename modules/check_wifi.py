# import required functions/modules
from functions.block_button import block_button
from functions.run_shell_command import run_shell_command as run

# load mouse button click handler
block_button("check_wifi", button=None)

# required escaped shell commands (escape any braces or double quotes)
cmd_wifi_signal = "nmcli -f SIGNAL,IN-USE dev wifi | grep '*' | awk '{print $1}' | tr -d '*'"

# get required values
try:
    wifi_signal = int(run(cmd_wifi_signal))
except:
    wifi_signal = 0


# check and display output
def i3blocks_check(warning,critical):
    status_color = "#444444" if wifi_signal == 0 else ("red" if wifi_signal <= int(critical) else "orange" if wifi_signal <= int(warning) else "white")
    print(f"{wifi_signal}% <span color='{status_color}'>\uf1eb</span>")
