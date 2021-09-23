from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b> Hi there,👋 {message.from_user.first_name}!
\nThis is Sophia Music Bot.
I play music on Telegram's Voice Chats.
\nFo More Help Use Buttons Below:
 </b>""",
      
       
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "🛠 Source Code 🛠", url="https://github.com/dihanofficial/sophiamusic-v6")
                  ],[
                    InlineKeyboardButton(
                        "💬 Updates Channel", url="https://t.me/dihanofficial"
                    ),
                    InlineKeyboardButton(
                        "💻 Support Group", url="https://t.me/dihan_official"
                    )
                ],[ 
                    InlineKeyboardButton(
                        "➕ Add Me To Your Group ➕", url="https://t.me/SophiaSLBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""*Sophia Music Bot is alive.*""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Updates Channel", url="https://t.me/dihanofficial")
                ]
            ]
        )
   )


