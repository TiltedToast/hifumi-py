from datetime import datetime as dt
from importlib import reload
import discord
import main
import tools

bot = discord.Client()
start_time = tools.current_time()

file = open(r"files/token.txt", "r")
TOKEN = file.readline()
file.close()


@bot.event
async def on_message(message):
    restart_shortcut = "hr~~~"
    if message.content.startswith(restart_shortcut):
        if message.author.id == main.BOT_OWNER:
            if main.vote_running:
                await message.channel.send("There is a voting running, close it before reloading!")
                return
            else:
                try:
                    reload(main)
                    await main.reload_modules()
                    main.init_vars(bot)
                    msg = "Reload successful!"
                except Exception as e:
                    msg = f"Reload failed!\n{e}"
                print(msg)
                await message.channel.send(msg)
        else:
            await message.channel.send("Insufficient Permissions!")
    else:
        await main.message_in(message)


@bot.event
async def on_ready():
    time = dt.utcnow().strftime("%d/%m/%Y %H:%M:%S")
    done_loading_time = tools.current_time()

    print(f'Started up in {done_loading_time - start_time} seconds on {time} UTC')
    print('Logged in as:')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

    channel = bot.get_channel(655484804405657642)
    await channel.send(f"Logged in as:\n{bot.user.name}\nTime: {time}\n"
                       f"--------------------------")
    game = discord.Game("with best girl Annie!")
    main.init_vars(bot)
    await bot.change_presence(activity=game)

bot.run(TOKEN)
