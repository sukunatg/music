import asyncio
from telethon.errors import MessageIdInvalidError
from TelethonHell.plugins import *

# Global variable to keep track of auction toggle status
auction_enabled = False

# Use a dictionary to store the last command message ID for each chat
last_command_messages = {}

@bot.on(events.NewMessage(pattern=r"/toggleauc"))
async def toggle_auction(event):
    global auction_enabled

    # Toggle the auction status
    auction_enabled = not auction_enabled

    if auction_enabled:
        if event.is_reply:
            await event.respond("Auction mode has been enabled.", reply_to=event.reply_to_msg_id)
        else:
            await event.respond("Auction mode has been enabled.")
    else:
        if event.is_reply:
            await event.respond("Auction mode has been disabled.", reply_to=event.reply_to_msg_id)
        else:
            await event.respond("Auction mode has been disabled.")

@bot.on(events.NewMessage(pattern=r"\.", outgoing=True))
async def _(event):
    global last_command_messages, auction_enabled

    # Check if auction is enabled
    if not auction_enabled:
        return

    # Check if the message matches the command pattern
    if not event.message.message.startswith("."):
        return

    cid = await client_id(event)
    hell_mention = cid[2]
    animation_interval = 2
    animation_ttl = range(3)
    animation_chars = [
        "•",
        "• •",
        f"• • •",
    ]

    # Delete the previous command message, if it exists
    if event.chat_id in last_command_messages:
        try:
            await event.client.delete_messages(event.chat_id, last_command_messages[event.chat_id])
        except MessageIdInvalidError:
            pass  # Ignore if the message has already been deleted

    # Show the animation
    for i in animation_ttl:
        msg = await event.edit(animation_chars[i % 3])
        await asyncio.sleep(animation_interval)

    # Store the current message as the last command message
    last_command_messages[event.chat_id] = msg.id
