from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError
from .. import loader, utils


def register(cb):
    cb(QuotLyMod())


class QuotLyMod(loader.Module):
    """Простой цитатник"""

    strings = {'name': 'Текст на гиф'}

    def __init__(self):
        self.name = self.strings['name']
        self._me = None
        self._ratelimit = []

    async def client_ready(self, client, db):
        self._db = db
        self._client = client
        self.me = await client.get_me()

    async def dmcmd(self, event):
        """.qq <reply>"""
        user_msg = """{}""".format(utils.get_args_raw(event))
        reply_and_text = False
        if event.fwd_from:
            return
        if not event.reply_to_msg_id:
            self_mess = True
            if not user_msg:
                return
        elif event.reply_to_msg_id and user_msg:
            reply_message = await event.get_reply_message()
            reply_and_text = True
            self_mess = True
        elif event.reply_to_msg_id:
            reply_message = await event.get_reply_message()
            self_mess = False
            if not reply_message.text:
                return
        chat = '@super_rjaka_demotivator_bot'
        await event.edit('<code>Жду ответа от генератора...</code>')
        async with event.client.conversation(chat) as conv:
            try:
                response = conv.wait_event(events.NewMessage(incoming=True,
                                                             from_users=1016409811))
                if not self_mess:
                    await event.client.forward_messages(chat, reply_message)
                else:
                    await event.client.send_message(chat, user_msg)
                response = await response
            except YouBlockedUserError:
                await event.reply('<code>Разблокируй </code> @super_rjaka_demotivator_bot')
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
