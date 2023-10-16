""" check_time.py
monitors:   time
desc:       print date and time
usage:      /path/to/i3blocks.py --check time
"""

# import modules
from datetime import datetime
import subprocess

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

# load check specifics from configuration file
time_format = read_configuration(conf, "i3blocks", 0, "time", 0, "time_format")


# i3blocks_check function called by i3blocks.py
def i3blocks_check(warning=None, critical=None):
    # get the current date and time
    str_datetime = datetime.now().strftime(time_format)

    # print output
    print(
        f"{str_datetime.upper()} <span font_desc='FontAwesome' foreground='#444444'></span>"
    )
