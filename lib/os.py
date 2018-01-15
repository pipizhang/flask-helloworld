import os

def uname(show_all=False):
    arg = "-a" if show_all else ""
    return os.popen("uname %s" % arg).read().strip()

def top():
    return os.popen("top -n 1 -b").read().strip()

def whoami():
    return os.popen("whoami").read().strip()

def df():
    return os.popen("df -h").read().strip()

def cpu():
    return os.popen("lscpu").read().strip()
