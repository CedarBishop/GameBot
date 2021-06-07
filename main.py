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

  options = starter_encouragements
  if "encouragements" in db.keys():
    for enc in db["encouragements"]:
      options.append(enc)

  if msg.startswith('!greet'):
    await greet(message, client)


keep_alive()

my_secret = os.environ['TOKEN']
client.run(my_secret)