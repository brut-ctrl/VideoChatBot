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
from config import Config
from pyrogram import Client, filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified

CHAT_ID = Config.CHAT_ID
USERNAME = Config.BOT_USERNAME
HOME_TEXT = "👋🏻 **Hi Dude [{}](tg://user?id={})**, \n\n🤖 Im **Video Chat Bot**. \nI Can Stream Lives, Radios, YouTube Videos & Telegram Video Files On Voice Chat Of Telegram Channels & Groups"
HELP_TEXT = """
🏷️ **Setting Up** :

\u2022 Start a voice chat in your channel or group.
\u2022 Add bot and user account in chat with admin rights.
\u2022 Use /stream YouTube link or /stream live stream link or /stream as a reply to an video file.

🏷️ **Common Commands** :

\u2022 `/start` - start the bot
\u2022 `/help` - show help message

🏷️ **Admin Only Commands** :

\u2022 `/radio` - start streaming the radio
\u2022 `/stream` - start streaming the video
\u2022 `/nstream` - stop streaming the video
"""

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("💌 Contact Me", url="https://t.me/dunottagme"),
                InlineKeyboardButton("🏷️ Join Here", url="https://t.me/fantaestheticgang"),
            ],
            [
                InlineKeyboardButton("🤖 Make Own Bot", url="https://heroku.com/deploy?template=https://github.com/brut-ctrl/VideoChatBot"),
            ],
            [
                InlineKeyboardButton("🔙 Back", callback_data="home"),
                InlineKeyboardButton("🔚 Close", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        buttons = [
            [
                InlineKeyboardButton("SEARCH INLINE", switch_inline_query_current_chat=""),
            ],
            [
                InlineKeyboardButton("💌 Contact Me", url="https://t.me/dunottagme"),
                InlineKeyboardButton("🏷️ Join Here", url="https://t.me/fantaestheticgang"),
            ],
            [
                InlineKeyboardButton("🤖 Make Own Bot", url="https://heroku.com/deploy?template=https://github.com/brut-ctrl/VideoChatBot"),
            ],
            [
                InlineKeyboardButton("🤔 Help Menu", callback_data="help"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start", f"start@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def start(client, message):
    buttons = [
            [
                InlineKeyboardButton("SEARCH INLINE", switch_inline_query_current_chat=""),
            ],
            [
                InlineKeyboardButton("💌 Contact Me", url="https://t.me/dunottagme"),
                InlineKeyboardButton("🏷️ Join Here", url="https://t.me/fantaestheticgang"),
            ],
            [
                InlineKeyboardButton("🤖 Make Own Bot", url="https://heroku.com/deploy?template=https://github.com/brut-ctrl/VideoChatBot"),
            ],
            [
                InlineKeyboardButton("🤔 Help Menu", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help", f"help@{USERNAME}"]) & (filters.chat(CHAT_ID) | filters.private))
async def help(client, message):
    buttons = [
            [
                InlineKeyboardButton("💌 Contact Me", url="https://t.me/dunottagme"),
                InlineKeyboardButton("🏷️ Join Here", url="https://t.me/fantaestheticgang"),
            ],
            [
                InlineKeyboardButton("🤖 Make Own Bot", url="https://heroku.com/deploy?template=https://github.com/brut-ctrl/VideoChatBot"),
            ],
            [
                InlineKeyboardButton("🔙 Back", callback_data="home"),
                InlineKeyboardButton("🔚 Close", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_text(text=HELP_TEXT, reply_markup=reply_markup)
