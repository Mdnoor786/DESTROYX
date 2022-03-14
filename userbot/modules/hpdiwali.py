import asyncio
import random

from telethon import events, functions, types, utils

from userbot import bot as borg


def choser(cmd, pack, blacklist={}):
    docs = None

    @borg.on(events.NewMessage(pattern=rf"\.{cmd}", outgoing=True))
    async def handler(event):

        if event.fwd_from:
            return
        animation_interval = 3
        animation_ttl = range(5)
        nonlocal docs

        for _ in animation_ttl:
            await asyncio.sleep(animation_interval)
            if docs is None:
                docs = [
                    utils.get_input_document(x)
                    for x in (
                        await borg(
                            functions.messages.GetStickerSetRequest(
                                types.InputStickerSetShortName(pack)
                            )
                        )
                    ).documents
                ]

            await event.respond(file=random.choice(docs))


choser("hpdiwali", "a929138153_by_Shivam_Patel_1_anim")
