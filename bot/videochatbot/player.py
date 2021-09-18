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

import os
import re
import sys
import time
import ffmpeg
import asyncio
import subprocess
from signal import SIGINT
from asyncio import sleep
from config import Config, Database
from bot.videochatbot.nopm import User
from youtube_dl import YoutubeDL
from pyrogram import Client, filters
from pyrogram.types import Message
from pytgcalls import GroupCallFactory
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

ADMINS = Config.ADMINS
CHAT_ID = Config.CHAT_ID
USERNAME = Config.BOT_USERNAME
VIDEO_CALL = Database.VIDEO_CALL
RADIO_CALL = Database.RADIO_CALL
FFMPEG_PROCESSES = Database.FFMPEG_PROCESSES


ydl_opts = {
        "geo_bypass": True,
        "nocheckcertificate": True,
}
ydl = YoutubeDL(ydl_opts)
group_call_factory = GroupCallFactory(User, GroupCallFactory.MTPROTO_CLIENT_TYPE.PYROGRAM)

@Client.on_message(filters.command(["stream", f"stream@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT_ID) | filters.private))
async def stream(client, m: Message):
    media = m.reply_to_message
    if media.video or media.document:
        msg = await m.reply_text("⏳ `Processing...`")

        process = FFMPEG_PROCESSES.get(CHAT_ID)
        if process:
            try:
                process.send_signal(SIGINT)
                await sleep(3)
            except Exception as e:
                print(e)
                pass

        vid_call = VIDEO_CALL.get(CHAT_ID)
        if vid_call:
            await VIDEO_CALL[CHAT_ID].stop()
            VIDEO_CALL.pop(CHAT_ID)
            await sleep(3)

        rad_call = RADIO_CALL.get(CHAT_ID)
        if rad_call:
            await RADIO_CALL[CHAT_ID].stop()
            RADIO_CALL.pop(CHAT_ID)
            await sleep(3)

        await msg.edit("📥 `Downloading ...`")
        video = await client.download_media(media)
        await sleep(2)
        group_call = group_call_factory.get_group_call()
        if group_call.is_connected:
            try:
                await group_call.start_video(video, with_audio=True)
                VIDEO_CALL[CHAT_ID] = group_call
                await msg.edit(f"📺 **Start Playing [Video Streaming](https://github.com/brut-ctrl/VideoChatBot)**", disable_web_page_preview=True)
            except Exception as e:
                await msg.edit(f"😵‍💫 **An Error Occoured!** \n\nBot Brain was Error: `{e}`")
        else:
            try:
                await group_call.join(CHAT_ID)
                await group_call.start_video(video, with_audio=True)
                VIDEO_CALL[CHAT_ID] = group_call
                await msg.edit(f"📺 **Start Playing [Video Streaming](https://github.com/brut-ctrl/VideoChatBot)**", disable_web_page_preview=True)
            except Exception as e:
                await msg.edit(f"😵‍💫 **An Error Occoured!** \n\nBot Brain was Error: `{e}`")

    elif ' ' in m.text:
        text = m.text.split(' ', 1)
        query = text[1]
        msg = await m.reply_text("⏳ `Processing...`")

        process = FFMPEG_PROCESSES.get(CHAT_ID)
        if process:
            try:
                process.send_signal(SIGINT)
                await sleep(3)
            except Exception as e:
                print(e)
                pass

        vid_call = VIDEO_CALL.get(CHAT_ID)
        if vid_call:
            await VIDEO_CALL[CHAT_ID].stop()
            VIDEO_CALL.pop(CHAT_ID)
            await sleep(3)

        rad_call = RADIO_CALL.get(CHAT_ID)
        if rad_call:
            await RADIO_CALL[CHAT_ID].stop()
            RADIO_CALL.pop(CHAT_ID)
            await sleep(3)

        regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
        match = re.match(regex,query)
        if match:
            await msg.edit("📢 `Starting Play YouTube Stream...`")
            try:
                meta = ydl.extract_info(query, download=False)
                formats = meta.get('formats', [meta])
                for f in formats:
                        ytstreamlink = f['url']
                ytstream = ytstreamlink
            except Exception as e:
                await msg.edit(f"😵‍💫 **YouTube Download Error!** \n\nBot Brain was Error: `{e}`")
                print(e)
                return
            await sleep(2)
            group_call = group_call_factory.get_group_call()
            if group_call.is_connected:
                try:
                    await group_call.start_video(ytstream, with_audio=True)
                    VIDEO_CALL[CHAT_ID] = group_call
                    await msg.edit(f"📺 **Start Playing [YouTube Streaming]({query})!**", disable_web_page_preview=True)
                except Exception as e:
                    await msg.edit(f"😵‍💫 **An Error Occoured!** \n\nBot Brain was Error: `{e}`")
            else:
                try:
                    await group_call.join(CHAT_ID)
                    await group_call.start_video(ytstream, with_audio=True)
                    VIDEO_CALL[CHAT_ID] = group_call
                    await msg.edit(f"📺 **Start Playing [YouTube Streaming]({query})!**", disable_web_page_preview=True)
                except Exception as e:
                    await msg.edit(f"😵‍💫 **An Error Occoured!** \n\nBot Brain was Error: `{e}`")
        else:
            await msg.edit("🎦 `Starting Play Live Stream...`")
            livestream = query
            await sleep(2)
            group_call = group_call_factory.get_group_call()
            if group_call.is_connected:
                try:
                    await group_call.start_video(livestream, with_audio=True)
                    VIDEO_CALL[CHAT_ID] = group_call
                    await msg.edit(f"🎦 **Start Playing [Live Streaming]({query})!**", disable_web_page_preview=True)
                except Exception as e:
                    await msg.edit(f"😵‍💫 **An Error Occoured!** \n\nBot Brain was Error: `{e}`")
            else:
                try:
                    await group_call.join(CHAT_ID)
                    await group_call.start_video(livestream, with_audio=True)
                    VIDEO_CALL[CHAT_ID] = group_call
                    await msg.edit(f"🎦 **Started [Live Streaming]({query})!**", disable_web_page_preview=True)
                except Exception as e:
                    await msg.edit(f"😵‍💫 **An Error Occoured!** \n\nBot Brain was Error: `{e}`")

    else:
        await m.reply_text("‼️ __Send Me An Live Stream Link YouTube, Video Link or Reply To An Video to Start Video Streaming__‼️")


@Client.on_message(filters.command(["nstream", f"nstream@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT_ID) | filters.private))
async def nstream(client, m: Message):
    msg = await m.reply_text("⏳ `Processing...`")

    process = FFMPEG_PROCESSES.get(CHAT_ID)
    if process:
        try:
            process.send_signal(SIGINT)
            await sleep(3)
        except Exception as e:
            print(e)
            pass

    if CHAT_ID in RADIO_CALL:
        await RADIO_CALL[CHAT_ID].stop()
        RADIO_CALL.pop(CHAT_ID)
        await msg.edit("⏹️ **Stopped Radio Streaming!**")

    elif CHAT_ID in VIDEO_CALL:
        await VIDEO_CALL[CHAT_ID].stop()
        VIDEO_CALL.pop(CHAT_ID)
        await msg.edit("⏹️ **Stopped Video Streaming!**")

    else:
        await msg.edit("🤖 **Please Start An Stream First!**")


admincmds=["stream", "radio", "nstream", f"stream@{USERNAME}", f"radio@{USERNAME}", f"nstream@{USERNAME}"]

@Client.on_message(filters.command(admincmds) & ~filters.user(ADMINS) & (filters.chat(CHAT_ID) | filters.private))
async def notforu(_, m: Message):
    k = await m.reply_sticker("CAACAgUAAxkBAAEBpyZhF4R-ZbS5HUrOxI_MSQ10hQt65QACcAMAApOsoVSPUT5eqj5H0h4E")
    await sleep(5)
    await k.delete()
    try:
        await m.delete()
    except:
        pass

allcmd = ["start", "help", f"start@{USERNAME}", f"help@{USERNAME}"] + admincmds

@Client.on_message(filters.command(allcmd) & filters.group & ~filters.chat(CHAT_ID))
async def not_chat(_, m: Message):
    buttons = [
            [
                InlineKeyboardButton("💌 Contact Me", url="https://t.me/dunottagme"),
                InlineKeyboardButton("🏷️ Join Here", url="https://t.me/fantaestheticgang"),
            ],
            [
                InlineKeyboardButton("🤖 Make Own Bot", url="https://heroku.com/deploy?template=https://github.com/brut-ctrl/VideoChatBot"),
            ]
         ]
    await m.reply_text(text="**So Sorry Dude... You Cant Use This Bot In This Group! But You Can Make Your Own Bot Like This From The [Source Code](https://github.com/brut-ctrl/VideoChatBot) Below 😉!**", reply_markup=InlineKeyboardMarkup(buttons), disable_web_page_preview=True)
