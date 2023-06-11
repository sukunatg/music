import sys
import os
import asyncio
from telethon import events

@hell_cmd(pattern="missing(?:\s|$)([\s\S]*)")
async def _(event):
    input_str = int(event.pattern_match.group(1)) or 15
    await eod(event,"`Ok! Finding.....`")
    while True:
        await event.client.send_message(572621020,"/hunt")
        await asyncio.sleep(input_str)
      

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    if 'A wild Marshadow' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Kakuna' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Greninja' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Ninjask' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Hoopa' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Zygrade' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Volcanion' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'An expert trainer has challenged you to a battle.' in event.raw_text:

        await bot.disconnect()

        os.execl(sys.executable, sys.executable, *sys.argv)
