import os
import sys
import json
# from main import getch


def downloader(mes):
    print(mes)
    pass


def main():
    os.system('clear')
    print("Dir with attachments will be created where json is.\nWhat dialog to parse? (example: /tmp/dialog.json)")
    path = input()
    os.system('clear')
    try:
        jsonfile = open(path, "r")
    except FileNotFoundError:
        print("Can't read specified json. Does file exist?", file=sys.stderr)
        exit(1)
    else:
        try:
            jsoncontent = json.load(jsonfile)
        except json.decoder.JSONDecodeError:
            print("It's not a correct json!", file=sys.stderr)
            exit(1)
        else:
            downloader(jsoncontent)
            pass
