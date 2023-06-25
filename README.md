## i3blocks control script

### Setup virtual environment
```
$ cd ~/data/scripts/i3blocks/
$ python -m venv venv
$ source venv/bin/activate
venv$ pip install -r requirements.txt
```
### Copy config files
Copy default configs to `~/.config/i3blocks/i3blocks.conf` and `~/.config/i3blocks/i3blocks.conf.json`

### JSON config file
Specify monitor name and audio sink (required!)
GPUs supported: `nvidia`
Fans supported: `nvidia` `asus-nb-wmi`
Toggle time:adjust_glare to disable brightness/gamma changes on day/night

### i3blocks.conf
Add or remove entries as desired, google "i3blocks conf documentation" for more info

### i3blocks.py
Make executable, e.g., `chmod +x i3blocks.py`
Start via i3, e.g., `bar { status_command i3blocks -c ~/.config/i3blocks/i3blocks.conf }`
