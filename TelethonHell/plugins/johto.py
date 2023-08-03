



from telethon import events
import random
import asyncio

is_johto = False  # Flag variable to control the loop
hunt_attempts = 0  # Number of consecutive hunt attempts

pokemon_messages = {
    'Ho-Oh': 'A wild Ho-Oh appeared!',
    'Lugia': 'A wild Lugia appeared!'
}


@hell_cmd(pattern="johto(?:\s|$)([\s\S]*)")
async def _(event):
    global is_johto, hunt_attempts
    if is_johto:
        is_johto = False  # Turn off the auto hunt
        await event.edit("Auto hunt turned off.")
        return
    await event.edit("Finding...")  # Edit the command invoked message
    is_johto = True  # Start the hunting loop
    hunt_attempts = 0  # Reset the hunt attempts counter
    while is_johto:
        await event.client.send_message(572621020, "/hunt")
        hunt_attempts += 1
        if hunt_attempts > 3:
            is_johto = False  # Stop the hunting loop
            break
        delay = random.randint(3, 6)  # Generate a random delay between 3 and 6 seconds
        await asyncio.sleep(delay)

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    global is_johto, hunt_attempts
    if 'Daily hunt limit reached' in event.raw_text:
        is_johto = False  # Stop the hunting loop
    elif 'strange' in event.raw_text:
        is_johto = False  # Stop the hunting loop
    elif 'Shiny pokemon found!' in event.raw_text:
        is_johto = False  # Stop the hunting loop
    else:
        for pokemon, message in pokemon_messages.items():
            if f'A wild {pokemon}' in event.raw_text:
                is_johto = False  # Stop the hunting loop
                break
    hunt_attempts = 0  # Reset the hunt attempts counter after receiving a response