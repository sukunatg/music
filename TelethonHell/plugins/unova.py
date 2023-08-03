
    
        

from telethon import events
import random
import asyncio

is_unova = False  # Flag variable to control the loop
hunt_attempts = 0  # Number of consecutive hunt attempts

pokemon_messages = {
    'Reshiram': 'A wild Reshiram appeared!',
    'Kyurem': 'A wild Kyurem appeared!',
    'Zekrom': 'A wild Zekrom appeared!',
    'Victini': 'A wild Victini appeared!'
}


@hell_cmd(pattern="unova(?:\s|$)([\s\S]*)")
async def _(event):
    global is_unova, hunt_attempts
    if is_unova:
        is_unova = False  # Turn off the auto hunt
        await event.edit("Auto hunt turned off.")
        return
    await event.edit("Finding...")  # Edit the command invoked message
    is_unova = True  # Start the hunting loop
    hunt_attempts = 0  # Reset the hunt attempts counter
    while is_unova:
        await event.client.send_message(572621020, "/hunt")
        hunt_attempts += 1
        if hunt_attempts > 3:
            is_unova = False  # Stop the hunting loop
            break
        delay = random.randint(3, 6)  # Generate a random delay between 3 and 6 seconds
        await asyncio.sleep(delay)

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    global is_unova, hunt_attempts
    if 'Daily hunt limit reached' in event.raw_text:
        is_unova = False  # Stop the hunting loop
    elif 'strange' in event.raw_text:
        is_unova = False  # Stop the hunting loop
    elif 'Shiny pokemon found!' in event.raw_text:
        is_unova = False  # Stop the hunting loop
    else:
        for pokemon, message in pokemon_messages.items():
            if f'A wild {pokemon}' in event.raw_text:
                is_unova = False  # Stop the hunting loop
                break
    hunt_attempts = 0  # Reset the hunt attempts counter after receiving a response