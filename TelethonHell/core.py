import asyncio
import os
from pathlib import Path

from . import *


@hell_cmd(pattern="cmds$")
async def kk(event):
    event.message.id
    if event.reply_to_msg_id:
        event.reply_to_msg_id
    cids = await client_id(event)
    ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
    cmd = "ls TelethonHell/plugins"
    process = await asyncio.create_subprocess_shell(
        cmd, stdout=asyncio.subprocess.PIPE, stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    o = stdout.decode()
    _o = o.split("\n")
    o = "\n".join(_o)
    OUTPUT = f"""
<h1>List of Plugins in WarUserBot:</h1>

<code>{o}</code>

<b><i>HELP:</b></i> <i>If you want to know the commands for a plugin, do “ .plinfo <plugin name> ”

<b><a href='https://t.me/waruserbot'>@waruserbotsupport</a></b>
"""
    hell = await telegraph_paste("All available plugins in WarUserBOt", OUTPUT)
    await eor(event, f"[All available plugins in Waruserbot]({hell})", link_preview=False)




import asyncio
import os
from pathlib import Path

from TelethonHell.plugins import *

# Add the user IDs of approved providers
approved_provider_ids = [5912161237]

@hell_cmd(pattern="install(?:\s|$)([\s\S]*)")
async def install(event):
    cids = await client_id(event)
    ForGo10God, HELL_USER, hell_mention = cids[0], cids[1], cids[2]
    b = 1
    owo = event.text[9:]
    hell = await eor(event, "Installing.")
    reply_msg = await event.get_reply_message()
    if reply_msg and reply_msg.sender_id in approved_provider_ids:
        try:
            downloaded_file = await event.client.download_media(
                reply_msg,
                "./TelethonHell/plugins/"
            )
            if owo != "-f":
                op = open(downloaded_file, "r")
                rd = op.read()
                op.close()
                try:
                    for harm in HARMFUL:
                        if harm in rd:
                            os.remove(downloaded_file)
                            return await hell.edit(
                                f"⚠️ WARNING !! \n\nReplied plugin file contains some harmful codes. Please consider checking the file. If you still want to install then use {hl}install -f. \n\nCodes Detected : \n• {harm}"
                            )
                except BaseException:
                    pass
            if "(" not in downloaded_file:
                path1 = Path(downloaded_file)
                shortname = path1.stem
                load_module(shortname.replace(".py", ""))
                if shortname in CMD_LIST:
                    string = "Commands found in {}\n".format(os.path.basename(downloaded_file))
                    for i in CMD_LIST[shortname]:
                        string += "  •  " + i
                        string += "\n"
                        if b == 1:
                            a = "Installing.."
                            b = 2
                        else:
                            a = "Installing..."
                            b = 1
                        await hell.edit(a)
                    return await hell.edit(
                        f"✅ Installed module :- {shortname} \n✨ BY :- {hell_mention}\n\n{string}\n\n      ⚡ʟᴇɢᴇɴᴅᴀʀʏ ᴀꜰ ᴘʀᴏxɪᴍᴀ⚡",
                        link_preview=False,
                    )
                return await hell.edit(f"Installed module {os.path.basename(downloaded_file)}")
            else:
                os.remove(downloaded_file)
                return await parse_error(hell, "Module already installed or unknown format.")
        except Exception as e:
            await parse_error(hell, e)
            return os.remove(downloaded_file)
    else:
        return await hell.edit("`Sorry u can only install plugins sent by approved users for your safety..`")



@hell_cmd(pattern="uninstall ([\s\S]*)")
async def uninstall(event):
    shortname = event.text[11:]
    if ".py" in shortname:
        shortname = shortname.replace(".py", "")
    hell = await eor(event, f"__Trying to uninstall plugin__ `{shortname}` ...")
    dir_path = f"./TelethonHell/plugins/{shortname}.py"
    try:
        remove_plugin(shortname)
        os.remove(dir_path)
        await eod(hell, f"**Uninstalled plugin** `{shortname}` **successfully.**")
    except OSError as e:
        await parse_error(hell, f"`{dir_path}` : __{e.strerror}__", False)


@hell_cmd(pattern="unload ([\s\S]*)")
async def unload(event):
    shortname = event.pattern_match["shortname"]
    try:
        remove_plugin(shortname)
        await eod(event, f"Successfully unloaded `{shortname}`")
    except Exception as e:
        await parse_error(event, e)


@hell_cmd(pattern="load ([\s\S]*)")
async def load(event):
    shortname = event.pattern_match["shortname"]
    try:
        try:
            remove_plugin(shortname)
        except BaseException:
            pass
        load_module(shortname)
        await eod(event, f"Successfully loaded `{shortname}`")
    except Exception as e:
        await parse_error(event, e)


CmdHelp("core").add_command(
    "install", "<reply to a .py file>", "Installs the replied python file if suitable to WarUserBot's codes.`\n**🚩 Flags :** `-f"
).add_command(
    "uninstall", "<plugin name>", "Uninstalls the given plugin from WarUserBot. To get that again do .restart", "uninstall alive"
).add_command(
    "load", "<plugin name>", "Loades the unloaded plugin to your WarUserBot", "load alive"
).add_command(
    "unload", "<plugin name>", "Unloads the plugin from your WarUserBot", "unload alive"
).add_command(
    "cmds", None, "Gives out the list of modules in WarUserBot."
).add_command(
    "repo", None, "Gives HellBot's Github repo link."
).add_command(
    "help", None, "Shows inline help menu."
).add_command(
    "plinfo", "<plugin name>", "Shows the detailed information of given plugin."
).add_command(
    "cmdinfo", "<cmd name>", "Shows the information of given command."
).add_warning(
    "❌ Install External Plugin On Your Own Risk. We won't help if anything goes wrong after installing a plugin."
).add()