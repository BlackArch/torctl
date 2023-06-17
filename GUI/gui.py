#!/usr/bin/env python3

import tkinter as tk
from tkinter import ttk, messagebox
from ttkthemes import ThemedStyle
import subprocess
import os
import re


# Verifica se lo script è stato eseguito con i permessi di root
if os.geteuid() != 0:
    messagebox.showinfo("Popup", "You must run the app with sudo permissions.")
    exit()

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

CONTACT = """Github: https://github.com/aleff-github

Instagram: https://www.instagram.com/alessandro_greco_aka_aleff/

Linkeding: https://www.linkedin.com/in/alessandro-greco-aka-aleff/"""

def tmp():
    print("ok")

def get_update_lines(output: str):
    lines = output.decode("utf-8").splitlines()
    for line in lines:
        if re.search(r"^\[", line):
            info_panel.insert(tk.END, line+"\n")
    info_panel.see(tk.END)

def initial_state():
    get_update_lines(subprocess.check_output("sudo torctl ip", shell=True))
    get_update_lines(subprocess.check_output("sudo torctl status", shell=True))

def start():
    info_panel.configure(state="normal")
    info_panel.insert(tk.END, "\n\nSTART\n")
    get_update_lines(subprocess.check_output("sudo torctl start", shell=True))
    info_panel.configure(state="disabled")

def stop():
    info_panel.configure(state="normal")
    info_panel.insert(tk.END, "\n\nSTOP\n")
    get_update_lines(subprocess.check_output("sudo torctl stop", shell=True))
    info_panel.configure(state="disabled")

def status():
    info_panel.configure(state="normal")
    info_panel.insert(tk.END, "\n\nSTATUS\n")
    get_update_lines(subprocess.check_output("sudo torctl status", shell=True))
    info_panel.configure(state="disabled")

def restart():
    info_panel.configure(state="normal")
    info_panel.insert(tk.END, "\n\nRESTART\n")
    get_update_lines(subprocess.check_output("sudo torctl restart", shell=True))
    info_panel.configure(state="disabled")

def autowipe():
    info_panel.configure(state="normal")
    info_panel.insert(tk.END, "\n\nAUTO WIPE\n")
    get_update_lines(subprocess.check_output("sudo torctl autowipe", shell=True))
    info_panel.configure(state="disabled")

def autostart():
    info_panel.configure(state="normal")
    info_panel.insert(tk.END, "\n\nAUTO START\n")
    get_update_lines(subprocess.check_output("sudo torctl autostart", shell=True))
    info_panel.configure(state="disabled")

def ip():
    info_panel.configure(state="normal")
    info_panel.insert(tk.END, "\n\nWHAT IS MY IP?\n")
    get_update_lines(subprocess.check_output("sudo torctl ip", shell=True))
    info_panel.configure(state="disabled")

def chngid():
    info_panel.configure(state="normal")
    info_panel.insert(tk.END, "\n\nCHANGE TOR IDENTITY\n")
    get_update_lines(subprocess.check_output("sudo torctl chngid", shell=True))
    info_panel.configure(state="disabled")

def chngmac():
    info_panel.configure(state="normal")
    info_panel.insert(tk.END, "\n\nCHANGE MAC\n")
    get_update_lines(subprocess.check_output("sudo torctl chngmac", shell=True))
    info_panel.configure(state="disabled")

def rvmac():
    info_panel.configure(state="normal")
    info_panel.insert(tk.END, "\n\nREVERD MAC\n")
    get_update_lines(subprocess.check_output("sudo torctl rvmac", shell=True))
    info_panel.configure(state="disabled")

def version():
    info_panel.configure(state="normal")
    info_panel.insert(tk.END, "\n\nVERSION\n")
    get_update_lines(subprocess.check_output("sudo torctl version", shell=True))
    info_panel.configure(state="disabled")

def man():
    messagebox.showinfo("Popup", MAN)

def about():
    messagebox.showinfo("Popup", ABOUT)

def contact():
    messagebox.showinfo("Popup", CONTACT)

# Create main window
window = tk.Tk()
window.title("TORCTL by Aleff")

# Apply a theme from the ttkthemes library
style = ThemedStyle(window)
style.set_theme("breeze")

# Create a text panel for information
info_panel = tk.Text(window, height=10, width=50)
info_panel.configure(font=("Linux Libertine", 14))
initial_state()
info_panel.configure(state="disabled")
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
