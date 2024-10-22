from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

HKZ = Client(
  name="Elizabeth-Olsen",
  api_id="25988816",
  api_hash="7ad4c2b1e5556277d341477b0776b2de",
  bot_token="8127557975:AAGcuavIDOjKQcMpS6VqjkBENh6IT6JLwD0"
)

@HKZ.on_message(filters.command("start"))
async def start(client, message):
    await message.reply(
        text=f"""Hey there {message.from_user.mention} 👋,

I am [Elizabeth Olsen](t.me/HollywoodMalayalamMovieBot),I can share you Malayalam Dubbed Hollywood Movies. Just Send Me the Movie Name you want 😍

Hit /help to know more ✨"""
    )

@HKZ.on_message(filters.command("help"))
async def help(client, message):
    await message.reply(
        text=f"""Hey {message.from_user.mention} ✨

Basic Commands:
/start - Check I am Alive ☑
/help  - To Reach Here
/about - About Me 🤠
/list  - Check the Movies I have

Instructions:

When you will request the Movie You want to login with your Telegram Phone Number.

Then You will Receive a Code from Telegram, Just Send the Code to Me.

After Login The Movie File will be upload in your Telegram Saved Messages.

Note:- You Can request only 2 Movies Per Week..!
If the Movie didn't got please request Again..!"""
    )

@HKZ.on_message(filters.command("about"))
async def about(client, message):
    await message.reply(
        text=f"""Hey {message.from_user.mention} ✨

✰ My Name  : [Elizabeth Olsen](t.me/HollywoodMalayalamMovieBot]
✰ Language : [Python 3.13.0](www.python.org)
✰ Library  : Pyrogram, Tgcrypto
✰ Server   : [Render](www.render.com)"""
    )



@HKZ.on_message(filters.text)
async def titanic_txt(client, message):
    await message.reply(
        text=f"<b>Here is What I Found for Your Query #{message.text}</b>..!",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(f"<b>{message.text}</b> Malayalam Dubbed Full Movie @HollywoodMalayalamMovieBot.mkv</b>", callback_data="mission")
            ]]
            )
        )

@HKZ.on_message(filters.text)
async def robbhood_txt(client, message):
    await message.reply(
        text=f"<b>Here is What I Found for Your Query #{message.text}</b>..!",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(f"<b>{message.text} Malayalam Dubbed Full Movie @HollywoodMalayalamMovieBot.mkv</b>", callback_data="mission")
            ]]
            )
        )

@HKZ.on_message(filters.text)
async def natm_txt(client, message):
    await message.reply(
        text=f"<b>Here is What I Found for Your Query #{message.text}</b>..!",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(f"<b>{message.text} Malayalam Dubbed Full Movie @HollywoodMalayalamMovieBot.mkv</b>", callback_data="mission")
            ]]
            )
        )
    

@HKZ.on_message(filters.text)
async def iceage_txt(client, message):
    await message.reply(
        text=f"<b>Here is What I Found for Your Query #{message.text}</b>..!",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(f"<b>{message.text} Malayalam Dubbed Full Movie @HollywoodMalayalamMovieBot.mkv</b>", callback_data="mission")
            ]]
    )


print("Bot Started")
HKZ.run()
