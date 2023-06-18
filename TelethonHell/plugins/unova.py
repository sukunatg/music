
    

import asyncio
import os
import sys
import random
from telethon import events

is_unova = False  # Flag variable to control the loop

@hell_cmd(pattern="unova(?:\s|$)([\s\S]*)")
async def _(event):
    global is_unova
    await eod(event, "Ok! Finding.....")
    is_unova = True  # Start the hunting loop
    while is_unova:
        await event.client.send_message(572621020, "/hunt")
        delay = random.randint(3, 6)  # Generate a random delay between 3 and 6 seconds
        await asyncio.sleep(delay)

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    global is_unova
    if 'A wild Reshiram' in event.raw_text:
        is_unova = False  # Stop the hunting loop
    if 'A wild Kyurem' in event.raw_text:
        is_unova = False  # Stop the hunting loop
    if 'A wild Zekrom' in event.raw_text:
        is_unova = False  # Stop the hunting loop
    if 'A wild Victini' in event.raw_text:
        is_unova = False  # Stop the hunting loop
    if 'You noticed a strange object' in event.raw_text:
        is_unova = False  # Stop the hunting loop
    if 'Shiny pokemon found!' in event.raw_text:
        is_unova = False  # Stop the hunting loop
    if 'Daily hunt limit reached' in event.raw_text:
        is_unova = False  # Stop the hunting loop
    if 'limit' in event.raw_text:
        is_unova = False  # Stop the hunting loop.execl