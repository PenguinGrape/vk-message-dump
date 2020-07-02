class Attachment(object):
    """
    Attachment types:
    photo, video, audio_message, doc
    """
    # TODO gift sticker audio link video

    def __init__(self, attachment):
        if 'type' in attachment:
            self.type = attachment['type']
        else:
            self.type = None
        self.subtype = None
        if self.type == 'photo':
            sizes = attachment['photo']['sizes']
            maxw = 0
            for size in sizes:
                if size['width'] > maxw and size['type'] not in "opqr":
                    self.url = size['url']
                    maxw = size['width']
            if self.url:
                self.owner = attachment['photo']['owner_id']
                self.extension = ".jpg"
        if self.type == 'video':
            # TODO ну тут говно ебейшее, надо апишку дергать. наверное.
            pass
        if self.type == 'audio_message':
            self.url = attachment['audio_message']['link_mp3']
            self.owner = attachment['audio_message']['owner_id']
            self.extension = ".mp3"
        if self.type == 'doc':
            self.subtype = {1: 'text_documents',
                            2: 'archives',
                            3: 'gifs',
                            4: 'images',
                            5: 'audios',
                            6: 'videos',
                            7: "e-books",
                            8: 'unknown'
                            }[attachment['doc']['type']]
            self.url = attachment['doc']['url']
            self.owner = attachment['doc']['owner_id']
            self.extension = f'.{attachment["doc"]["ext"]}'
            pass


class Message(object):
    """
    All messages have this fields:
    - date and time of message
    - who sent message
    - id of message
    - who received message
    - is it important
    Optional fields:
    - text of message
    - attachments
    - forwarded messages (id only?)
    """

    def __init__(self, message):
        self.date = message['date']
        self.sender = message['from_id']
        self.id = message['id']
        self.receiver = message['peer_id']
        self.important = message['important']
        self.text = ""
        if 'text' in message:
            self.text = message['text']
        self.attachments = []
        if 'attachments' in message:
            for attachment in message['attachments']:
                self.attachments.append(Attachment(attachment))
        self.fwd = []
        if 'fwd_messages' in message:
            for fwd in message['fwd_messages']:
                self.fwd.append(fwd)
