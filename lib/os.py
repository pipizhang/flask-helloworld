import os

def uname(show_all):
    arg = "-a" if show_all else ""
    return os.popen("uname %s" % arg).read()

def top():
    return os.popen("top -n 1 -b").read()

def whoami():
    return os.popen("whoami").read()

def df():
    return os.popen("df -h").read()

def cpu():
    return os.popen("lscpu").read()
