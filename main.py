import os
import discord
from commands import *
import random
from replit import db
from keep_alive import keep_alive
import utils
from random import seed
from random import randint
from vector2 import Vector2
from game import Game

seed(1)

last_game_state_id = 0

client = discord.Client()
games = {}

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
      games[message.author] = Game(Vector2(0,0), Vector2(0,0), Vector2(0,0))
      games[message.author].new_level()
      await play(message, client, games[message.author].get_board())

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
    user_input = 0
    if reaction.emoji == utils.up_arrow_emoji:
      user_input = 0
    elif reaction.emoji == utils.down_arrow_emoji:
      user_input = 2
    elif reaction.emoji == utils.left_arrow_emoji:
      user_input = 3
    elif reaction.emoji == utils.right_arrow_emoji:
      user_input = 1

    users = await reaction.users().flatten()
    users = users[0]
    if games[user].update_state(user_input):
      await update_game(reaction.message.channel, user.name, games[user].get_board())
    else:
      await reaction.message.channel.send('Cannot move in that direction.')
      await update_game(reaction.message.channel, user.name, games[user].get_board())

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