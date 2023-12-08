# import required functions/modules
import psutil

# get required values
memory_util = round(psutil.virtual_memory().percent)


# check and display output
def i3blocks_check(warning,critical):
    status_color = "red" if memory_util >= int(critical) else ("orange" if memory_util >= int(warning) else "white")
    print(f"{memory_util}% <span color='{status_color}'>\uf201</span>")
    