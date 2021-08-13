from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton



@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAx0CQELqEwACJT9hFkRsyBfjMt4V-azZJt0IeojVKgACxQIAAiS6mVbvGguidLMMxSAE")
    await message.reply_text(
        f"""<b> Hi there,👋 {message.from_user.first_name}!
\n I can play music in voice chats of Telegeam Groups.
I have a lot of Super feature that will amaze you!
\nTo add in your group contact us at @dihan_official .
\nHit /help list of available commands.
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
                        "➕ Add Me To Your Group ➕", url="https://t.me/SophiaMusicBot?startgroup=true"
                    )]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""**Sophia Music Player Online ✅**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Updates Channel", url="https://t.me/dihanofficial")
                ]
            ]
        )
   )


@Client.on_message(
    filters.command("help")
    & filters.private
    & ~ filters.edited
)
async def help(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hey,{message.from_user.first_name}!
\n/play <song name> - play song you requested
/dplay <song name> - play song you requested via deezer
/splay <song name> - play song you requested via jio saavn
/playlist - Show now playing list
/current - Show now playing
/song <song name> - download songs you want quickly
/search <query> - search videos on youtube with details
/deezer <song name> - download songs you want quickly via deezer
/saavn <song name> - download songs you want quickly via saavn
/video <song name> - download videos you want quickly
\n*Admins only*
/player - open music player settings panel
/pause - pause song play
/resume - resume song play
/skip - play next song
/end - stop music play
/userbotjoin - invite assistant to your chat
/admincache - Refresh admin list
 </b>""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "💬 Updates Channel", url="https://t.me/dihanofficial"
                    ),
                    InlineKeyboardButton(
                        "💻 Support Group", url="https://t.me/dihan_official"
                    )
                ]
            ]
        )
    )    
