
import random
import asyncio
import time
from datetime import datetime, timedelta, timezone
from telethon import events

is_hoenn = False  # Flag variable to control the loop
hunt_attempts = 0  # Number of consecutive hunt attempts

pokemon_messages = {
    'Kyogre': 'A wild Kyogre appeared!',
    'Deoxys': 'A wild Deoxys appeared!',
    'Groudon': 'A wild Groudon appeared!'
}


@hell_cmd(pattern="hoenn(?:\s|$)([\s\S]*)")
async def _(event):
    global is_hoenn, hunt_attempts
    if is_hoenn:
        is_hoenn = False  # Turn off the auto hunt
        await event.edit("Auto hunt turned off.")
        return
    
    # Get the current time in IST
    current_time = datetime.now(timezone.utc) + timedelta(hours=5, minutes=30)
    formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")

    # Print the message with the timestamp
    print(f"Plugin is invoked on {formatted_time} IST")
    
    await event.edit("Finding...")  # Edit the command invoked message
    is_hoenn = True  # Start the hunting loop
    hunt_attempts = 0  # Reset the hunt attempts counter
    while is_hoenn:
        await event.client.send_message(572621020, "/hunt")
        hunt_attempts += 1
        if hunt_attempts > 3:
            is_hoenn = False  # Stop the hunting loop
            break
        delay_seconds = random.uniform(3.0, 6.0)  # Generate a random delay in seconds
        await asyncio.sleep(delay_seconds)

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    global is_hoenn, hunt_attempts
    if 'Daily hunt limit reached' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    elif 'strange' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    elif 'Shiny pokemon found!' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    elif 'Cannot hunt while battling' in event.raw_text:
        is_hoenn = False  # Stop the hunting loop
    else:
        for pokemon, message in pokemon_messages.items():
            if f'A wild {pokemon}' in event.raw_text:
                is_hoenn = False  # Stop the hunting loop
                break
    hunt_attempts = 0  # Reset the hunt attempts counter after receiving a response