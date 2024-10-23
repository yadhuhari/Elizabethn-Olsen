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

Hit /help to know more ✨""",
        reply_markup=InlineKeyboardMarkup( [[
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
async def titanic_txt(client, message):
    await message.reply(
        text=f"<b>Here is What I Found for Your Query #{message.text}</b>..!",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(text=f"<b>{message.text} Malayalam Dubbed Full Movie @HollywoodMalayalamMovieBot.mkv</b>", callback_data="mission")
            ]]
            )
        )

@HKZ.on_message(filters.text)
async def iceage_txt(client, message):
    await message.reply(
        text=f"<b>Here is What I Found for Your Query #{message.text}</b>..!",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton(text=f"<b>{message.text} Malayalam Dubbed Full Movie @HollywoodMalayalamMovieBot.mkv</b>", callback_data="mission")
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
➖➖➖➖➖➖➖➖➖➖

300
2012
Agent Cody Banks
Avengers Infinity War
Anaconda
Anacondas: The Hunt for the Blood Orchid Anacondas: Trail of Blood
Ben-Hur (1959)
Ben-Hur 2016
Black Widow
Captain Phillips
CZ12 Chinese Zodiac
Die Another Day
Die Hard
Django Unchained
Doctor Strange in the Multiverse of Madness
Exodus Gods and Kings
Fantastic Four
Godzilla
Ghost Rider
Gorgeous
Hollow Man
Home Alone 2: Lost in New York
Hotel Transylvania
Ice Age
Jack the Giant Slayer
Jumanji
Jumanji: Welcome to the Jungle
Jumanji: The Next Level 
Jurassic Park
Jurassic World Dominion
King Kong
Man of Steel
Men in Black
Men in Black 2
Men in Black International
Monster House
Night at the Museum
Pacific Rim
Passion of the Christ
Spider-Man
Spider-Man 2
Spider-Man 3
Spider-Man: Homecoming
Spider-Man: Far From Home
Spider-Man: No Way Home
Stuart Little 2
Stuart Little 3: Call of the Wild
The Adventures of Tintin: The Secret of the Unicorn
The Amazing Spider-Man
The Amazing Spider-Man 2
The Angry Birds
The Angry Birds 2
The Conjuring
The Da Vinci Code
The Hangover
The Incredible Hulk
The Matrix
The Mummy Rebirth
The Smurfs
The Smurfs 2
Titanic
Uncharted
Van Helsing
Venom
Venom: Let there be Carnage

Note:- You can only request 2 Movies in a week..!"""
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
