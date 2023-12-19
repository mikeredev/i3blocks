# import required functions/modules
import os
from functions.run_shell_command import run_shell_command as run


# function to handle mouse button actions
# 1 left, 2 middle, 3 right, 4 mouse up, 5 mouse down
def block_button(module, button):
    # Define the button actions for each module
    module_actions = {
        "check_volume": {
            2: "pactl set-sink-mute @DEFAULT_SINK@ toggle && pkill -RTMIN+1 i3blocks",
            4: "pactl set-sink-volume @DEFAULT_SINK@ +10% && pkill -RTMIN+1 i3blocks",
            5: "pactl set-sink-volume @DEFAULT_SINK@ -10% && pkill -RTMIN+1 i3blocks"
        },
        "check_wifi": {
            2: "~/.config/scripts/tools/connect-wifi.sh"
        },
        "check_memory": {
            2: "alacritty -e htop --sort-key PERCENT_MEM"
        },
        "check_load": {
            2: "alacritty -e htop --sort-key PERCENT_CPU"
        },
        "check_gpu": {
            2: "alacritty -e sh -c 'nvidia-smi; read -p [ok]'"
        }
    }

    button = int(os.getenv("BLOCK_BUTTON", "0"))

    actions = module_actions[module]
    action = actions.get(button)
    if action:
        run(action)
