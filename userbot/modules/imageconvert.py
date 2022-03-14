"""Rename Telegram Files
Syntax:
.rename file.name
.rnupload file.name
.rnstreamupload file.name
By @Ck_ATR"""

import os
import time
from datetime import datetime

from userbot import bot as javes
from userbot.javes_main.heroku_var import *
from userbot.utils import admin_cmd

config = Config

thumb_image_path = f"{Config.TEMP_DOWNLOAD_DIRECTORY}/thumb_image.jpeg"


@javes.on(admin_cmd("pti (.*)"))
async def _(event):
    if event.fwd_from:
        return
    thumb = thumb_image_path if os.path.exists(thumb_image_path) else None
    await event.edit(
        "Rename & Upload in process 🙄🙇‍♂️🙇‍♂️🙇‍♀️ It might take some time if file size is big"
    )
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = f"{input_str}.ico"
        reply_message = await event.get_reply_message()
        to_download_directory = Config.TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await javes.download_media(
            reply_message, downloaded_file_name
        )
        end = datetime.now()
        ms_one = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            time.time()
            await javes.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=False,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
            )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await event.edit(
                f"Downloaded in {ms_one} seconds. Uploaded in {ms_two} seconds."
            )

        else:
            await event.edit(f"File Not Found {input_str}")
    else:
        await event.edit("Syntax // .pti<name>  as reply to a photo")


@javes.on(admin_cmd("pts (.*)"))
async def _(event):
    if event.fwd_from:
        return
    thumb = thumb_image_path if os.path.exists(thumb_image_path) else None
    await event.edit(
        "Rename & Upload in process 🙄🙇‍♂️🙇‍♂️🙇‍♀️ It might take some time if file size is big"
    )
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = f"{input_str}.webp"
        reply_message = await event.get_reply_message()
        to_download_directory = Config.TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await javes.download_media(
            reply_message, downloaded_file_name
        )
        end = datetime.now()
        ms_one = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            time.time()
            await javes.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=False,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
            )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await event.edit(
                f"Downloaded in {ms_one} seconds. Uploaded in {ms_two} seconds."
            )

        else:
            await event.edit(f"File Not Found {input_str}")
    else:
        await event.edit("Syntax // .pts<name> as reply to a Telegram media")


@javes.on(admin_cmd("vtg (.*)"))
async def _(event):
    if event.fwd_from:
        return
    thumb = thumb_image_path if os.path.exists(thumb_image_path) else None
    await event.edit(
        "Rename & Upload in process 🙄🙇‍♂️🙇‍♂️🙇‍♀️ It might take some time if file size is big"
    )
    input_str = event.pattern_match.group(1)
    if not os.path.isdir(Config.TEMP_DOWNLOAD_DIRECTORY):
        os.makedirs(Config.TEMP_DOWNLOAD_DIRECTORY)
    if event.reply_to_msg_id:
        start = datetime.now()
        file_name = f"{input_str}.gif"
        reply_message = await event.get_reply_message()
        to_download_directory = Config.TEMP_DOWNLOAD_DIRECTORY
        downloaded_file_name = os.path.join(to_download_directory, file_name)
        downloaded_file_name = await javes.download_media(
            reply_message, downloaded_file_name
        )
        end = datetime.now()
        ms_one = (end - start).seconds
        if os.path.exists(downloaded_file_name):
            time.time()
            await javes.send_file(
                event.chat_id,
                downloaded_file_name,
                force_document=False,
                supports_streaming=False,
                allow_cache=False,
                reply_to=event.message.id,
                thumb=thumb,
            )
            end_two = datetime.now()
            os.remove(downloaded_file_name)
            ms_two = (end_two - end).seconds
            await event.edit(
                f"Downloaded in {ms_one} seconds. Uploaded in {ms_two} seconds."
            )

        else:
            await event.edit(f"File Not Found {input_str}")
    else:
        await event.edit("Syntax // .vtg<name> as reply to a Telegram video")
