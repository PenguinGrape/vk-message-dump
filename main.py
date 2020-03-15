import sys
import tty
import termios


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(fd)
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def main():
    print("This is vk messages dumper. It can:\n1) Dump all messages to json\n2) Download all attachments from dumped json\n3) Parse json to html (or txt)\n4) Real time dumping with lonpoll\n0) exit\nChoose what you wnat to do:")
    try:
        choice = getch()
    except termios.error:
        print("Your terminal doesn't support RT input!", file=sys.stderr)
        choice = input()
    if choice == '0':
        exit(0)


if __name__ == '__main__':
    main()