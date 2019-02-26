"""File generated by TLObjects' generator. All changes will be ERASED"""
import struct
from .. import TLObject, types, custom

class MessageEmpty(custom.message.Message):
    CONSTRUCTOR_ID = 0x83e5de54
    SUBCLASS_OF_ID = 0x790009e3
    def to_dict(self):
        return {
            '_': 'MessageEmpty',
            'id': self.id
        }

    def __bytes__(self):
        return b''.join((
            b'T\xde\xe5\x83',
            struct.pack('<i', self.id),
        ))

    @classmethod
    def from_reader(cls, reader):
        _id = reader.read_int()
        return cls(id=_id)

types.MessageEmpty = MessageEmpty

class Message(custom.message.Message):
    CONSTRUCTOR_ID = 0x44f9b43d
    SUBCLASS_OF_ID = 0x790009e3
    def to_dict(self):
        return {
            '_': 'Message',
            'id': self.id,
            'to_id': self.to_id.to_dict() if isinstance(self.to_id, TLObject) else self.to_id,
            'date': self.date,
            'message': self.message,
            'out': self.out,
            'mentioned': self.mentioned,
            'media_unread': self.media_unread,
            'silent': self.silent,
            'post': self.post,
            'from_scheduled': self.from_scheduled,
            'from_id': self.from_id,
            'fwd_from': self.fwd_from.to_dict() if isinstance(self.fwd_from, TLObject) else self.fwd_from,
            'via_bot_id': self.via_bot_id,
            'reply_to_msg_id': self.reply_to_msg_id,
            'media': self.media.to_dict() if isinstance(self.media, TLObject) else self.media,
            'reply_markup': self.reply_markup.to_dict() if isinstance(self.reply_markup, TLObject) else self.reply_markup,
            'entities': [] if self.entities is None else [x.to_dict() if isinstance(x, TLObject) else x for x in self.entities],
            'views': self.views,
            'edit_date': self.edit_date,
            'post_author': self.post_author,
            'grouped_id': self.grouped_id
        }

    def __bytes__(self):
        return b''.join((
            b'=\xb4\xf9D',
            struct.pack('<I', (0 if self.out is None or self.out is False else 2) | (0 if self.mentioned is None or self.mentioned is False else 16) | (0 if self.media_unread is None or self.media_unread is False else 32) | (0 if self.silent is None or self.silent is False else 8192) | (0 if self.post is None or self.post is False else 16384) | (0 if self.from_scheduled is None or self.from_scheduled is False else 262144) | (0 if self.from_id is None or self.from_id is False else 256) | (0 if self.fwd_from is None or self.fwd_from is False else 4) | (0 if self.via_bot_id is None or self.via_bot_id is False else 2048) | (0 if self.reply_to_msg_id is None or self.reply_to_msg_id is False else 8) | (0 if self.media is None or self.media is False else 512) | (0 if self.reply_markup is None or self.reply_markup is False else 64) | (0 if self.entities is None or self.entities is False else 128) | (0 if self.views is None or self.views is False else 1024) | (0 if self.edit_date is None or self.edit_date is False else 32768) | (0 if self.post_author is None or self.post_author is False else 65536) | (0 if self.grouped_id is None or self.grouped_id is False else 131072)),
            struct.pack('<i', self.id),
            b'' if self.from_id is None or self.from_id is False else (struct.pack('<i', self.from_id)),
            bytes(self.to_id),
            b'' if self.fwd_from is None or self.fwd_from is False else (bytes(self.fwd_from)),
            b'' if self.via_bot_id is None or self.via_bot_id is False else (struct.pack('<i', self.via_bot_id)),
            b'' if self.reply_to_msg_id is None or self.reply_to_msg_id is False else (struct.pack('<i', self.reply_to_msg_id)),
            self.serialize_datetime(self.date),
            self.serialize_bytes(self.message),
            b'' if self.media is None or self.media is False else (bytes(self.media)),
            b'' if self.reply_markup is None or self.reply_markup is False else (bytes(self.reply_markup)),
            b'' if self.entities is None or self.entities is False else b''.join((b'\x15\xc4\xb5\x1c',struct.pack('<i', len(self.entities)),b''.join(bytes(x) for x in self.entities))),
            b'' if self.views is None or self.views is False else (struct.pack('<i', self.views)),
            b'' if self.edit_date is None or self.edit_date is False else (self.serialize_datetime(self.edit_date)),
            b'' if self.post_author is None or self.post_author is False else (self.serialize_bytes(self.post_author)),
            b'' if self.grouped_id is None or self.grouped_id is False else (struct.pack('<q', self.grouped_id)),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _out = bool(flags & 2)
        _mentioned = bool(flags & 16)
        _media_unread = bool(flags & 32)
        _silent = bool(flags & 8192)
        _post = bool(flags & 16384)
        _from_scheduled = bool(flags & 262144)
        _id = reader.read_int()
        if flags & 256:
            _from_id = reader.read_int()
        else:
            _from_id = None
        _to_id = reader.tgread_object()
        if flags & 4:
            _fwd_from = reader.tgread_object()
        else:
            _fwd_from = None
        if flags & 2048:
            _via_bot_id = reader.read_int()
        else:
            _via_bot_id = None
        if flags & 8:
            _reply_to_msg_id = reader.read_int()
        else:
            _reply_to_msg_id = None
        _date = reader.tgread_date()
        _message = reader.tgread_string()
        if flags & 512:
            _media = reader.tgread_object()
        else:
            _media = None
        if flags & 64:
            _reply_markup = reader.tgread_object()
        else:
            _reply_markup = None
        if flags & 128:
            reader.read_int()
            _entities = []
            for _ in range(reader.read_int()):
                _x = reader.tgread_object()
                _entities.append(_x)

        else:
            _entities = None
        if flags & 1024:
            _views = reader.read_int()
        else:
            _views = None
        if flags & 32768:
            _edit_date = reader.tgread_date()
        else:
            _edit_date = None
        if flags & 65536:
            _post_author = reader.tgread_string()
        else:
            _post_author = None
        if flags & 131072:
            _grouped_id = reader.read_long()
        else:
            _grouped_id = None
        return cls(id=_id, to_id=_to_id, date=_date, message=_message, out=_out, mentioned=_mentioned, media_unread=_media_unread, silent=_silent, post=_post, from_scheduled=_from_scheduled, from_id=_from_id, fwd_from=_fwd_from, via_bot_id=_via_bot_id, reply_to_msg_id=_reply_to_msg_id, media=_media, reply_markup=_reply_markup, entities=_entities, views=_views, edit_date=_edit_date, post_author=_post_author, grouped_id=_grouped_id)

types.Message = Message

class MessageService(custom.message.Message):
    CONSTRUCTOR_ID = 0x9e19a1f6
    SUBCLASS_OF_ID = 0x790009e3
    def to_dict(self):
        return {
            '_': 'MessageService',
            'id': self.id,
            'to_id': self.to_id.to_dict() if isinstance(self.to_id, TLObject) else self.to_id,
            'date': self.date,
            'action': self.action.to_dict() if isinstance(self.action, TLObject) else self.action,
            'out': self.out,
            'mentioned': self.mentioned,
            'media_unread': self.media_unread,
            'silent': self.silent,
            'post': self.post,
            'from_id': self.from_id,
            'reply_to_msg_id': self.reply_to_msg_id
        }

    def __bytes__(self):
        return b''.join((
            b'\xf6\xa1\x19\x9e',
            struct.pack('<I', (0 if self.out is None or self.out is False else 2) | (0 if self.mentioned is None or self.mentioned is False else 16) | (0 if self.media_unread is None or self.media_unread is False else 32) | (0 if self.silent is None or self.silent is False else 8192) | (0 if self.post is None or self.post is False else 16384) | (0 if self.from_id is None or self.from_id is False else 256) | (0 if self.reply_to_msg_id is None or self.reply_to_msg_id is False else 8)),
            struct.pack('<i', self.id),
            b'' if self.from_id is None or self.from_id is False else (struct.pack('<i', self.from_id)),
            bytes(self.to_id),
            b'' if self.reply_to_msg_id is None or self.reply_to_msg_id is False else (struct.pack('<i', self.reply_to_msg_id)),
            self.serialize_datetime(self.date),
            bytes(self.action),
        ))

    @classmethod
    def from_reader(cls, reader):
        flags = reader.read_int()

        _out = bool(flags & 2)
        _mentioned = bool(flags & 16)
        _media_unread = bool(flags & 32)
        _silent = bool(flags & 8192)
        _post = bool(flags & 16384)
        _id = reader.read_int()
        if flags & 256:
            _from_id = reader.read_int()
        else:
            _from_id = None
        _to_id = reader.tgread_object()
        if flags & 8:
            _reply_to_msg_id = reader.read_int()
        else:
            _reply_to_msg_id = None
        _date = reader.tgread_date()
        _action = reader.tgread_object()
        return cls(id=_id, to_id=_to_id, date=_date, action=_action, out=_out, mentioned=_mentioned, media_unread=_media_unread, silent=_silent, post=_post, from_id=_from_id, reply_to_msg_id=_reply_to_msg_id)

types.MessageService = MessageService
