from userbot import CMD_HELP, bot
from userbot.utils import admin_cmd


@bot.on(admin_cmd(pattern=r"space"))
async def space(e):
    await e.edit("ㅤ")


@bot.on(admin_cmd(pattern=r"blank"))
async def blank(e):
    await e.edit("­")


# Ported from shivam's project
CMD_HELP.update({"space": "try .space or .blank"})
