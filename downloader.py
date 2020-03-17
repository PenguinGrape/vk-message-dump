import os
import sys
import json
from dumperUtils import clear
# from main import getch


def downloader(mes):
    for message in mes:
        if 'attachments' in message:
            for attachment in message['attachments']:
                pass
    pass


def main():
    clear()
    print("Dir with attachments will be created where json is.\nWhat dialog to parse? (example: /tmp/dialog.json)")
    jsonpath = input()
    if '/' not in jsonpath:
        path = os.getcwd() + '/'
    else:
        filename = jsonpath.split('/')[-1]
        path = jsonpath.split(filename)[0]
    clear()
    try:
        jsonfile = open(jsonpath, "r")
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
            # TODO check another types
            dirs = ['photo', 'video', 'audio', 'doc']
            for i in dirs:
                if not os.path.exists(path + i):
                    os.makedirs(path + i)
            # TODO check what api writes into json and fix keys
            downloader(jsoncontent['response']['items'])
            pass


if __name__ == '__main__':
    main()
