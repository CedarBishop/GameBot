import discord
from discord.utils import get
import requests
import json

async def play(message, client):
  await message.channel.send('Hello {0.author}!'.format(message))
  emoji = '\N{THUMBS UP SIGN}'
  await message.add_reaction(emoji)

async def help(message, client):
  await message