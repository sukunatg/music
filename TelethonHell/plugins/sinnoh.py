import sys
import os
import asyncio
from telethon import events

@hell_cmd(pattern="sinnoh(?:\s|$)([\s\S]*)")
async def _(event):
    input_str = int(event.pattern_match.group(1)) or 15
    await eod(event,"`Ok! Finding.....`")
    while True:
        await event.client.send_message(572621020,"/hunt")
        await asyncio.sleep(input_str)
      

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    if 'A wild Deoxys' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Arceus' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Dialga' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Palkia' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Giratina' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Regigigas' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'A wild Darkrai' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    if 'Shiny pokemon found!' in event.raw_text:
        await bot.disconnect()
        os.execl(sys.executable, sys.executable, *sys.argv)
    

import asyncio
import os
import sys
import random
from telethon import events

is_sinnoh = False  # Flag variable to control the loop

@hell_cmd(pattern="sinnoh(?:\s|$)([\s\S]*)")
async def _(event):
    global is_sinnoh
    await eod(event, "Ok! Finding.....")
    is_sinnoh = True  # Start the hunting loop
    while is_sinnoh:
        await event.client.send_message(572621020, "/hunt")
        delay = random.randint(3, 6)  # Generate a random delay between 3 and 6 seconds
        await asyncio.sleep(delay)

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    global is_sinnoh
    if 'A wild Arceus' in event.raw_text:
        is_sinnoh = False  # Stop the hunting loop
    if 'A wild Dialga' in event.raw_text:
        is_sinnoh = False  # Stop the hunting loop
    if 'A wild Giratina' in event.raw_text:
        is_sinnoh = False  # Stop the hunting loop
    if 'A wild Palkia' in event.raw_text:
        is_sinnoh = False  # Stop the hunting loop
    if 'A wild Regigigas' in event.raw_text:
        is_sinnoh = False  # Stop the hunting loop
    if 'A wild Darkrai' in event.raw_text:
        is_sinnoh = False  # Stop the hunting loop
    if 'You noticed a strange object' in event.raw_text:
        is_sinnoh = False  # Stop the hunting loop
    if 'Shiny pokemon found!' in event.raw_text:
        is_sinnoh = False  # Stop the hunting loop
    if 'Daily hunt limit reached' in event.raw_text:
        is_sinnoh = False  # Stop the hunting loop
    if 'limit' in event.raw_text:
        is_sinnoh = False  # Stop the hunting loop
    
    