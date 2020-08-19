
from telethon import events

import asyncio

from uniborg.util import admin_cmd



@borg.on(admin_cmd(pattern="phub"))

async def _(event):

    if event.fwd_from:

        return

    animation_interval = 0.5

    animation_ttl = range(0, 101)

    await event.edit("pornhub")

    animation_chars = [

            "P_",

            "PO_",

            "POR_",

            "PORN_",
            
            "PORNH_",
            
            "PORNHU_",
            
           "PORNHUB_", 
           
           "PORNHUB",

        ]
