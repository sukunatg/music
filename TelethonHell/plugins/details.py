import os
from telethon import events

@bot.on(events.NewMessage(pattern=r"\.detail$", outgoing=True))
async def detail(event):
    if event.sender_id == (await event.client.get_me()).id and not event.is_reply:
        # Get the values of the required environment variables
        heroku_app_name = os.getenv('HEROKU_APP_NAME', 'Not set')
        guesser_var = os.getenv('guesser', 'False')
        trail_var = os.getenv('TRAIL', 'Yes')

        # Prepare the details message
        details_message = (
            f"🔰 𝘿𝙀𝙏𝘼𝙄𝙇𝙎 🔰\n"
            f"-----------------------------------------------\n"
            f"𝘼𝙋𝙋 𝙉𝘼𝙈𝙀👤: {heroku_app_name}\n"
            f"𝘼𝙐𝙏𝙊 𝙂𝙐𝙀𝙎𝙎🔎: {guesser_var}\n"
            f"𝙋𝙍𝙀𝙈𝙄𝙐𝙈 𝙐𝙎𝙀𝙍❓: {trail_var}✅\n"
            f"-----------------------------------------------\n"
        )

        # Edit the invoked command message with the details
        await event.edit(details_message)
