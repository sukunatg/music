# Don't froget about me. ~ @UKR_Known_1 xD

from traceback import format_exc

import telethon

from . import *


pkkasbeiwvi = {}
pkkasbeiwvi["is_active"] = False
pkkasbeiwvi["is_asking_for_poka_battle"] = False
pkkasbeiwvi["is_auto_hunting"] = False
pkkasbeiwvi["is_hunting"] = False
POKA_BOTS_LIST = [572621020, 2010717663] # ADD THAT POKE BOT ID HERE.
pkkasbeiwvi["number_of_edits"] = 0
pkkasbeiwvi["t_btns"] = [(1, 1), (0, 0), (1, 0), (0, 1)]
pkkasbeiwvi["preferred_btn"] = 0 
pkkasbeiwvi["curr_btn"] = pkkasbeiwvi["preferred_btn"]

def change_pref():
    pkkasbeiwvi["curr_btn"] = (pkkasbeiwvi["curr_btn"] + 1) % len(pkkasbeiwvi["t_btns"])

def get_pref():
    return pkkasbeiwvi["t_btns"][pkkasbeiwvi["curr_btn"]]

@H1.on(telethon.events.NewMessage(pattern = "/b4", outgoing = True))
async def ready_for_challenge(event):
    pkkasbeiwvi["is_active"] = not pkkasbeiwvi["is_active"]
    pkkasbeiwvi["number_of_edits"] = 0
    await event.edit("Poke farmer: " + ("active" if pkkasbeiwvi["is_active"] else "sleeping"))

@H1.on(telethon.events.NewMessage(pattern = "/togglefarmer", outgoing = True))
async def ready_for_challenge(event):
    pkkasbeiwvi["number_of_edits"] = 0
    pkkasbeiwvi["is_auto_hunting"] = not pkkasbeiwvi["is_auto_hunting"]
    await event.edit("Poke auto farmer: " + ("active" if pkkasbeiwvi["is_auto_hunting"] else "sleeping"))

@H1.on(telethon.events.NewMessage(pattern = "/challenge", incoming = True))
async def ready_for_challenge(event):
    pkkasbeiwvi["is_asking_for_poka_battle"] = True

@H1.on(telethon.events.NewMessage(pattern = "/hunt", incoming = False))
async def ready_for_hunt(event):
    pkkasbeiwvi["is_hunting"] = True

@H1.on(telethon.events.NewMessage(pattern = "(.*) has challenged (.*) to a battle", incoming = True))
async def challenge_btn_clicker(event):
    try:
        if not pkkasbeiwvi["is_active"]:
            return
        if not pkkasbeiwvi["is_asking_for_poka_battle"]:
            return
        if not event.sender_id in POKA_BOTS_LIST:
            return
        await event.click(0, 0) # Accept every challenge.
        pkkasbeiwvi["number_of_edits"] = 0
    except Exception as err:
        await event.reply("hm....")
    finally:
        pkkasbeiwvi["is_asking_for_poka_battle"] = False

@H1.on(telethon.events.NewMessage(pattern = "([\S\s]*)Current turn: (.*)", incoming = True))
@H1.on(telethon.events.MessageEdited(pattern="([\S\s]*)((Current turn: (.*))|(Dealt [\d]+ damage.)|(.* is attacking))", incoming=True))
async def challenge_main_clicker(event):
    try:
        if not pkkasbeiwvi["is_active"]:
            return
        if not event.sender_id in POKA_BOTS_LIST:
            return
        await event.click(*get_pref())  # Click the button every time the message is edited
        if "not very effective" in event.raw_text:
            change_pref()
        if "had no effect" in event.raw_text:
            change_pref()
    except Exception:
        pass

@H1.on(telethon.events.MessageEdited(pattern = "([\S\s]*) fainted.([\S\s]*)", incoming = True))
async def challenge_hunting_done(event):
    try:
        if not pkkasbeiwvi["is_active"]:
            return
        if not event.sender_id in POKA_BOTS_LIST:
            return
        if pkkasbeiwvi["is_auto_hunting"]:
            return await event.reply("/hunt")
        if pkkasbeiwvi["is_hunting"]:
            pkkasbeiwvi["is_hunting"] = False
    except Exception as err:
        await event.reply("hm")
    finally:
        pkkasbeiwvi["number_of_edits"] = 0
        pkkasbeiwvi["curr_btn"] = pkkasbeiwvi["preferred_btn"]
