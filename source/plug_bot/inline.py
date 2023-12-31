from pyrogram import Client, filters,enums
from pyrogram.types import (InlineQueryResultArticle, InputTextMessageContent,
                            InlineKeyboardMarkup, InlineKeyboardButton)
from config import *
import asyncio


@bot.on_inline_query(filters.regex("^الاوامر$") )
async def answer(client, inline_query):
    reply_markup = InlineKeyboardMarkup(
            [[
             InlineKeyboardButton("①",callback_data="help1"),
             InlineKeyboardButton("②",callback_data="help2"),
             ],
             [
             InlineKeyboardButton("③",callback_data="help3"),
             InlineKeyboardButton("④",callback_data="help4"),
             ],
             [
             InlineKeyboardButton("⑤",callback_data="help5"),
             InlineKeyboardButton("⑥",callback_data="help6"),
             ],
             [
             InlineKeyboardButton("✅ - قناه السورس - ✅",url="https://t.me/RB_RO"),
             ],
             [
             InlineKeyboardButton("🔺️ - لتنصيب حسابك - 🔻",url="https://t.me/Y0Q_bot"),
             ]]
             )
    await inline_query.answer(
        results=[
            InlineQueryResultArticle(
                title="اوامر البوت",
                input_message_content=InputTextMessageContent(
                    "• اهلا بك في اوامر اليوزر البوت\n• ① اوامر الخاص\n• ② اوامر القنوات والمجموعات \n• ③ اوامر اليوتيوب \n• ④ اوامر الاذاعه\n• ⑤ اوامر التسليه \n• ⑥ اوامر اضافيه"
                ),
                url="https://t.me/RB_RO",
                description="𝐒𝐎𝐔𝐑𝐂𝐄 𝐕𝐄𝐍𝐎𝐌",
                reply_markup=reply_markup
            ),
        ],
        cache_time=1
    )
