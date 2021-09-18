# Telegram Video Chat Bot (Beta)


**📢 Video Chat Stream Telegram Bot**

```
🤖 Can Stream Live Videos, Radios, YouTube Videos & Telegram Video Files On Your Video Chat Of Channels & Groups!
```


## Main Features

- Supports Live Streaming
- Supports YouTube Streaming
- Supports Live Radio Streaming
- Supports Video Files Streaming
- Supports YouTube Live Streaming
- Customizable Userbot Protection

## Deploy

### Railway App

<p><a href="https://railway.app/new/template?template=https%3A%2F%2Fgithub.com%2Fbrut-ctrl%2FVideoChatBot&envs=API_ID%2CAPI_HASH%2CBOT_TOKEN%2CSESSION_STRING%2CCHAT_ID%2CAUTH_USERS%2CBOT_USERNAME%2CREPLY_MESSAGE&optionalEnvs=REPLY_MESSAGE&API_IDDesc=User+Account+Telegram+API_ID+get+it+from+my.telegram.org%2Fapps&API_HASHDesc=User+Account+Telegram+API_HASH+get+it+from+my.telegram.org%2Fapps&BOT_TOKENDesc=Your+Telegram+Bot+Token%2C+get+it+from+%40Botfather+XD&SESSION_STRINGDesc=Pyrogram+Session+String+of+User+Account%2C+get+it+from+%40genStr_robot&CHAT_IDDesc=ID+of+your+Channel+or+Group+where+the+bot+will+works+or+stream+videos&AUTH_USERSDesc=ID+of+Auth+Users+who+can+use+Admin+commands+%28for+multiple+users+seperated+by+space%29&BOT_USERNAMEDesc=Your+Telegram+Bot+Username+without+%40%2C+get+it+from+%40Botfather+XD&REPLY_MESSAGEDesc=A+reply+message+to+those+who+message+the+USER+account+in+PM.+Make+it+blank+if+you+do+not+need+this+feature.&REPLY_MESSAGEDefault=Hello+Sir%2C+I%27m+a+bot+to+stream+videos+on+telegram+voice+chat%2C+not+having+time+to+chat+with+you+%F0%9F%98%82%21&referralCode=oAwpFa"><img src="https://img.shields.io/badge/Deploy%20To%20Railway-blueviolet?style=for-the-badge&logo=railway" width="200""/></a></p>

### Heroku

<p><a href="https://heroku.com/deploy?template=https://github.com/brut-ctrl/VideoChatBot"><img src="https://img.shields.io/badge/Deploy%20To%20Heroku-blueviolet?style=for-the-badge&logo=heroku" width="200""/></a></p>

## Commands (Botfather)
```sh
start - Start The Bot
help - Show Help Message
radio - Start Radio Streaming
stream - Start Video Streaming
nstream - Stop Video Streaming
```

## Config Vars
1. `API_ID` : User Account Telegram API_ID, get it from `my.telegram.org`
2. `API_HASH` : User Account Telegram API_HASH, get it from `my.telegram.org`
3. `BOT_TOKEN` : Your Telegram Bot Token, get it from **@Botfather**
4. `BOT_USERNAME` : Your Telegram Bot Username, get it from **@Botfather**
4. `SESSION_STRING` : Pyrogram Session String of User Account, get it from [@SessionGeneratorBot](http://t.me/SessionGeneratorBot) or [![GenerateStringName](https://img.shields.io/badge/repl.it-generateStringName-yellowgreen)](https://repl.it/@brut69/getStringName)
5. `CHAT_ID` : ID of Channel/Group where the bot will works or stream videos.
6. `AUTH_USERS` : ID of Users who can use Admins commands. For multiple users seperated by space.
7. `REPLY_MESSAGE` : A reply to those who message the USER account in PM. Leave it blank if you do not need this feature.


## Requirements
- Python 3.8 or Higher
- Latest [FFmpeg](https://www.ffmpeg.org/)
- [Telegram API key](https://docs.pyrogram.org/intro/quickstart#enjoy-the-api)
- Pyrogram [String Session](http://t.me/SessionGeneratorBot) Of The Account.
- The User Account Needs To Be An Admin In The Group/Channel.


## Self Hosting on VPS
```sh
$ git clone https://github.com/brut-ctrl/VideoChatBot.git
$ cd VideoChatBot
$ sudo apt-get install python3-pip ffmpeg
$ pip3 install -U pip
$ pip3 install -U -r requirements.txt
# <create .env variables appropriately>
$ python3 -m bot
```


## License
```sh
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
```

## Credits
- **[py-tgcalls](https://github.com/pytgcalls/pytgcalls)**
- **[subinps](https://t.me/subin_works) for Brilliant Source Code**
- **[Dan](https://github.com/delivrance) for [Pyrogram](https://github.com/pyrogram/pyrogram)**
- **[Safone](https://github.com/AsmSafone) for [Repo](https://github.com/AsmSafone/VideoPlayerBot)**
- **[MarshalX](https://github.com/MarshalX) for [pytgcalls](https://github.com/MarshalX/tgcalls)**
- **[Its-fork](https://github.com/Itz-fork)**
- **TeamDaisyX**
- **TheHamkerCat**
- **And Thanks To All**
