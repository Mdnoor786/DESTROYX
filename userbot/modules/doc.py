# by @mrconfused (@sandy1709) Bhadwa hai Ye Cat Userbot Ka Owner

import os

from userbot import bot as borg
from userbot.utils import admin_cmd

if not os.path.isdir("./temp"):
    os.makedirs("./temp")


@borg.on(admin_cmd(pattern="doc ?(.*)"))
async def get(event):
    name = event.text[5:]
    if name is None:
        await event.edit("reply to text message as `.ttf <file name>`")
        return
    m = await event.get_reply_message()
    if m.text:
        with open(name, "w") as f:
            f.write(m.message)
        await event.delete()
        await event.client.send_file(event.chat_id, name, force_document=True)
        os.remove(name)
    else:
        await event.edit("reply to text message as `.ttf <file name>`")
