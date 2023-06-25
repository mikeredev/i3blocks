from datetime import datetime


def check(warning=None, critical=None):
    time_str = datetime.now().strftime("%d/%m %H:%M")
    print(f"{time_str} <span font='FontAwesome'>\uf017</span>")
