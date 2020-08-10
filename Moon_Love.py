import asyncio
import time
from userbot import CMD_HELP, ZALG_LIST
from userbot.events import register



@register(outgoing=True, pattern='^.moon(?: |$)(.*)')
async def mun(typew):
    for _ in range(50):
        await typew.edit("🌚")
        await asyncio.sleep(0.3)
        await typew.edit("🌝")
        await asyncio.sleep(0.3)

@register(outgoing=True, pattern='^.love(?: |$)(.*)')
async def mun(typew):
    for _ in range(10):
        await typew.edit("🧡")
        await asyncio.sleep(0.5)
        await typew.edit("💛")
        await asyncio.sleep(0.5)
        await typew.edit("💚")
        await asyncio.sleep(0.5)
        await typew.edit("💙")
        await asyncio.sleep(0.5)
        await typew.edit("💜")
        await asyncio.sleep(0.5)
        await typew.edit("🖤")
        await asyncio.sleep(0.5)
