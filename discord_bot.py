# Austin Wong-Parker
# 12 - 27 - 2019
# CLA Major Discord Bot

# Starting information from https://realpython.com/how-to-make-a-discord-bot-python/#interacting-with-discord-apis

#! python3.6

import os
import discord
from dotenv import load_dotenv              # This library loads environment variables from a .env file into the shell's environment variables

load_dotenv()
token = os.getenv('DISCORD_TOKEN')          # Connects specific Discord Token from .env file
guild = os.getenv('DISCORD_GUILD')          # Connects specific Discord Guild from .env file

client = discord.Client()                   # Client is an object that will represent connection to Discord.

@client.event
async def on_ready():                       # Event handler; called when client is ready for stuff to happen.
    for guild in client.guilds:             # Ensure this is the correct server.
        if guild.name == guild:
            break
    print(f'{client.user} has connected to Discord!')
    print(f'{client.user} has connected to {guild.name} (id: {guild.id})')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if client.user.mentioned_in(message) and message.mention_everyone is False:
        await message.channel.send("Hello, please choose which response you want: \n"
              "1. The friendly opinion for CLA majors. \n"
              "2. The mean opinion for CLA majors. \n"
        )

    if message.content == '1':
        f = open('friendly_cla.txt', 'r', encoding="utf8")        # Open and read friendly_cla.txt
        file_contents = f.read()
        #print(file_contents)
        await message.channel.send(file_contents)
        f.close()

    if message.content == '2':
        m = open('mean_cla.txt', 'r', encoding="utf8")            # Open and read mean_cla.txt
        file_contents1 = m.read()
        m = open('mean_cla_2.txt', 'r', encoding="utf8")
        file_contents2 = m.read()
        m = open('mean_cla_3.txt', 'r', encoding="utf8")
        file_contents3 = m.read()
        #print(file_contents)
        await message.channel.send(file_contents1)
        await message.channel.send(file_contents2)
        await message.channel.send(file_contents3)
        m.close()

client.run(token)
