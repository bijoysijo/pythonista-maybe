import random
import sys

#scoreboard
wins = 0
losses = 0
ties = 0

while True:
  print('%sWins, %sLose, %sTies'%(wins, losses, ties))
  while True:
    print("Enter your move: (r)ock, (p)aper,(s)cissor or (q)uit")
    playermove = input()
    if playermove == 'q':
      sys.exit()
    elif playermove == 'r' or playermove == 'p' or playermove == 's':
      break
    else:
      print("type one: r, p, s or q")

  if playermove == 'r':
    print("player chose rock")
  elif playermove == 'p':
    print("player chose paper")
  elif playermove == 's':
    print("player chose scissors")

  rand = random.randint(1,3)
  if rand == 1:
    computer_choice = 'r'
    print("computer chose rock")
  elif rand == 2:
    computer_choice = 'p'
    print("computer chose paper")
  elif rand == 3:
    computer_choice = 's'
    print("computer chose scissors")

  if playermove == computer_choice:
    print("It's a tie")
    ties = ties + 1
  elif playermove == 'r' and computer_choice == 'p':
    print("It's a win")
    wins = wins + 1
  elif playermove == 's' and computer_choice == 'r':
    print("It's a loss")
    losses = losses + 1
  elif playermove == 'p' and computer_choice == 's':
    print("It's a loss")
    losses = losses + 1
  elif playermove == 'p' and computer_choice == 'r':
    print("It's a win")
    wins = wins + 1
  elif playermove == 's' and computer_choice == 'p':
    print("It's a win")
    wins = wins + 1
  elif playermove == 'r' and computer_choice == 's':
    print("It's a win")
    wins = wins + 1






















