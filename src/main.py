import os
import discord
from os import path
from get_ts import get_ts
from lib import get_cookie
from lib import loop_check
from termcolor import colored
from get_ts import forward_saved

# =================================================
# ===            GO TO WORKING DIR              ===
# =================================================

os.chdir(os.environ.get("WORKING_DIR"))

# =================================================
# ===          TOKEN AND COOKIE PARSING         ===
# =================================================

if ((path.exists("./cookie.txt") and path.isfile('./cookie.txt')) == False):
    print(colored("cookie.txt not found, create and fill it with reservation_system cookie", "red"))
    quit()

if ((path.exists("./token.txt") and path.isfile('./token.txt')) == False):
    print(colored("token.txt not found, fill it with your discord bot token", "red"))
    quit()

f_token = open("token.txt", "r")
f_cookie = open("cookie.txt", "r")

TOKEN = f_token.readline()
COOKIE = f_cookie.readline()

# =================================================
# ===               BOT LAUNCH                  ===
# =================================================

client = discord.Client()

async def global_loop():
    await client.wait_until_ready()
    ts = get_ts();             # Get timestamps min and max to scrap
    cookie = get_cookie()
    channel = discord.utils.get(client.get_all_channels(), name='general')
    while (True):
        await loop_check(ts, cookie) # will send request to 42 if slots is avalaible
        msg = "🚨 @everyone La nouvelle semaine de reservation est arrivé ! 🚨"
        await channel.send(msg)
        ts = forward_saved(ts)

@client.event
async def on_ready():
    print(colored(f'{client.user} has connected to Discord!\n', 'green'))
    channel = discord.utils.get(client.get_all_channels(), name='general')
    msg = "🤖 I'm started and looking for new slots !"
    await channel.send(msg)

@client.event
async def on_message(message):
    if (message.content == "!alive"):
        msg = "🤖 Yes i'm alive and i'm waiting for slots !"
        await message.channel.send(msg)

print("starting srv")
client.loop.create_task(global_loop())
client.run("ODIzODcxOTQyODYzNzQ5MTYx.YFnIiQ.wAixlo8toJCVbF35dRb6ajdf8zE")

