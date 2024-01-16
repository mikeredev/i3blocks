### examples

| style | example |
|:------|:--------|
| angles | ![i3blocks-angles](https://github.com/mikeredev/i3blocks/assets/132297919/c3232c62-5bde-4546-9f4d-7b9caa777e49) |
| powerline | ![i3blocks-powerline](https://github.com/mikeredev/i3blocks/assets/132297919/cf44d0ed-4273-49e3-91df-1bd80cdfef8d) |
| rounded | ![i3blocks-rounded](https://github.com/mikeredev/i3blocks/assets/132297919/4997d82c-99cd-4125-9c50-2eeeb515be3c) |
| simple | ![i3blocks-simple](https://github.com/mikeredev/i3blocks/assets/132297919/ac8eb95b-fb9f-4cc6-bb77-c4954fa9ac2b) |
| solid | ![i3blocks-solid](https://github.com/mikeredev/i3blocks/assets/132297919/b7e64fc9-ae3f-4d4e-9b92-0cd6232f5806) |


### description
a lightweight i3blocks implementation with stylised blocks and visual `OK` `WARN` `NOK` alerting on returned values


### uses
`alsa-utils` `nvidia` `pulseaudio` 


### blocks
`volume` `wifi` `memory` `cpu load` `gpu` `time` 


### installation
- update your i3 config to start the bar with the new i3blocks configuration file: `bar { status_command i3blocks -c ~/.config/i3blocks/i3blocks.conf }`
- clone or download this repo into `~/.config/i3blocks`, and get the default fonts
```bash
sudo pacman -S python-psutil ttf-font-awesome ttf-inconsolata-nerd
cd ~/.config
git clone https://github.com/mikeredev/i3blocks.git
chmod +x control
i3-msg restart
```


### signals
`1 volume` `2 ethernet` `3 wifi`


### mouse actions
`$BLOCK_BUTTON` allows for the following mouse events:
```
1: left-click
2: middle-click
3: right-click
4: mouse wheel up
5: mouse wheel down
```

### configuring thresholds
- define `warning` and `critical` thresholds directly in `i3blocks.conf`, e.g.:

```conf
[load]
command="$HOME"/.config/i3blocks/control --check load --warning 0.7 --critical 1.0

[gpu]
command="$HOME"/.config/i3blocks/control --check $BLOCK_NAME --warning 70 --critical 80
```


### creating new blocks
- store new modules in the `blocks` directory
- the control script will call its `i3blocks_check(warning, critical)` function


### styling
- colors/fonts/glyphs can be defined in `i3blocks.conf`


### more info
- config files for i3, dunst, etc., may be found in [dotfiles](https://github.com/mikeredev/dotfiles) repo
- any custom scripts attached here can probably be found in [dotfiles/scripts/tools/](https://github.com/mikeredev/dotfiles/tree/main/scripts/tools)
- [i3blocks documentation](https://vivien.github.io/i3blocks)
- [vivien/i3blocks](https://github.com/vivien/i3blocks)
