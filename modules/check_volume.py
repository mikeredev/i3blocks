# import required functions/modules
from functions.block_button import block_button
from functions.run_shell_command import run_shell_command as run

# load mouse button click handler
block_button("check_volume", button=None)

# required escaped shell commands (escape any braces or double quotes)
cmd_volume_level = "amixer -D pulse sget Master | grep -oP '\d+%' | head -n1 | tr -d '%'"
cmd_audio_status = "amixer -D pulse get Master | grep -oP '\[o[nf]*\]' | head -n1"

# get required values
volume_level = int(run(cmd_volume_level))
audio_status = run(cmd_audio_status)


# check and display output
def i3blocks_check(warning,critical):
    icon = "\uf6a9" if audio_status=="[off]" else ("\uf028" if volume_level >=70 else "\uf027" if volume_level >=10 else "\uf026")
    status_color = "#444444" if audio_status=="[off]" else ("#FB4934" if volume_level >= int(critical) else "#FABD2F" if volume_level >= int(warning) else "#FFFFFF")
    print(f"{volume_level}% <span color='{status_color}'>{icon}</span>")
