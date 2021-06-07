import os
import discord
from commands import *
import random
from replit import db
from keep_alive import keep_alive


client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('!play'):
    await play(message, client)


keep_alive()

my_secret = os.environ['TOKEN']
client.run(my_secret)