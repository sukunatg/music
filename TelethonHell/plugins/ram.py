"""Fun plugin
\nCode by @waruserbot (member)
type .ram and ram to see the fun.
"""
import random, re
from uniborg.util import admin_cmd
import asyncio
from telethon import events

@borg.on(admin_cmd(pattern="ram?(.*)"))
async def _(event):
     if not event.text[0].isalpha() and event.text[0] not in ("/", "#", "@", "!"):
        await event.edit("जय")
        await asyncio.sleep(1)
        await event.edit("श्री") 
        await asyncio.sleep(1) 
        await event.edit("राम") 
        await asyncio.sleep(1) 
        
@borg.on(events.NewMessage(pattern=r"\.nehi", outgoing=True))
async def _(event):
    if event.fwd_from:
        return
    await event.edit("Jai Shree Ram 🚩🚩") 
    await asyncio.sleep(999) 