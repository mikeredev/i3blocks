#!/usr/bin/env python3
import customtkinter
import os
import subprocess

dir_path = os.path.dirname(os.path.realpath(__file__))
style_path = os.path.join(dir_path, "..", "styles/", "session_manager.json")
customtkinter.set_default_color_theme(style_path)

root = customtkinter.CTk()
root.attributes("-type", "splash")
root.geometry("400x180+1510+5")
root.overrideredirect(True)


def close_gui():
    root.destroy()


def system_control(option):
    actions = {
        "lock": lambda: [close_gui(), subprocess.run(["i3lock"])],
        "logoff": lambda: subprocess.run(["i3-msg", "exit"]),
        "suspend": lambda: [
            close_gui(),
            subprocess.run(["i3lock"]),
            subprocess.run(["systemctl", "suspend"]),
        ],
        "reboot": lambda: subprocess.run(["systemctl", "reboot"]),
        "shutdown": lambda: subprocess.run(["systemctl", "poweroff"]),
    }

    action = actions.get(option)
    if action:
        action()


def main():
    frame1 = customtkinter.CTkFrame(master=root)
    frame1.grid(row=0, column=0, pady=20, padx=20, sticky="nsw")

    button_lock = customtkinter.CTkButton(
        master=frame1, text="Lock", command=lambda: system_control("lock")
    )
    button_lock.grid(row=0, column=0, padx=20, pady=10, sticky="e")

    button_logoff = customtkinter.CTkButton(
        master=frame1, text="Logoff", command=lambda: system_control("logoff")
    )
    button_logoff.grid(row=1, column=0, padx=20, pady=10, sticky="e")

    button_suspend = customtkinter.CTkButton(
        master=frame1, text="Suspend", command=lambda: system_control("suspend")
    )
    button_suspend.grid(row=2, column=0, padx=20, pady=10, sticky="e")

    button_reboot = customtkinter.CTkButton(
        master=frame1, text="Reboot", command=lambda: system_control("reboot")
    )
    button_reboot.grid(row=0, column=1, padx=20, pady=10, sticky="w")

    button_shutdown = customtkinter.CTkButton(
        master=frame1, text="Shutdown", command=lambda: system_control("shutdown")
    )
    button_shutdown.grid(row=1, column=1, padx=20, pady=10, sticky="w")

    button_cancel = customtkinter.CTkButton(master=frame1, text="Cancel", command=quit)
    button_cancel.grid(row=2, column=1, padx=20, pady=10, sticky="w")

    root.mainloop()


if __name__ == "__main__":
    main()
