import os
from telethon import events
import requests as r
import re
import asyncio

# Get the chat ID from the OS environment variable
chat_id = int(os.getenv('CHAT_ID', '-946433760'))

read = r.get("https://gist.githubusercontent.com/itz-king/1b98aa6ec756058144d66e306fc557dc/raw/pokemon.txt").text

guesser_enabled = os.getenv('guesser', '').lower() == 'true'

@bot.on(events.NewMessage(chats=chat_id))
async def guessing(event):
    if guesser_enabled and event.sender_id == 572621020 and not event.photo and 'Hint' in event.raw_text:
        string = event.raw_text[8:]
        toreplace = {'_': '.', ' ': ''}
        for key, value in toreplace.items():
            string = string.replace(key, value)
        patt = re.compile(string)
        matches = patt.finditer(read)

        # Limit the number of matched outputs to 20 or below
        max_outputs = 29
        num_outputs = 0

        for match in matches:
            if num_outputs >= max_outputs:
                break

            await event.client.send_message(event.chat_id, f"{match[0]}")
            num_outputs += 1

@bot.on(events.NewMessage(chats=chat_id))
async def gues(event):
    if guesser_enabled and event.sender_id == 572621020 and not event.photo and '+5' in event.raw_text:
        # Add a 1-second delay before sending the /guess command
        await asyncio.sleep(0.5)
        await event.client.send_message(event.chat_id, "/guess")