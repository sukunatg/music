

import asyncio
import os
import sys
import random
from telethon import events

is_kalos = False  # Flag variable to control the loop

@hell_cmd(pattern="kalos(?:\s|$)([\s\S]*)")
async def _(event):
    global is_kalos
    await eod(event, "Ok! Finding.....")
    is_kalos = True  # Start the hunting loop
    while is_kalos:
        await event.client.send_message(572621020, "/hunt")
        delay = random.randint(3, 6)  # Generate a random delay between 3 and 6 seconds
        await asyncio.sleep(delay)

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    global is_kalos
    if 'A wild Mewtwo' in event.raw_text:
        is_kalos = False  # Stop the hunting loop
    if 'A wild Xerneas' in event.raw_text:
        is_kalos = False  # Stop the hunting loop
    if 'A wild Yveltal' in event.raw_text:
        is_kalos = False  # Stop the hunting loop
    if 'You noticed a strange object' in event.raw_text:
        is_kalos = False  # Stop the hunting loop
    if 'Shiny pokemon found!' in event.raw_text:
        is_kalos = False  # Stop the hunting loop
    if 'Daily hunt limit reached' in event.raw_text:
        is_kalos = False  # Stop the hunting loop
    if 'limit' in event.raw_text:
        is_kalos = False  # Stop the hunting loop
    if 'A wild Mewtwo' in event.raw_text:

        is_kalos = False  # Stop the hunting loop




        
        
        
