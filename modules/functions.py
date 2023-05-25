def check_config(units):
    import os
    import configparser

    # Get the absolute path of the directory that contains this script
    # dir_path = os.path.dirname(os.path.realpath(__file__))
    # config_file_path = os.path.join(dir_path, "..", "i3blocks.py.conf")
    config_file_path = os.path.expanduser("~/.config/i3blocks/i3blocks.py.conf")

    config = configparser.ConfigParser()
    config.read(config_file_path)

    results = {}
    for unit in units:
        try:
            results[unit] = config.get("i3blocks.py", unit)
        except (configparser.NoOptionError, configparser.NoSectionError) as e:
            print(f"Error: {e}")
            results[unit] = "unknown"

    return results


def check_value(value, datatype, warning_threshold, critical_threshold, compare):
    # load colors from config
    config = check_config(["color_ok", "color_warn", "color_nok"])
    color_ok = config.get("color_ok", "unknown")
    color_warn = config.get("color_warn", "unknown")
    color_nok = config.get("color_nok", "unknown")
    colors = {"ok": color_ok, "warn": color_warn, "nok": color_nok}

    try:
        if datatype == "float":
            value = float(value)
            warning_threshold = float(warning_threshold)
            critical_threshold = float(critical_threshold)
        elif datatype == "int":
            value = int(value)
            warning_threshold = int(warning_threshold)
            critical_threshold = int(critical_threshold)
        else:
            raise ValueError("Invalid datatype. Must be 'int' or 'float'.")
        if compare == "gt":
            if value > critical_threshold:
                return colors["nok"]
            elif value > warning_threshold:
                return colors["warn"]
            else:
                return colors["ok"]
        elif compare == "lt":
            if value < critical_threshold:
                return colors["nok"]
            elif value < warning_threshold:
                return colors["warn"]
            else:
                return colors["ok"]
        else:
            raise ValueError("Invalid comparison. Must be 'gt' or 'lt'.")
    except ValueError as e:
        raise e


def get_output(cmd):
    import subprocess

    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = proc.communicate()
    if error:
        print(f"Command failed: {cmd}. Error message: {error.decode()}")
    return output.decode().strip()
    proc.stdout.close()
