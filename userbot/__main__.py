import glob
import os
import sys
from sys import *

from telethon.tl.types import InputMessagesFilterDocument

from userbot import *
from userbot.javes_main.commands import *

javes = tgbot = bot.tgbot = client
import logging
from importlib import import_module

from telethon.tl.types import InputMessagesFilterDocument

logging.basicConfig(
    format="[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s", level=logging.WARNING
)

#####################################
plugin_channel = "@DXplugins"
#####################################


async def a():
    LOGS.info("Connecting...")
    o = o2 = o3 = o4 = ""
    try:
        await client.start()
        LOGS.info("client connected")
        o = "Client1"
    except:
        LOGS.info("Telegram String Session Wrong or Expired Please Add new one ")
        quit(1)
    if client2:
        try:
            await client2.start()
            LOGS.info("client2 connected")
            o2 = ", Client2"
        except:
            LOGS.info(
                "client2 Session string Wrong/Expired Please add new string session or delete var S2"
            )
            quit(1)
    if client3:
        try:
            await client3.start()
            LOGS.info("client3 connected")
            o3 = ", Client3"
        except:
            LOGS.info(
                "client3 Session string Wrong/Expired Please add new string  or delete var S3 "
            )
            quit(1)
    if tebot:
        try:
            await tebot.start()
            LOGS.info("Telegram Bot connected")
            o4 = ", TGBot"
        except:
            LOGS.info(
                "Bot Token Wrong/ Expired please add new one  or delete var BOT_TOKEN "
            )
            quit(1)
    test1 = await client.get_messages(
        plugin_channel, None, filter=InputMessagesFilterDocument
    )
    total = int(test1.total)
    total_doxx = range(total)
    for ixo in total_doxx:
        mxo = test1[ixo].id
        await client.download_media(
            await client.get_messages(cIient, ids=mxo), "userbot/modules/"
        )
    ar = glob.glob("userbot/modules/*.py")
    f = len(ar)
    LOGS.info(f" loading {f} modules it may take 1 minute please wait")
    for la, i in enumerate(ar, start=1):
        br = os.path.basename(i)
        cr = os.path.splitext(br)[0]
        import_module(f"userbot.modules.{cr}")
        LOGS.info(f" loaded {la}/{f} modules")
    # os.system("rm userbot/modules/*.py") ;
    LOGS.info(
        f"Sucessfully connected with {o}{o2}{o3}{o4} check it by typing !destroyx in any client's chat, type !help for more info."
    )

    if len(argv) in {1, 3, 4}:
        await javes.run_until_disconnected()
        os.execl(sys.executable, sys.executable, *sys.argv)
        quit()
    else:
        await javes.disconnect()
    javes.start()


javes.loop.run_until_complete(a())
