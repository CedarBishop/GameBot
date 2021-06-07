import discord
from discord.utils import get
import requests
import json
from utils import *



async def play(message, client):
  await message.channel.send('Hi {0.author}! Let\'s play a game.'.format(message)) 
  await update_game(message.channel, """-------\n|-------|""")

async def help(message, client):
  await message.channel.send('The commands I have are:\n1. !play\n2. !guess\n3. !help')

async def guess(message, client):
  await message.channel.send('Guess a number between 1 and 5?')

async def controls(message, client):
  await message.add_reaction(up_arrow_emoji)
  await message.add_reaction(down_arrow_emoji)
  await message.add_reaction(left_arrow_emoji)
  await message.add_reaction(right_arrow_emoji)

async def guesses(message, client):
  await message.add_reaction(one_emoji)
  await message.add_reaction(two_emoji)
  await message.add_reaction(three_emoji)
  await message.add_reaction(four_emoji)
  await message.add_reaction(five_emoji)

async def update_game(channel, game_state):
  await channel.send(game_state + '\nWhat is your next move?')