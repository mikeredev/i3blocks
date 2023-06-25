# function to load JSON configuration file
def load_configuration():
    import json
    import os

    config_file_path = f"/home/{os.getlogin()}/.config/i3blocks/i3blocks.conf.json"
    with open(config_file_path, "r") as file:
        data = json.load(file)
    return data


# function to read JSON configuration file
def read_configuration(data, *keys):
    result = data
    for key in keys:
        if isinstance(result, list):
            key = int(key)  # Convert key to integer if accessing a list
            if len(result) > key:
                result = result[key]
            else:
                return None
        else:
            if key in result:
                result = result[key]
            else:
                return None
    return result


# function to compare warning and critical values and return results
def perform_check(
    value,
    datatype,
    warning_threshold,
    critical_threshold,
    compare,
    color_ok,
    color_warn,
    color_nok,
):
    valid_datatypes = ["int", "float"]
    valid_comparisons = ["gt", "lt"]

    if datatype not in valid_datatypes:
        raise ValueError("Invalid datatype. Must be 'int' or 'float'.")
    if compare not in valid_comparisons:
        raise ValueError("Invalid comparison. Must be 'gt' or 'lt'.")

    converted_value = float(value) if datatype == "float" else int(value)
    converted_warning = (
        float(warning_threshold) if datatype == "float" else int(warning_threshold)
    )
    converted_critical = (
        float(critical_threshold) if datatype == "float" else int(critical_threshold)
    )

    if compare == "gt":
        if converted_value >= converted_critical:
            result = "NOK"
            return {"color": color_nok, "result": result}
        elif converted_value > converted_warning:
            result = "WARN"
            return {"color": color_warn, "result": result}
        else:
            result = "OK"
            return {"color": color_ok, "result": result}
    elif compare == "lt":
        if converted_value <= converted_critical:
            result = "NOK"
            return {"color": color_nok, "result": result}
        elif converted_value < converted_warning:
            result = "WARN"
            return {"color": color_warn, "result": result}
        else:
            result = "OK"
            return {"color": color_ok, "result": result}
