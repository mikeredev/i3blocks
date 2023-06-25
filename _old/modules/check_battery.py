try:
    import psutil
    from .functions import check_value
except ImportError as e:
    print(f"Check failed: {e}")


def check(warning, critical):
    battery = psutil.sensors_battery()
    plugged = battery.power_plugged
    percent = round(battery.percent)

    if plugged:
        icon = "\uf0e7"  # bolt
    elif 75 <= percent <= 100:
        icon = "\uf240"  # battery full
    elif 50 <= percent < 75:
        icon = "\uf241"  # battery 3/4
    elif 25 <= percent < 50:
        icon = "\uf242"  # battery 1/2
    elif 0 <= percent < 25:
        icon = "\uf243"  # battery 1/4
    else:
        icon = "\uf244"  # battery-empty

    color = check_value(percent, "int", warning, critical, "lt")
    print(f"{percent}% <span font='FontAwesome' foreground='{color}'>{icon}</span>")
