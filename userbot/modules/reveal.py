import os

from userbot import CMD_HELP
from userbot import bot as borg
from userbot.utils import admin_cmd


@borg.on(admin_cmd(pattern=r"reveal", outgoing=True))
async def _(event):
    b = await event.client.download_media(await event.get_reply_message())
    with open(b, "r") as a:
        c = a.read()
    a = await event.reply("Reading file...")
    if len(c) > 4095:
        await a.edit(
            "The Total words in this file is more than a bitch can write this file is useless👍."
        )
    else:
        await event.client.send_message(event.chat_id, f"{c}")
        await a.delete()
    os.remove(b)


CMD_HELP.update(
    {
        "reveal": ".reveal <reply to a file>\nUse - Read contents of file and send as a telegram message."
    }
)
