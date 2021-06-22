from vector2 import Vector2
import discord
from random import randint

class Game:
  def __init__(self, game_size, player_position, goal):
    self.game_size = game_size
    self.player_position = player_position
    self.goal = goal

  def new_level(self):
    self.game_size = Vector2(randint(2,10),randint(2,6))
    self.player_position = Vector2(randint(0,self.game_size.x - 1),randint(0,self.game_size.y - 1))
    
    self.goal = Vector2(randint(0,self.game_size.x - 1),randint(0,self.game_size.y - 1))

  def update_state(self, user_input): #0 up, 1 right, 2 down, 3 left
    new_pos = Vector2(self.player_position.x, self.player_position.y)
    if user_input == 0:
      new_pos.y -= 1
    if user_input == 1:
      new_pos.x += 1
    if user_input == 2:
      new_pos.y += 1
    if user_input == 3:
      new_pos.x -= 1

    if new_pos.x < 0 or new_pos.y < 0:
      return False
    if new_pos.x >= self.game_size.x or new_pos.y >= self.game_size.y:
      return False
    
    self.player_position = new_pos
    return True

  def get_board(self):
    if self.player_position.x == self.goal.x and self.player_position.y == self.goal.y:
      self.new_level()

    board = []
    for y in range(self.game_size.y):
      row = []
      for x in range(self.game_size.x):
        row.append('x')
      board.append(row)
    player_row = board[self.player_position.y]
    player_row[self.player_position.x] = 'p'

    goal_row = board[self.goal.y]
    goal_row[self.goal.x] = 'g'

    board_string = ""
    for y in range(self.game_size.y):
      current_row = board[y]
      for x in range(self.game_size.x):
        board_string += current_row[x] + ' '
      board_string += '\n'

    return board_string
