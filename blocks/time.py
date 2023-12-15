# import required functions/modules
from datetime import datetime
from styles import styles

# collect check data
current_datetime    = datetime.now()
formatted_date      = current_datetime.strftime("%a%d %H:%M").upper()

# i3blocks_check function called by i3blocks.py
def i3blocks_check(warning=None, critical=None):
    print(f"<span font='{styles.FONT}'>{formatted_date}</span>")