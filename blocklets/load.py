# import required functions/modules
import os
from styles import styles
from functions.block_button import block_button

# load mouse button click handler
block_button("check_load", button=None)

# collect check data
load_avg        = os.getloadavg()
total_cores     = os.cpu_count()
cpu_load        = round(load_avg[0] / total_cores, 1)


# i3blocks_check function called by i3blocks.py
def i3blocks_check(warning, critical):
    status_color =  f"{styles.NOK}" if cpu_load >= float(critical) else (
                    f"{styles.WARN}" if cpu_load >= float(warning) else 
                    f"{styles.OK}")

    print(f"<span font='{styles.FONT}'>{cpu_load}</span> <span font='{styles.GLYPHS}' color='{status_color}'>\uf625</span>")
