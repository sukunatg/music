import datetime
import random
import time

from telethon.errors import ChatSendInlineForbiddenError as noin
from telethon.errors.rpcerrorlist import BotMethodInvalidError as dedbot

from TelethonHell.DB.gvar_sql import gvarstat

from . import *

# -------------------------------------------------------------------------------

ALIVE_TEMP = """
<b><i>🔥🔥ᴘʀᴏxɪᴍᴀ ᴜꜱᴇʀʙᴏᴛ ɪꜱ ʜᴇʀᴇ🔥🔥</i></b>  
<i><b> » ᴏᴡɴᴇʀ </i></b> :  <a href='tg://user?id={}'>{}</a> 
 <b>» ᴛᴇʟᴇᴛʜᴏɴ :</b> <i>{}</i>
 <b>» ᴘʀᴏxɪᴍᴀʙᴏᴛ :</b> <i>{}</i>
 <b>» sᴜᴅᴏ :</b> <i>{}</i>
 <b>» ᴜᴘᴛɪᴍᴇ :</b> <i>{}</i>
 <b>» ᴘɪɴɢ :</b> <i>{}</i>
<b><i>❤️‍🔥 <a href='https://graph.org/PROXIMA-USERBOT-05-26'>[ ᴘʀᴏxɪᴍᴀʙᴏᴛ ]</a> ❤️‍🔥</i></b>
"""

msg = """{}\n
<b><i> ❤️‍🔥 ʙᴏᴛ sᴛᴀᴛᴜs ❤️‍🔥  </b></i>
<b> ᴛᴇʟᴇᴛʜᴏɴ :</b>  <i>{}</i>
<b> ᴘʀᴏxɪᴍᴀʙᴏᴛ :</b>  <i>{}</i>
<b> ᴜᴘᴛɪᴍᴇ :</b>  <i>{}</i>
<b> ᴀʙᴜsᴇ :</b>  <i>{}</i>
<b> sᴜᴅᴏ :</b>  <i>{}</i>
"""
# -------------------------------------------------------------------------------


@hell_cmd(pattern="proxima$")
async def up(event):
    ForGo10God, HELL_USER, hell_mention = await client_id(event)
    start = datetime.datetime.now()
    reply = await event.get_reply_message()
    hell = await eor(event, "`Building Alive....`")
    uptime = await get_time((time.time() - StartTime))
    alive_name = gvarstat("ALIVE_NAME") or HELL_USER
    a = gvarstat("ALIVE_PIC")
    pic_list = []
    if a:
        b = a.split(" ")
        if len(b) >= 1:
            for c in b:
                pic_list.append(c)
        PIC = random.choice(pic_list)
    else:
        PIC = "https://graph.org/file/123baddab9a3de00aa390.mp4"
    end = datetime.datetime.now()
    ling = (end - start).microseconds / 1000
    omk = ALIVE_TEMP.format(ForGo10God, alive_name, tel_ver, hell_ver, is_sudo, uptime, ling)
    await event.client.send_file(
        event.chat_id,
        file=PIC,
        caption=omk,
        parse_mode="HTML",
        reply_to=reply,
    )
    await hell.delete()





CmdHelp("alive").add_command(
    "proxima", None, "Shows the Default Alive Message"
).add_warning(
    "✅ Harmless Module"
).add()
