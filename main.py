from pyrogram import Client, filters

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

print("Bot Started")
HKZ.run()
