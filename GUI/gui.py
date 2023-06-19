#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
import subprocess
import os
import re


MAN = """--==[ torctl.sh by blackarch.org ]==--

Usage: torctl.sh COMMAND

A script to redirect all traffic through tor network

Commands:

start      - start tor and redirect all traffic through tor

stop       - stop tor and redirect all traffic through clearnet

status     - get tor service status

restart    - restart tor and traffic rules

autowipe   - enable memory wipe at shutdown

autostart  - start torctl at startup

ip         - get remote ip address

chngid     - change tor identity

chngmac    - change mac addresses of all interfaces

rvmac      - revert mac addresses of all interfaces

version    - print version of torctl and exit"""

ABOUT = """Official Repository: blackarch.org

GUI Developer: Aleff (github.com/aleff-github)

Licence: GPLv3"""

CONTACT = """Github: https://github.com/BlackArch

Twitter: https://twitter.com/blackarchlinux/

YouTube: https://www.youtube.com/channel/UChw5hByy70ey2F7QeLEGICQ

Matrix: https://matrix.to/#/#BlackArch:matrix.org

Blog and News: https://www.blackarch.org/blog.html"""

def tmp():
    print("ok")

def get_update_lines(output: str):
    lines = output.decode("utf-8").splitlines()
    for line in lines:
        if re.search(r"^\[", line):
            info_panel.insert(tk.END, line+"\n")
    info_panel.see(tk.END)

def run_a_command(description:str, command: str):
    info_panel.configure(state="normal")
    info_panel.insert(tk.END, f"{description}\n")
    get_update_lines(subprocess.check_output(f"/usr/local/bin/torctl {command}", shell=True))
    info_panel.configure(state="disabled")

def initial_state():
    run_a_command("Your Actual IP: ", "ip")
    run_a_command("...", "status")

def start():
    run_a_command("\nSTART", "start")

def stop():
    run_a_command("\nSTOP", "stop")

def status():
    run_a_command("\nSTATUS", "status")

def restart():
    run_a_command("\nRESTART", "restart")

def autowipe():
    run_a_command("\nAUTO WIPE", "autowipe")

def autostart():
    run_a_command("\nAUTO START", "autostart")

def ip():
    run_a_command("\nYour Actual IP: ", "ip")

def chngid():
    run_a_command("\nCHANGE TOR IDENTITY", "chngid")

def chngmac():
    run_a_command("\nCHANGE MAC", "chngmac")

def rvmac():
    run_a_command("\nREVERD MAC", "rvmac")

def version():
    run_a_command("\nVERSION", "version")

def man():
    messagebox.showinfo("Popup", MAN)

def about():
    messagebox.showinfo("Popup", ABOUT)

def contact():
    messagebox.showinfo("Popup", CONTACT)

# Create main window
window = tk.Tk()
window.title("torctl - Redirect yout traffic")

# Apply a theme from the ttkthemes library
style = ThemedStyle(window)
style.set_theme("breeze")

# Create a text panel for information
info_panel = tk.Text(window, height=10, width=50)
info_panel.configure(font=("Linux Libertine", 14))
initial_state()
info_panel.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create the menu bar
toolbar = tk.Menu(window)

# Add buttons as menu bar commands
toolbar.add_command(label="Manual", command=man)
toolbar.add_command(label="About", command=about)
toolbar.add_command(label="Contact", command=contact)

# Add the menu bar to the window
window.config(menu=toolbar)

button1 = ttk.Button(window, text="Start", command=start)
button2 = ttk.Button(window, text="Stop", command=stop)
button3 = ttk.Button(window, text="Status", command=status)
button4 = ttk.Button(window, text="Restart", command=restart)
button5 = ttk.Button(window, text="Auto-Wipe", command=autowipe)
button6 = ttk.Button(window, text="Auto-Start", command=autostart)
button7 = ttk.Button(window, text="IP", command=ip)
button8 = ttk.Button(window, text="Change Identity", command=chngid)
button9 = ttk.Button(window, text="Change MAC", command=chngmac)
button10 = ttk.Button(window, text="Revert MAC", command=rvmac)
button11 = ttk.Button(window, text="Version", command=version)

button1.grid(row=1, column=0, padx=10, pady=10)
button2.grid(row=2, column=0, padx=10, pady=10)
button3.grid(row=3, column=0, padx=10, pady=10)
button4.grid(row=1, column=1, padx=10, pady=10)
button5.grid(row=2, column=1, padx=10, pady=10)
button6.grid(row=3, column=1, padx=10, pady=10)
button7.grid(row=1, column=2, padx=10, pady=10)
button8.grid(row=2, column=2, padx=10, pady=10)
button9.grid(row=3, column=2, padx=10, pady=10)
button9.grid(row=3, column=2, padx=10, pady=10)
button9.grid(row=3, column=2, padx=10, pady=10)

window.mainloop()
