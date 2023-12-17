# import required functions/modules
from styles import styles
from functions.run_shell_command import run_shell_command as run
from functions.block_button import block_button

# load mouse button click handler
block_button("check_wifi", button=None)

# escaped shell commands
cmd_wifi_signal     = "nmcli -f SIGNAL,IN-USE dev wifi | grep '*' | awk '{print $1}' | tr -d '*'"

# collect check data
try:
    wifi_signal     = int(run(cmd_wifi_signal))
except:
    wifi_signal = 0


# i3blocks_check function called by i3blocks.py
def i3blocks_check(warning, critical):
    status_color =  f"{styles.NONE}" if wifi_signal == 0 else (
                    f"{styles.NOK}" if wifi_signal <= int(critical) else
                    f"{styles.WARN}" if wifi_signal <= int(warning) else
                    f"{styles.OK}")
        
    print(f"<span font='{styles.FONT}'>{wifi_signal}%</span> <span font='{styles.GLYPHS}' color='{status_color}'>\uf1eb</span>")
