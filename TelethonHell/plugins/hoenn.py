

import asyncio
import os
import sys
import random
from telethon import events

is_hoenn = False  # Flag variable to control the loop

@hell_cmd(pattern="hoenn(?:\s|$)([\s\S]*)")
async def _(event):
    global is_hoenn
    await eod(event, "Ok! Finding.....")
    is_hoenn = True  # Start the hunting loop
    while is_hoenn:
        await event.client.send_message(572621020, "/hunt")
        delay = random.randint(3, 6)  # Generate a random delay between 3 and 6 seconds
        await asyncio.sleep(delay)

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    global is_hoenn
    if 'A wild Kyogre' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    if 'A wild Deoxys' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    if 'A wild Rayquaza' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    if 'A wild Regirock' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    if 'A wild Registeel' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    if 'A wild Regice' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    if 'You noticed a strange object' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    if 'Shiny pokemon found!' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    if 'Daily hunt limit reached' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    if 'limit' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop