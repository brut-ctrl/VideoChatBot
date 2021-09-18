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
import ffmpeg
import asyncio
import subprocess
from asyncio import sleep
from signal import SIGINT
from config import Config, Database
from pyrogram import Client, filters
from pyrogram.types import Message
from bot.videochatbot.player import ydl, group_call_factory

ADMINS = Config.ADMINS
CHAT_ID = Config.CHAT_ID
USERNAME = Config.BOT_USERNAME
VIDEO_CALL = Database.VIDEO_CALL
RADIO_CALL = Database.RADIO_CALL
FFMPEG_PROCESSES = Database.FFMPEG_PROCESSES

@Client.on_message(filters.command(["radio", f"radio@{USERNAME}"]) & filters.user(ADMINS) & (filters.chat(CHAT_ID) | filters.private))
async def radio(client, m: Message):
    if not ' ' in m.text:
        await m.reply_text("‼️ __Send Me An Live Stream Link YouTube, Video Link or Reply To An Video to Start Video Streaming__‼️")
        return

    text = m.text.split(' ', 1)
    query = text[1]
    input_filename = f'radio-{CHAT_ID}.raw'
    msg = await m.reply_text("⏳ `Processing...`")

    vid_call = VIDEO_CALL.get(CHAT_ID)
    if vid_call:
        await VIDEO_CALL[CHAT_ID].stop()
        VIDEO_CALL.pop(CHAT_ID)
        await sleep(3)

    process = FFMPEG_PROCESSES.get(CHAT_ID)
    if process:
        try:
            process.send_signal(SIGINT)
            await sleep(3)
        except Exception as e:
            print(e)
            pass

    regex = r"^(https?\:\/\/)?(www\.youtube\.com|youtu\.?be)\/.+"
    match = re.match(regex,query)
    if match:
        try:
            meta = ydl.extract_info(query, download=False)
            formats = meta.get('formats', [meta])
            for f in formats:
                ytstreamlink = f['url']
            station_stream_url = ytstreamlink
        except Exception as e:
            await msg.edit(f"😵‍💫 **YouTube Download Error!** \n\nBot Brain was Error: `{e}`")
            print(e)
            return
    else:
        station_stream_url = query
        print(station_stream_url)

    process = (
        ffmpeg.input(station_stream_url)
        .output(input_filename, format='s16le', acodec='pcm_s16le', ac=2, ar='48k')
        .overwrite_output()
        .run_async()
    )
    FFMPEG_PROCESSES[CHAT_ID] = process

    if CHAT_ID in RADIO_CALL:
        await sleep(1)
        await msg.edit(f"📻 **Starting Play [Radio Streaming]({query})!**", disable_web_page_preview=True)
    else:
        await msg.edit("📻 `Starting Play Radio Stream...`")
        await sleep(2)
        group_call = group_call_factory.get_file_group_call(input_filename)
        try:
            await group_call.start(CHAT_ID)
            RADIO_CALL[CHAT_ID] = group_call
            await msg.edit(f"📻 **Starting Play [Radio Streaming]({query})!**", disable_web_page_preview=True)
        except Exception as e:
            await msg.edit(f"😵‍💫 **An Error Occoured!** \n\nBot Brain was Error: `{e}`")
