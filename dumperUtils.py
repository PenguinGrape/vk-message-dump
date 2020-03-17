import os


def clear():
    if 'TERM' in os.environ:
        os.system('clear')
