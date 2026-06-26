import subprocess
import tkinter as tk
from tkinter import messagebox

BYPASS_Process = [
    'net user defaultuser0 ""',
    'reg add "HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\OOBE" /v BypassNRO /t REG_DWORD /d 1 /f',
    'shutdown /r /t 0'
]


message = (
    "This Tool Is Made By BO7MEDX\n\n"
    "BypassNRO For Windows 11 25H2\n\n"
    "Discord: @bo7medx\n\n"
    "Press OK when you are ready to restart."
)

def bypass_and_clear_password():
    root = tk.Tk()
    root.withdraw()
    root.attributes("-topmost", True)
    messagebox.showinfo("info", message, parent=root)
    root.destroy()
    
    for process in BYPASS_Process:
        try:
            subprocess.run(process, shell=True, creationflags=subprocess.CREATE_NO_WINDOW)
        except Exception:
    	    pass


if __name__ == "__main__":
    bypass_and_clear_password()
