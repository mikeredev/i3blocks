#!/usr/bin/env python3
import customtkinter
import subprocess

customtkinter.set_appearance_mode("dark")

root = customtkinter.CTk()
root.attributes("-type", "dialog")
root.geometry("400x180+1510+11")


def system_control(option):
    if option == "lock":
        subprocess.run(["i3lock"])
    elif option == "logoff":
        subprocess.run(["i3-msg", "exit"])
    elif option == "suspend":
        subprocess.run(["systemctl", "suspend"])
    elif option == "reboot":
        subprocess.run(["systemctl", "reboot"])
    elif option == "shutdown":
        subprocess.run(["systemctl", "poweroff"])
    else:
        print("Invalid option")


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
