
from .. import loader, utils

from telethon.errors.rpcerrorlist import MessageNotModifiedError

import logging
import asyncio

logger = logging.getLogger(__name__)


@loader.tds
class textMod(loader.Module):
    """Автор странный чел by @laciamemeframe"""
    
    strings = {"name": "Текстовая анимация",
               "no_message": "<b>...🏳️‍🌈Нихуя🏳️‍🌈!</b>",
               "type_char_cfg_doc": "Персонаж для гей оргии🏳️‍🌈",
               "delay_typer_cfg_doc": "Как долго будет длиться гей-оргия🏳️‍🌈",
               "delay_text_cfg_doc": "Как долго будет длиться оргазм🏳️‍🌈"}

    def __init__(self):
        self.config = loader.ModuleConfig("DELAY_TYPER", 0.10, lambda m: self.strings("delay_typer_cfg_doc", m),
                                          "DELAY_TEXT", 0.5, lambda m: self.strings("delay_text_cfg_doc", m))

    @loader.ratelimit
    async def textcmd(self, message):
        """Делает сообщение с анимацией бегущей строки (🏳️‍🌈Срет в логи🏳️‍🌈) .text <сообщение>"""
        a = utils.get_args_raw(message)
        if not a:
            await utils.answer(message, self.strings("no_message", message))
            return
        for c in a:
            a = a[-1]+a[0:-1]
            message = await utils.answer(message, "⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠"+a+"⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠⁠")
            await asyncio.sleep(0.02)


