# i3blocks

## example
![image](https://github.com/mikeredev/i3blocks/assets/132297919/e029ff01-dd68-4b3c-8629-259a52da41d0)

# description
a lightweight i3blocks python implementation with stylised blocks and visual `OK` `WARN` `NOK` alerting

# toolset
`alsa-utils` `nmcli` `nvidia` 

# blocks
`volume` `wireless` `memory` `cpu load` `gpu` `time` 

# installation
update your i3 config to start the bar with the new i3blocks configuration file:
`
bar {status_command i3blocks -c ~/.config/i3blocks/i3blocks.conf}
`

```
cd ~/.config
git clone https://github.com/mikeredev/i3blocks.git
cd i3blocks
sudo pacman -s psutil ttf-font-awesome ttf-inconsolata-nerd
i3-msg restart
```

# signals
`1 volume` `2 ethernet` `3 wifi`

- custom actions can be defined in `functions/block_button.py`

- bind hotkeys in i3 appending  `pkill -RTMIN+[SIGNAL] i3blocks` to the command to update the block value, e.g., where volume is signal 1 use `bindsym XF86AudioMute exec --no-startup-id pactl set-sink-mute @DEFAULT_SINK@ toggle && exec pkill -RTMIN+1 i3blocks`

- signals must be defined in the appropriate `i3blocks.conf` section

# configuring thresholds
- define `warning` and `critical` inside `i3blocks.conf`, for example:
```
[load]
command=~/.config/i3blocks/i3blocks --check $BLOCK_NAME --warning 0.7 --critical 1.0

[gpu]
command=~/.config/i3blocks/i3blocks --check $BLOCK_NAME --warning 70 --critical 80
```

# creating new blocks
- store new modules in `blocks` as `$BLOCK_NAME.py`
- update dictionary in `i3blocks` python script, format `$BLOCK_NAME = $module_filename`
- the script module should have a function `i3blocks_check(warning, critical)`
- this function should be presented with an int or float to check against
- the function should output the result in the desired format and/or perform additional actions on check completion
- define the blocks and configure the alert thresholds in `i3blocks.conf`

# styling
- use the config file to configure glyphs (e.g., circle for rounded blocks)
- fonts and colours are defined in `styles/styles.py`
- default fonts are listed above, download these or change the config to your preferred font

# more info
- config files for i3, dunst, etc., may be found in [dotfiles](https://github.com/mikeredev/dotfiles) repo
- any custom scripts attached here can probably be found in [dotfiles/scripts/tools/](https://github.com/mikeredev/dotfiles/tree/main/scripts/tools)
- [i3blocks documentation](https://vivien.github.io/i3blocks)
- [vivien/i3blocks](https://github.com/vivien/i3blocks)
