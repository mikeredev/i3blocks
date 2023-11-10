# import required functions/modules
import os

# get required values
load_avg = os.getloadavg()
total_cores = os.cpu_count()
cpu_load = round(load_avg[0] / total_cores, 1)


# check and display output
def i3blocks_check(warning,critical):
    status_color = "#FB4934" if cpu_load >= float(critical) else ("#FABD2F" if cpu_load >= float(warning) else "#FFFFFF")
    print(f"{cpu_load} <span color='{status_color}'>\uf3fd</span>")
