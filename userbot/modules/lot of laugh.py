import asyncio

from userbot import bot as javes
from userbot.utils import admin_cmd


@javes.on(admin_cmd("luul"))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 1
    animation_ttl = range(101)
    await event.edit("LOL HAHA ... !!!")
    animation_chars = [
        "😂🤣😂🤣😂🤣😂🤣😂🤣",
        "🤣😂🤣😂🤣😂🤣😂🤣😂",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 2])
