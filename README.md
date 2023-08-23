#### i3blocks control script
___

#### Setup virtual environment
```
$ cd ~/data/scripts/i3blocks/
$ python -m venv venv
$ source venv/bin/activate
venv$ pip install -r requirements.txt
```

#### Copy config files
Copy default configs to `~/.config/i3blocks/i3blocks.conf` and `~/.config/i3blocks/i3blocks.conf.json`

#### JSON config file
Specify monitor name and audio sink (required!)

GPUs supported: `nvidia`

Fans supported: `nvidia` `asus-nb-wmi`

Toggle `time:adjust_glare` to disable brightness/gamma changes on day/night

#### i3blocks.conf
Add or remove entries as needed

#### i3blocks.py
Make executable via `chmod +x i3blocks.py`

Start via i3, e.g., `bar { status_command i3blocks -c ~/.config/i3blocks/i3blocks.conf }`

#### Checks
Define checks with arguments in `i3blocks.conf`. Script will return `OK`, `WARN`, or `NOK` and alert as configured.

For example, `i3blocks.py --check wifi --warning 40 --critical 20` would highlight when the SSID signal strength is below 40 or 20%, and additional actions (e.g., notify-send) can be added here.