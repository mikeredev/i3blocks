# i3blocks Control Script

This is a Python script that provides a command-line interface for performing various checks that can be used with the i3blocks status bar. The available checks include:

- Battery
- Brightness
- GPU temperature
- Load
- Memory
- Time
- Volume
- WiFi

The script takes the following arguments:

- `--check`: The check to perform (required).
- `--warning`: The warning threshold.
- `--critical`: The critical threshold.
- `--compare`: The comparison operator (`lt` for less than, `gt` for greater than).
- `--datatype`: The data type (`int` or `float`).

The script dynamically imports the appropriate module for the specified check and calls its `check()` function with the provided arguments. If the check fails, an error message is printed.

To use this script with i3blocks, you can create a custom block that calls the script with the appropriate arguments. For example:

```
[battery]
command=/path/to/i3blocks_control.py --check battery --warning 20 --critical 10 --compare lt --datatype int
interval=30
```

This block will display the battery status and change color when the battery level drops below 20% (warning) or 10% (critical).
