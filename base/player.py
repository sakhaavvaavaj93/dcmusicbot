from typing import Dict

from pyrogram import types
from pytgcalls import idle

from .music_base import MusicPlayer
from .video_base import VideoPlayer
from .bot_base import pyro_bot
from .client_base import call_py
from dB.database import db

username = ""


class Methods(MusicPlayer, VideoPlayer):
    pass


class Player(Methods):
    async def play_or_stream(self, cb: types.CallbackQuery, result: Dict):
        user_id = result["user_id"]
        title = result["title"]
        duration = result["duration"]
        yt_url = result["yt_url"]
        yt_id = result["yt_id"]
        stream_type = result["stream_type"]
        chat_id = cb.message.chat.id
        if stream_type == "music":
            await self.play(cb, user_id, title, duration, yt_url, yt_id)
        elif stream_type == "stream":
            quality = db.get_chat(chat_id)[10]["video_quality"]
            await self.stream(
                cb, user_id, title, duration, yt_url, yt_id, quality
            )

    async def start(self):
        print("[ INFO ] STARTING BOT CLIENT")
        await pyro_bot.start()
        print("[ INFO ] GETTING BOT USERNAME")
        await self.get_username()
        print("[ INFO ] STARTING PyTgCalls CLIENT")
        await call_py.start()
        print("[ INFO ] CLIENT RUNNING")
        await idle()
        print("[ INFO ] STOPPING BOT")
        await pyro_bot.stop()

    @staticmethod
    async def get_username():
        global username
        me = await pyro_bot.get_me()
        username += me.username


player = Player()
