import os
import sys
import time
import json
import termios
from main import getch
from dumperUtils import clear, download, whois


# TODO check another types
def menu():
    clear()
    print("What would you like to download?\n1) Only photos\n2) Only videos\n3) Only audios\n4) Only "
          "documents\n5)Multiple choice\n0) Exit")
    try:
        choice = getch()
    except termios.error:
        choice = input()
    if choice == '0':
        exit()
    if choice == '1':
        return ['photo']
    if choice == '2':
        return ['video']
    if choice == '3':
        return ['audio_message']
    if choice == '4':
        return ['doc']
    if choice == '5':
        clear()
        print("Enter numbers of attachment types (example: 1 2 4)\nAttachments:\n1) Photos\n2) Videos\n3) Audios\n4) "
              "Documents")
        multichoice = input().split(' ')
        attachments = []
        for i in multichoice:
            if i not in '1234':
                print("There is no such option!", file=sys.stderr)
                exit(1)
            else:
                if i == '1':
                    attachments.append('photo')
                    continue
                if i == '2':
                    attachments.append('video')
                    continue
                if i == '3':
                    attachments.append('audio_message')
                    continue
                if i == '4':
                    attachments.append('doc')
                    continue
        return attachments
    else:
        print("There is no such option!", file=sys.stderr)
        exit(1)


def downloader(mes, path, requested):
    for message in mes:
        if 'attachments' in message:
            for attachment in message['attachments']:
                if attachment['type'] in requested:
                    if attachment['type'] == 'photo':
                        sizes = attachment['photo']['sizes']
                        maxw = 0
                        url = None
                        for size in sizes:
                            if size['width'] > maxw and size['type'] not in "opqr":
                                url = size['url']
                                maxw = size['width']
                        if url:
                            uid = attachment['photo']['owner_id']
                            download(url, f"{path}photo/{time.time()}_{whois(uid)}.jpg")
                        else:
                            raise Exception("What the fuck, man??")
                    if attachment['type'] == 'video':
                        pass
                    if attachment['type'] == 'audio_message':
                        url = attachment['audio_message']['link_mp3']
                        uid = attachment['audio_message']['owner_id']
                        download(url, f"{path}audio_message/{time.time()}_{whois(uid)}.mp3")
                    if attachment['type'] == 'doc':
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
    dirs = menu()
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
            for i in dirs:
                if not os.path.exists(path + i):
                    os.makedirs(path + i)
            # TODO check what api writes into json and fix keys
            downloader(jsoncontent['response']['items'], path, dirs)
            pass


if __name__ == '__main__':
    main()
