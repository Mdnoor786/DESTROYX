# For @UniBorg
# (c) Shrimadhav U K
# PoRTeD FRoM ULTRA X

from telethon.tl.functions.channels import GetAdminedPublicChannelsRequest

from userbot import CMD_HELP, bot
from userbot.utils import admin_cmd


@bot.on(admin_cmd("listmyusernames"))
async def mine(event):
    result = await bot(GetAdminedPublicChannelsRequest())
    output_str = "".join(
        f"{channel_obj.title}\n@{channel_obj.username}\n\n"
        for channel_obj in result.chats
    )

    await event.edit(output_str)


CMD_HELP.update(
    {
        "LisT My Usernames": ".listmyusernames gives you a list of your channels and groups"
    }
)
