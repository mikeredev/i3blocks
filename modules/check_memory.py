# import required functions/modules
import psutil
from colors import colors
from functions.block_button import block_button

# load mouse button click handler
block_button("check_memory", button=None)

# collect check data
memory_util = round(psutil.virtual_memory().percent)


# i3blocks_check function called by i3blocks.py
def i3blocks_check(warning, critical):
    status_color =  f"{colors.NOK}" if memory_util >= int(critical) else (
                    f"{colors.WARN}" if memory_util >= int(warning) else
                    f"{colors.OK}")

    print(f"{memory_util}% <span color='{status_color}'>\uf201</span>")
