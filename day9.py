import re

input = '412 players; last marble is worth 71646 points'
examples = [
  ('9 players; last marble is worth 25 points', 32),
  ('10 players; last marble is worth 1618 points', 8317),
  ('13 players; last marble is worth 7999 points', 146373),
  ('17 players; last marble is worth 1104 points', 2764),
  ('21 players; last marble is worth 6111 points', 54718),
  ('30 players; last marble is worth 5807 points', 37305)
]


# step 1


def play_game(players, max_value):
  player, point, index, marbles, score = 0, 0, 0, [0], [0 for i in range(players)]

  while point < max_value:

    if point % 100000 == 0:
      print('loop', point)

    point += 1
    player = player % players + 1

    if point % 23 == 0:
      index = (index-8) % len(marbles) + 1
      score[player-1] += point 
      score[player-1] += marbles.pop(index)
    else:
      index = (index+1) % len(marbles) + 1
      marbles.insert(index, point)
  
  return score


for s in examples:
  data = list(map(int, re.findall(r'\d+', s[0]))) 
  scores = play_game(data[0], data[1])
  print('score', data[0], data[1], sorted(scores).pop())

data = list(map(int, re.findall(r'\d+', input))) 
scores = play_game(data[0], data[1])
print('score', data[0], data[1], sorted(scores).pop())

data = list(map(int, re.findall(r'\d+', input))) 
scores = play_game(data[0], data[1] * 100)
print('score', data[0], data[1] * 100, sorted(scores).pop())