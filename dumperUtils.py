import os
import sys
import tty
import termios
import urllib.request


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
