
        

import asyncio
import os
import sys
import random
from telethon import events

is_johto = False  # Flag variable to control the loop

@hell_cmd(pattern="johto(?:\s|$)([\s\S]*)")
async def _(event):
    global is_johto
    await eod(event, "Ok! Finding.....")
    is_johto = True  # Start the hunting loop
    while is_johto:
        await event.client.send_message(572621020, "/hunt")
        delay = random.randint(3, 6)  # Generate a random delay between 3 and 6 seconds
        await asyncio.sleep(delay)

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    global is_johto
    if 'A wild Ho-Oh' in event.raw_text:
        is_johto = False  # Stop the hunting loop
    if 'A wild Lugia' in event.raw_text:
        is_johto = False  # Stop the hunting loop
    if 'You noticed a strange object' in event.raw_text:
        is_johto = False  # Stop the hunting loop
    if 'Shiny pokemon found!' in event.raw_text:
        is_johto = False  # Stop the hunting loop
    if 'Daily hunt limit reached' in event.raw_text:
        is_johto = False  # Stop the hunting loop
    if 'limit' in event.raw_text:
        is_johto = False  # Stop the hunting loop