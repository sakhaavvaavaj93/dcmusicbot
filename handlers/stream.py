from pyrogram import Client, filters, types
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from utils.call_functions import (
    extract_info,
    stream_result,
    yt_search,
    process_button,
)


def extract_all(query: str, chat_id: int, user_id: int, status: str):
    yt_btn = process_button(user_id, status)
    yt_search(chat_id, query)
    result = extract_info(chat_id, stream_result)
    return result, yt_btn


@Client.on_message(filters.command("play") & filters.group)
async def play_(_, message: types.Message):
    query = " ".join(message.command[1:])
    chat_id = message.chat.id
    user_id = message.from_user.id
    status = "music"
    result, yt_btn = extract_all(query, chat_id, user_id, status)
    await message.reply(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                yt_btn[0],
                yt_btn[1],
                [
                    InlineKeyboardButton("🗑", f"close|{user_id}"),
                    InlineKeyboardButton("➡", "nextmusic"),
                ],
            ],
        ),
    )
    await message.delete()

@Client.on_message(filters.command("vplay") & filters.group)
async def vplay_(_, message: types.Message):
    query = " ".join(message.command[1:])
    chat_id = message.chat.id
    user_id = message.from_user.id
    status = "stream"
    result, yt_btn = extract_all(query, chat_id, user_id, status)
    await message.reply(
        result,
        reply_markup=InlineKeyboardMarkup(
            [
                yt_btn[0],
                yt_btn[1],
                [
                    InlineKeyboardButton("🗑", f"close|{user_id}"),
                    InlineKeyboardButton("➡", "nextstream"),
                ],
            ]
        ),
    )
    await message.delete()
