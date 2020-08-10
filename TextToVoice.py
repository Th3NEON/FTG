# Russian tts for Friendly-telegram: .rtts

from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils


def register(cb):
    cb(RttsMod())


class RttsMod(loader.Module):
    """Rtts - гениально простое решение для tts на русском языке"""

    strings = {'name': 'Text_To_Voice'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def rttscmd(self, event):
        """.r{текст} или .rtts как ответ на смс;
        .r {текст} как ответ - ответ голосом на смс"""
        user_msg = """{}""".format(utils.get_args_raw(event))
        global reply_and_text
        reply_and_text = False
        if event.fwd_from:
            return
        if not event.reply_to_msg_id:
            self_mess = True
            if not user_msg:
                await event.edit('<code>Вы должны или написать шото, '
                                 'или ответить на шото</code>')
                return
        elif event.reply_to_msg_id and user_msg:
            reply_message = await event.get_reply_message()
            reply_and_text = True
            self_mess = True
        elif event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            self_mess = False
            if not reply_message.text:
                await event.edit('<code>Ты на текст должен ответить, диб*ил</code>')
                return
        chat = '@aleksobot'
        await event.edit('<code>Происходит магия Деменкопа</code>')
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,
                                                             from_users=616484527))
                if not self_mess:
                    await event.client.forward_messages(chat, reply_message)
                else:
                    await event.client.send_message(chat, user_msg)
                response = await response
            except YouBlockedUserError:
                await event.reply('<code>Разблокируй @aleksobot, ибо магия не произойдёт</code>')
                return
            if response.text:
                await event.edit('<code>Бот ответил не медиа форматом, попробуйте снова</code>')
                return
            await event.delete()
            if reply_and_text:
                await event.client.send_message(event.chat_id, response.message,
                                                reply_to=reply_message.id)
            else:
                await event.client.send_message(event.chat_id, response.message)
