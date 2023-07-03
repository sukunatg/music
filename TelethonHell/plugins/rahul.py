

import asyncio
import os
import sys
import random
from telethon import events

is_rahul = False  # Flag variable to control the loop

@hell_cmd(pattern="rahul(?:\s|$)([\s\S]*)")
async def _(event):
    global is_rahul
    await eod(event, "Ok! Finding.....")
    is_rahul = True  # Start the hunting loop
    while is_rahul:
        await event.client.send_message(572621020, "/hunt")
        delay = random.randint(3, 6)  # Generate a random delay between 3 and 6 seconds
        await asyncio.sleep(delay)

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    global is_rahul
    if 'A wild Kyogre' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Deoxys' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Groudon' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Regirock' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Registeel' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Regice' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Latios' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Latias' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Jirachi' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Sceptile' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Xerneas' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Yveltal' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Hoopa' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Zygarde' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Greninja' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Alakazam' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Aegislash' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Aerodactyl' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Zapdos' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Moltres' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Articuno' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'A wild Mewtwo' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'You noticed a strange object' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'Shiny pokemon found!' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'Daily hunt limit reached' in event.raw_text:
        is_rahul = False  # Stop the hunting loop
    if 'limit' in event.raw_text:
        is_rahul = False  # Stop the hunting loop