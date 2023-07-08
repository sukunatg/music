




from telethon import events
import random
import asyncio

is_kanto = False  # Flag variable to control the loop
hunt_attempts = 0  # Number of consecutive hunt attempts

pokemon_messages = {
    'Mewtwo': 'A wild Mewtwo appeared!',
    'Aerodactyl': 'A wild Aerodactyl appeared!',
    'Articuno': 'A wild Articuno appeared!',
    'Moltres': 'A wild Moltres appeared!',
    'Zapdos': 'A wild Zapdos appeared!',
    'Mew': 'A wild Mew appeared!',
}

@hell_cmd(pattern="kanto(?:\s|$)([\s\S]*)")
async def _(event):
    global is_kanto, hunt_attempts
    if is_kanto:
        is_kanto = False  # Turn off the auto hunt
        await event.edit("Auto hunt turned off.")
        return
    await event.edit("Finding...")  # Edit the command invoked message
    is_kanto = True  # Start the hunting loop
    hunt_attempts = 0  # Reset the hunt attempts counter
    while is_kanto:
        await event.client.send_message(572621020, "/hunt")
        hunt_attempts += 1
        if hunt_attempts > 3:
            await event.client.send_message('me', "No response for more than three attempts. Stopping the hunting.")
            is_kanto = False  # Stop the hunting loop
            break
        delay = random.randint(3, 6)  # Generate a random delay between 3 and 6 seconds
        await asyncio.sleep(delay)

@bot.on(events.NewMessage(from_users=[572621020]))
async def _(event):
    global is_kanto, hunt_attempts
    if 'Daily hunt limit reached' in event.raw_text:
        await event.client.send_message('me', "Daily hunt limit reached. Stopping the hunting.")
        is_kanto = False  # Stop the hunting loop
    elif 'strange' in event.raw_text:
        await event.client.send_message('me', "Noice, an egg has been found!")
        is_kanto = False  # Stop the hunting loop
    elif 'Shiny pokemon found!' in event.raw_text:
        await event.client.send_message('me', "A shiny pokemon found! Stopping the hunting.")
        is_kanto = False  # Stop the hunting loop
    else:
        for pokemon, message in pokemon_messages.items():
            if f'A wild {pokemon}' in event.raw_text:
                try:
                    await event.client.send_message('me', message)
                except Exception as e:
                    print(f"Failed to send message: {e}")
                is_kanto = False  # Stop the hunting loop
                break
    hunt_attempts = 0  # Reset the hunt attempts counter after receiving a response