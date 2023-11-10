# i3blocks

## Example
![image](https://github.com/mikeredev/i3blocks/assets/132297919/e029ff01-dd68-4b3c-8629-259a52da41d0)


## Requirements
`alsa-utils`
`fontawesome`
`nmcli`
`nvidia`
`psutil`

## Blocks
`time`
`GPU VRAM% util, fan speed, temperature`
`CPU 1min load average%`
`memory`
`wireless signal`
`volume control`

## Installation
- Copy or clone this repository as `$HOME/.config/i3blocks`
- Make `i3blocks.py` executable via `chmod +x ~/.config/i3blocks/i3blocks.py`
- Start via i3 `bar {status_command i3blocks -c ~/.config/i3blocks/i3blocks.conf}`

## BLOCK_BUTTON signals
`1 volume`
`3 wifi`

- Custom actions can be defined in `functions/block_button.py`
- Bind hotkeys in i3 appending  `pkill -RTMIN+[SIGNAL] i3blocks` to the command to update the block value, e.g., where volume is signal 1 use `bindsym XF86AudioMute exec --no-startup-id pactl set-sink-mute @DEFAULT_SINK@ toggle && exec pkill -RTMIN+1 i3blocks`

## Configuring thresholds
Define `warning` and `critical` in `i3blocks.conf`, for example:
```
[load]
command=~/.config/i3blocks/i3blocks.py --check $BLOCK_NAME --warning 0.7 --critical 1.0

[gpu]
command=~/.config/i3blocks/i3blocks.py --check $BLOCK_NAME --warning 70 --critical 80
```

## Creating new blocks
- Store new modules in `modules` as `check_$BLOCK_NAME.py`
- Add it to the modules list in `i3blocks.py` in format `$BLOCK = check_$BLOCK_NAME`
- The script module should have a function `i3blocks_check(warning,critical)`
- This function should be presented with an int or float to check against
- The function should output the result in the desired format and/or perform additional actions on check completion
- Define the blocks and configure the alert thresholds in `i3blocks.conf`

## More info
- Config files for i3, dunst, etc., may be found in [dotfiles](https://github.com/mikeredev/dotfiles) repo
- [i3blocks documentation](https://vivien.github.io/i3blocks)
- [vivien/i3blocks](https://github.com/vivien/i3blocks)
