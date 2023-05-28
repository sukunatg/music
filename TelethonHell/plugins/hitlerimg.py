# Don't FROGet it was made by none other than @UKR_Known_1
# Some codes were copied from stackOverflow :')

from traceback import format_exc
from PIL import Image, ImageChops

# import asyncio # Guess why commented this :)
import os
import telethon

from . import *


pldjwfgsduto = {}
pldjwfgsduto["is_enabled"] = False
pldjwfgsduto["use_cache"] = True
pldjwfgsduto["valid_grp"] = []
pldjwfgsduto["cache"] = {}

@Hell.on(telethon.events.NewMessage(pattern = "\.toggleguesser$", outgoing = True))
async def toggle_enabled_stat(event):
    pldjwfgsduto["is_enabled"] = not pldjwfgsduto["is_enabled"]
    await event.edit("Pokemon guesser : " + ("active" if pldjwfgsduto["is_enabled"] else "sleeping"))

@Hell.on(telethon.events.NewMessage(pattern = "\.toggleguessercache$", outgoing = True))
async def toggle_cache_stat(event):
    pldjwfgsduto["use_cache"] = not pldjwfgsduto["use_cache"]
    await event.edit("Can use cache : " + ("enabled" if pldjwfgsduto["use_cache"] else "disabled"))

@Hell.on(telethon.events.NewMessage(pattern = "\.guesseradd$", outgoing = True))
async def addgrp_guesser(event):
    if event.chat_id in pldjwfgsduto["valid_grp"]:
        return await event.edit("Pokemon guesser is already active for this group.")
    pldjwfgsduto["valid_grp"].append(event.chat_id)
    await event.edit("Pokemon guesser is now active for this group!")

@Hell.on(telethon.events.NewMessage(pattern = "\.guesserrem$", outgoing = True))
async def addgrp_guesser(event):
    if not event.chat_id in pldjwfgsduto["valid_grp"]:
        return await event.edit("Pokemon guesser is already disabled for this group.")
    pldjwfgsduto["valid_grp"].remove(event.chat_id)
    await event.edit("Pokemon guesser is now disabled for this group!")

@Hell.on(telethon.events.NewMessage(incoming = True))
async def guess_handler(event):
    if not pldjwfgsduto["is_enabled"]:
        return
    if not event.chat_id in pldjwfgsduto["valid_grp"]:
        return
    if not "pokemon?" in event.raw_text:
        return
    file = await event.download_media("temp_guess.png")
    if not file:
        return await event.reply("Error while fetching file.")
    try:
        name = await process_query(file, allow_cache = pldjwfgsduto["use_cache"])
        if not name:
            return await event.reply("No match found in database!")
        name = name.split(".png")[0]
        await event.reply(name)
        os.remove(file)
    except Exception as err:
        await event.client.send_message(
            "me",
            (
                "An error has occurred!\nError: <code>"
                + str(err)
                + "</code>\n\nTraceback:\n<code>"
                + str(format_exc())
                + "</code>\n<b><i>ID</i>:</b> <code>"
                + str(event.chat_id)
                + "/" + str(event.id)
                + "</code>"
            ),
            parse_mode = "html"
        )

@Hell.on(telethon.events.NewMessage(pattern = "\.configguesser$", outgoing = True))
async def configure_guesser(event):
    await event.edit("Processing...")
    if not event.is_reply:
        return await event.edit("Reply to a message from where you want to configure.")
    reply = await event.get_reply_message()
    try:
        if not os.path.exists("pokeGuesser"):
            os.mkdir("pokeGuesser")
        async for message in event.client.iter_messages(event.chat_id, min_id=reply.id):
            await message.download_media(f"pokeGuesser/{message.message}.png")
        await event.edit(f"Configured with total of {str(len(os.listdir('pokeGuesser')))} file(s).")
    except Exception as err:
        await event.reply(
            (
                "An error has occurred!\nError: <code>"
                + str(err)
                + "</code>\n\nTraceback:\n<code>"
                + str(format_exc())
                + "</code>"
            ),
            parse_mode = "html"
        )

@Hell.on(telethon.events.NewMessage(pattern = "\.loadguesser$", outgoing = True))
async def load_memory_guesser(event):
    pldjwfgsduto["cache"] = {}
    if not os.path.exists("pokeGuesser"):
        os.mkdir("pokeGuesser")
        return await event.edit("No configuration found!")
    await event.edit(f"Total {str(len(os.listdir('pokeGuesser')))} configuration file(s) found.\nLoading...")
    for imgp in os.listdir("pokeGuesser"):
        img = Image.open(f"pokeGuesser/{imgp}")
        pldjwfgsduto["cache"][imgp] = img
    await event.edit(
        f"Total {str(len(os.listdir('pokeGuesser')))} configuration file(s) found."
        + f"\nLoaded {str(len(list(pldjwfgsduto['cache'])))} file(s) into memory."
    )


def are_images_equal(img1, img2, cmp_size = True, cmp_alpha = True, cmp_data = True):
    equal_size = cmp_size and (img1.height == img2.height and img1.width == img2.width)
    if cmp_alpha and (img1.mode == img2.mode == "RGBA"):
        img1_alphas = [pixel[3] for pixel in img1.getdata()]
        img2_alphas = [pixel[3] for pixel in img2.getdata()]
        equal_alphas = img1_alphas == img2_alphas
    else:
        equal_alphas = True
    equal_content = cmp_data and (not ImageChops.difference(
        img1.convert("RGB"), img2.convert("RGB")
    ).getbbox())
    return equal_size and equal_alphas and equal_content

# Presenting, The most inefficient function in the whole history.
# Sadly, It's no longer "most inefficient".
# Or is it!?
async def process_query(filepath, allow_cache = True):
    poke_name = None
    img1 = Image.open(filepath)
    if allow_cache:
        for img2p in os.listdir("pokeGuesser"):
            img2 = pldjwfgsduto["cache"].get(img2p, None)
            if not img2:
                img2 = Image.open(f"pokeGuesser/{img2p}")
                pldjwfgsduto["cache"][img2p] = img2
            v = are_images_equal(img1, img2)
            if v:
                return img2p
    else:
        for img2p in os.listdir("pokeGuesser"):
            img2 = Image.open(f"pokeGuesser/{img2p}")
            v = are_images_equal(img1, img2)
            if v:
                return img2p
