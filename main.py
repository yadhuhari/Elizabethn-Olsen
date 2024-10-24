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

I am [Elizabeth Olsen](t.me/HollywoodMalayalamMovieBot),I can share you Malayalam Dubbed Hollywood Movies. Just Click in the Movies List Button and Choose the Movie you want 😍

Hit /help to know more ✨""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Movies List 🌼", callback_data="list"),
            ],[
            InlineKeyboardButton("Help 🛠", callback_data="help"),
            InlineKeyboardButton("About 🤠", callback_data="about")
            ]]
            )
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
If the Movie didn't got please request Again..!""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Movies List 🌼", callback_data="list"),
            ],[
            InlineKeyboardButton("Home 🏡", callback_data="start"),
            InlineKeyboardButton("About 🤠", callback_data="about")
            ]]
            )
        )

@HKZ.on_message(filters.command("about"))
async def about(client, message):
    await message.reply(
        text=f"""Hey {message.from_user.mention} ✨

✰ My Name  : [Elizabeth Olsen](t.me/HollywoodMalayalamMovieBot)
✰ Language : [Python 3.13.0](www.python.org)
✰ Library  : Pyrogram, Tgcrypto
✰ Server   : [Render](www.render.com)""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("Home 🏡", callback_data="start"),
            InlineKeyboardButton("Help 🛠", callback_data="help")
            ]]
            )
        )




@HKZ.on_message(filters.text)
async def natm_txt(client, message):
    await message.reply(
        text=f"<b>Here is What I Found for Your Query #{message.text}</b>..!",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(text=f"<b>{message.text} Malayalam Dubbed Full Movie @HollywoodMalayalamMovieBot.mkv</b>", callback_data="mission")
            ]]
            )
        )

@HKZ.on_message(filters.command("list"))
async def list(client, message):
    await message.reply(
        text="""Here is the List of Movies I have..!

Note:- You can only request 2 Movies in a week..!""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("300", callback_data="300"),
            InlineKeyboardButton("2012", callback_data="2012"),
            ],[
            InlineKeyboardButton("Agent Cody Banks", callback_data="agentcodybanks"),
            InlineKeyboardButton("Avengers Infinity War", callback_data="avengers"),
            ],[
            InlineKeyboardButton("Anaconda", callback_data="anaconda"),
            InlineKeyboardButton("Anaconda 2", callback_data="anaconda2"),
            ],[
            InlineKeyboardButton("Anaconda 3", callback_data="anaconda3"),
            InlineKeyboardButton("Ben Hur (1959)", callback_data="benhur1"),
            ],[
            InlineKeyboardButton("Ben Hur (2016)", callback_data="benhur2"),
            InlineKeyboardButton("Black Widow", callback_data="blackwidow"),
            ],[
            InlineKeyboardButton("Captain Phillips", callback_data="captainphilips"),
            InlineKeyboardButton("CZ12", callback_data="cz12"),
            ],[
            InlineKeyboardButton("Die Another Day", callback_data="dieanotherday"),
            InlineKeyboardButton("Die Hard", callback_data="diehard"),
            ],[
            InlineKeyboardButton("Django Unchained", callback_data="djangounchained"),
            InlineKeyboardButton("Doctor Strange 2", callback_data="drstrange2"),
            ],[
          
        )

@HKZ.on_callback_query()
async def callback(bot, msg):
    if msg.data == "mission":
        await msg.message.edit_text("""𝖳𝗁𝗂𝗌 𝗂𝗌 𝗍𝗁𝖾 𝗉𝗋𝗈𝖼𝖾𝗌𝗌 𝗍𝗈 𝗅𝗈𝗀𝗂𝗇 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖺𝖼𝖼𝗈𝗎𝗇𝗍. 𝖨 𝖺𝗆 𝗅𝗈𝗀𝗂𝗇 𝗍𝗈 𝗒𝗈𝗎𝗋 𝖺𝖼𝖼𝗈𝗎𝗇𝗍 𝗍𝗈 𝗎𝗉𝗅𝗈𝖺𝖽 𝗍𝗁𝖾 𝖿𝗂𝗅𝖾 𝗂𝗇 𝗒𝗈𝗎𝗋 𝖲𝖺𝗏𝖾𝖽 𝖬𝖾𝗌𝗌𝖺𝗀𝖾𝗌

𝖤𝗇𝗍𝖾𝗋 𝗍𝗁𝖾 𝗉𝗁𝗈𝗇𝖾 𝗇𝗎𝗆𝖻𝖾𝗋, 𝖺𝗅𝗈𝗇𝗀 𝗐𝗂𝗍𝗁 𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝖼𝗈𝖽𝖾. 𝖤𝗑𝖺𝗆𝗉𝗅𝖾: +91876543210"""
        )
    elif msg.data == "start":
        await msg.message.edit_text(f"""Hey there {message.from_user.mention} 👋,

I am [Elizabeth Olsen](t.me/HollywoodMalayalamMovieBot),I can share you Malayalam Dubbed Hollywood Movies. Just Send Me the Movie Name you want 😍

Hit /help to know more ✨"""
        )
    elif msg.data == "help":
        await msg.message.edit_text(f"""Hey {msg.from_user.mention} ✨

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
    elif msg.data == "about":
        await msg.message.edit_text(f"""Hey {msg.from_user.mention} ✨

✰ My Name  : [Elizabeth Olsen](t.me/HollywoodMalayalamMovieBot)
✰ My Owner : [SOUL TG](www.github.com/SOULTG)
✰ Language : [Python 3.13.0](www.python.org)
✰ Library  : Pyrogram, Tgcrypto
✰ Server   : [Render](www.render.com)"""
        )


print("Bot Started")
HKZ.run()
