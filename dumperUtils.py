import os
import sys
import tty
import termios
import urllib.request
from datetime import datetime


def clear():
    if 'TERM' in os.environ:
        os.system('clear')


def download(url, filename):
    urllib.request.urlretrieve(url, filename)


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def whois(uid):
    # TODO parse username (when api will be ready)
    # TODO database with uid:uname maybe?
    return str(uid)


def ptime(utime):
    return datetime.utcfromtimestamp(utime).strftime('%d.%m.%Y %H:%M:%S')
