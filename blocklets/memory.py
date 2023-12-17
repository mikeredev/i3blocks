# import required functions/modules
import psutil
from styles import styles
from functions.block_button import block_button

# load mouse button click handler
block_button("check_memory", button=None)

# collect check data
memory_util = round(psutil.virtual_memory().percent)


# i3blocks_check function called by i3blocks.py
def i3blocks_check(warning, critical):
    status_color =  f"{styles.NOK}" if memory_util >= int(critical) else (
                    f"{styles.WARN}" if memory_util >= int(warning) else
                    f"{styles.OK}")

    print(f"<span font='{styles.FONT}'>{memory_util}%</span> <span font='{styles.GLYPHS}' color='{status_color}'>\uf201</span>")
