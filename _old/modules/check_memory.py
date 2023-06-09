try:
    import psutil
    from .functions import check_value
except ImportError as e:
    print(f"Check failed: {e}")


def check(warning, critical):
    try:
        output = round(psutil.virtual_memory().percent)
        color = check_value(output, "int", warning, critical, "gt")
        icon = f"<span font='FontAwesome' foreground='{color}'>\uf201</span>"
        print(f"{output}% {icon}")
    except ImportError as e:
        print(f"Check failed: {e}")
