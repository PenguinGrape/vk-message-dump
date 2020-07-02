import sys
import json
from models import Message
from dumperUtils import clear, getch, whois, ptime


def main():
    clear()
    json_path = input("Enter path to json file: ")
    print(f"{json_path}.txt will be overwritten!")
    try:
        filecontent = open(json_path, "r").read()
    except FileNotFoundError:
        print("There is no such file!", file=sys.stderr)
        exit(1)
    else:
        parsed = {}
        try:
            parsed = json.loads(filecontent)
        except json.JSONDecodeError as error:
            if error.msg == "Expecting property name enclosed in double quotes":
                print("Seems like your json has ' instead of \". You can try to parse it with eval(), but this func "
                      "is RCE possible. Do you want it? [Y/n] ", end="", flush=True)
                ch = getch().upper()
                if ch == 'Y':
                    parsed = eval(filecontent)
                else:
                    print("Failed to parse json file!", file=sys.stderr)
                    exit(1)
        messages = parsed['items']
        try:
            writer = open(f"{json_path}.txt", 'w')
        except (PermissionError, OSError):
            print("Failed to create new file at this location! (Read only fs?)", file=sys.stderr)
            exit(1)
        else:
            for m in messages:
                message = Message(m)
                writer.write(f"{whois(message.sender)} {ptime(message.date)} {message.id}\n{message.text}")
                if message.text:
                    writer.write("\n")
                if message.attachments:
                    writer.write("Вложения:\n")
                    counter = -1
                    for attachment in message.attachments:
                        counter += 1
                        try:
                            writer.write(f"  {attachment.type} {attachment.url}\n")
                        except AttributeError:
                            writer.write(f"  Unsupported type: {m['attachments'][0]['type']}")
                    writer.write("\n")
                # TODO a normal forwarded parser
                if message.fwd:
                    writer.write("Пересланные сообщения:\n")
                    for fwd in message.fwd:
                        writer.write(f"  {fwd}")
                    writer.write("\n")
                writer.write("\n\n")
