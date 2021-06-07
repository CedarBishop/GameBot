import os
import discord
from commands import *
import random
from replit import db
from keep_alive import keep_alive
import utils
from random import seed
from random import randint

seed(1)

last_game_state_id = 0

client = discord.Client()

@client.event
async def on_ready():
  print("We have logged in as {0.user}".format(client))

@client.event
async def on_message(message):
  msg = message.content
  if message.author == client.user:
    if msg.endswith('move?'):
      await controls(message, client)
    elif msg.startswith('Guess'):
      await guesses(message, client)
  else:

    if msg.startswith('!play'):
      global last_game_state_id
      last_game_state_id = message.id
      await play(message, client)

    if msg.startswith('!help'):
      await help(message, client)

    if msg.startswith('!guess'):
      await guess(message, client)

@client.event
async def on_reaction_add(reaction, user):
  if user == client.user:
    #print("Failed because user is bot")
    return

  if reaction.message.author != client.user:
    #print("Failed because the message wasnt the message created by this bot")
    return

  #if reaction.message.id == last_game_state_id:
    #print("Failed because the message reacted to wasnt the game state message")
    #return

  if reaction.message.content.endswith('move?'):
    if reaction.emoji == utils.up_arrow_emoji:
      print("up")
    elif reaction.emoji == utils.down_arrow_emoji:
      print("down")
    elif reaction.emoji == utils.left_arrow_emoji:
      print("left")
    elif reaction.emoji == utils.right_arrow_emoji:
      print("right")
    await update_game(reaction.message.channel, """-------\n|-------|""")
  
  elif reaction.message.content.startswith('Guess'):
    guess = 0
    answer = randint(0, 10)
    print(answer)
    if reaction.emoji == utils.one_emoji:
      guess = 1
    elif reaction.emoji == utils.two_emoji:
      guess = 2
    elif reaction.emoji == utils.three_emoji:
      guess = 3
    elif reaction.emoji == utils.four_emoji:
      guess = 4
    elif reaction.emoji == utils.five_emoji:
      guess = 5

    if guess == answer:
      await reaction.message.channel.send("Ding ding ding correct it was {0}.".format(answer))
    else:
      await reaction.message.channel.send("Incorrect, the correct answer was {0}.".format(answer))


keep_alive()

my_secret = os.environ['TOKEN']
client.run(my_secret)