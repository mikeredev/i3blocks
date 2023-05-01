def check_value(value, datatype, warning_threshold, critical_threshold, compare):
    colors = {"ok": "#ffffff", "warn": "#fabd2f", "nok": "#fb4934"}
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
