# i3blocks

## Example
![image](https://github.com/mikeredev/i3blocks/assets/132297919/e029ff01-dd68-4b3c-8629-259a52da41d0)


## Requirements
`alsa-utils`
`fontawesome`
`nmcli`
`nvidia`
`psutil`

## Installation
- Copy or clone this repository as `$HOME/.config/i3blocks`
- Make the control script executable via `chmod +x ~/.config/i3blocks/i3blocks.py`
- Start via i3 `bar { status_command i3blocks -c ~/.config/i3blocks/i3blocks.conf }`

## BLOCK_BUTTON signals
`1 volume`
`2 ethernet`
`3 wifi`

## Configuring thresholds
Define `warning` and `critical` in `i3blocks.conf`, for example:
```
[load]
command=~/.config/i3blocks/i3blocks.py --check load --warning 0.7 --critical 1.0

[gpu]
command=~/.config/i3blocks/i3blocks.py --check gpu --warning 70 --critical 80
```

## Creating new blocks
Create an module and store it in `modules`.

This script should have a function `i3blocks_check(warning,critical)` that performs check logic and displays colored output.
