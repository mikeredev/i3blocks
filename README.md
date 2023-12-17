# examples
simple
![i3blocks-simple](https://github.com/mikeredev/i3blocks/assets/132297919/a2a04c39-b7a0-4a10-9994-44908535ea6e)

rounded
![i3blocks-rounded](https://github.com/mikeredev/i3blocks/assets/132297919/e379d6ea-b767-4402-95d1-0bba1b08a5c0)

angles
![i3blocks-angles](https://github.com/mikeredev/i3blocks/assets/132297919/e9de35f5-a6c5-4391-b79f-d344154ee315)

powerline
![i3blocks-powerline](https://github.com/mikeredev/i3blocks/assets/132297919/38a18e92-6ce3-46f7-bc53-75a674739b3c)


# description
a lightweight i3blocks python implementation with stylised blocks and visual `OK` `WARN` `NOK` alerting on returned values


# toolset
`alsa-utils` `nmcli` `nvidia` 


# blocks
`volume` `wireless` `memory` `cpu load` `gpu` `time` 


# installation
- update your i3 config to start the bar with the new i3blocks configuration file: `bar { status_command i3blocks -c ~/.config/i3blocks/i3blocks.conf }`
- clone or download this repo into `~/.config/i3blocks`, and get the default fonts
```bash
sudo pacman -S python-psutil ttf-font-awesome ttf-inconsolata-nerd
cd ~/.config
git clone https://github.com/mikeredev/i3blocks.git
i3-msg restart
```


# signals
`1 volume` `2 ethernet` `3 wifi`
- custom actions can be defined in `functions/block_button.py`
- bind hotkeys in i3 appending  `pkill -RTMIN+[SIGNAL] i3blocks` to the command to update the block value, e.g., where volume is signal 1 use `bindsym XF86AudioMute exec --no-startup-id pactl set-sink-mute @DEFAULT_SINK@ toggle && exec pkill -RTMIN+1 i3blocks`
- signals must be defined in the appropriate `i3blocks.conf` section


# configuring thresholds
- define `warning` and `critical` alert thresholds in `i3blocks.conf`, for example:

```conf
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

**for example** you want to create a new blocklet that displays available updates, i.e., `checkupdates | wc -l`. to alert on this returned value:
- create a script `updates.py` in `blocklets/` which reads and returns this value
- include in this script a function called `i3blocks_check(warning, critical)` which simply returns a span of text in font pango markup based on whether the returned integer in this case breaches the warning or critical thresholds, e.g., 50 and 100
- update the dictionary in main python script `i3blocks` to include this new blocklet by its name `updates`
- update i3blocks.conf to call it via `i3blocks --check updates --warning 50 --critical 100`


# styling
- fonts and colours are defined in `styles/styles.py`
- default fonts are listed above, download these or config your preferred font
- additional themes are in `styles/themes`
- select a theme, e.g., powerline, and `cp styles/themes/i3blocks-powerline.conf i3blocks.conf` from the i3blocks directory and restart i3 to update


# more info
- config files for i3, dunst, etc., may be found in [dotfiles](https://github.com/mikeredev/dotfiles) repo
- any custom scripts attached here can probably be found in [dotfiles/scripts/tools/](https://github.com/mikeredev/dotfiles/tree/main/scripts/tools)
- [i3blocks documentation](https://vivien.github.io/i3blocks)
- [vivien/i3blocks](https://github.com/vivien/i3blocks)

