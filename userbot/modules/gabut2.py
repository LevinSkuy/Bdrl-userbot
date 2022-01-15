from time import sleep
from userbot import CMD_HELP, DEVS
from userbot.events import register


@register(outgoing=True, pattern='^.yansen(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Hai Perkenalkan Namaku Yansen`")
    sleep(3)
    await typew.edit("`17 Tahun`")
    sleep(3)
    await typew.edit("`JOMBLO`")
    sleep(1)
    await typew.edit("`Tinggal Di Jawa Barat, Salam Kenal:)`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.sayang(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Cuma Mau Bilang`")
    sleep(3)
    await typew.edit("`Aku Sayang Kamu`")
    sleep(1)
    await typew.edit("`I LOVE YOU 💞`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.semangat(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`Apapun Yang Terjadi`")
    sleep(3)
    await typew.edit("`Tetaplah Bernapas`")
    sleep(1)
    await typew.edit("`Dan Selalu Bersyukur`")
# Create by myself @localheart


@register(outgoing=True, pattern='^.ngeri(?: |$)(.*)')
async def typewriter(typew):
    typew.pattern_match.group(1)
    sleep(3)
    await typew.edit("`run ah ada suhu bot `")
    sleep(5)
    await typew.edit("`btw ajarin deploy bot dong`")
    sleep(3)
    await typew.edit("`kan Abang atau Kaka suhu nih`")
    sleep(3)
    await typew.edit("`ayolah ajarin saya🥺`")
    sleep(1)
    await typew.edit("`Pc @yansesat aja ya🥵`")
# Create by myself @localheart


CMD_HELP.update({
    "oi": "𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `yansen`\
    \n↳ : perkenalan yansen\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.sayang`\
    \n↳ : Gombalan maut`\
    \n\n𝘾𝙤𝙢𝙢𝙖𝙣𝙙: `.semangat`\
    \n↳ : Jan Lupa Semangat."
})
