"""
VideoChatBot, Telegram Video Chat Bot
Copyright (C) 2021 brut //  <https://github.com/brut-ctrl>

Copyright (C) 2007 Free Software Foundation, Inc. <https://fsf.org/>
Everyone is permitted to copy and distribute verbatim copies
of this license document, but changing it is not allowed.
The GNU Affero General Public License is a free, copyleft license for
software and other kinds of works, specifically designed to ensure
cooperation with the community in the case of network server software.
The licenses for most software and other practical works are designed
to take away your freedom to share and change the works.  By contrast,
our General Public Licenses are intended to guarantee your freedom to
share and change all versions of a program--to make sure it remains free
software for all its users.
The GNU Affero General Public License is designed specifically to
ensure that, in such cases, the modified source code becomes available
to the community.  It requires the operator of a network server to
provide the source code of the modified version running there to the
users of that server.  Therefore, public use of a modified version, on
a publicly accessible server, gives the public access to the source
code of the modified version
"""

import asyncio
from pyrogram import Client, filters
from config import Config
from pyrogram.errors import BotInlineDisabled

ADMINS = Config.ADMINS
USERNAME = Config.BOT_USERNAME
REPLY_MESSAGE = Config.REPLY_MESSAGE

User = Client(
    Config.SESSION_STRING,
    Config.API_ID,
    Config.API_HASH
)

@User.on_message(filters.private & filters.incoming & ~filters.bot & ~filters.service & ~filters.me & ~filters.edited)
async def nopm(client, message):
    if REPLY_MESSAGE is not None:
        try:
            inline = await client.get_inline_bot_results(USERNAME, "VideoChatBot")
            await client.send_inline_bot_result(
                message.chat.id,
                query_id=inline.query_id,
                result_id=inline.results[0].id,
                hide_via=True
            )
        except BotInlineDisabled:
            for admin in ADMINS:
                try:
                    await client.send_message(chat_id=admin, text=f"**Hello Sar 👋\nInline Mode Isn't Enabled For Your @{USERNAME} Yet. A Nibba Is Spaming Me In PM! Enable Inline Mode For Your @{USERNAME} From @Botfather To Reply With Him!**")
                except Exception as e:
                    print(e)
                    pass
        except Exception as e:
            print(e)
            pass
