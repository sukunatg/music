
import asyncio
import os
import sys
import random
from telethon import events

is_alola = False  # Flag variable to control the loop

@hell_cmd(pattern="alola(?:\s|$)([\s\S]*)")
async def _(event):
    global is_alola
    await eod(event, "Ok! Finding.....")
    is_alola = True  # Start the hunting loop
    while is_alola:
        await event.client.send_message(572621020, "/hunt")
        delay = random.randint(3, 6)  # Generate a random delay between 3 and 6 seconds
        await asyncio.sleep(delay)

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    global is_alola
    if 'A wild Cosmoem' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'A wild Pheromosa' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'A wild Cosmog' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'A wild Lunala' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'A wild Solgaleo' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'A wild Necrozma' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'A wild Zeraora' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'A wild Melmetal' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'A wild Marshadow' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'A wild Meltan' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'A wild Aerodactyl' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'You noticed a strange object' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'Shiny pokemon found!' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'Daily hunt limit reached' in event.raw_text:
        is_alola = False  # Stop the hunting loop
    if 'limit' in event.raw_text:
        is_alola = False  # Stop the hunting loop