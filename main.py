import sys
import termios
from dumperUtils import getch


def main():
    print("This is vk messages dumper. It can:\n1) Dump all messages to json\n2) Download all attachments from dumped "
          "json\n3) Parse json to html (or txt)\n4) Real time dumping with lonpoll\n0) exit\nChoose what you wnat to "
          "do:")
    try:
        choice = getch()
    except termios.error:
        print("Your terminal doesn't support RT input!", file=sys.stderr)
        choice = input()
    if choice == '0':
        exit(0)
    if choice == '1':
        from jsondump import main as dumper
        dumper()
    if choice == '2':
        from downloader import main as downloader
        downloader()
    if choice == '3':
        from htmlCreator import main as parser
        parser()
    if choice == '4':
        from longpoll import main as rt_dumper
        rt_dumper()
    else:
        print("There is no such option!", file=sys.stderr)
        exit(1)


if __name__ == '__main__':
    main()
