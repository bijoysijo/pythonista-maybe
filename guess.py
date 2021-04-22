import random

secret_number = random.randint(1,20)

for guesses_taken in range(1,7):
  print("I have guessed a number, what is it?")
  user_guess = int(input())

  if user_guess < secret_number:
    print("You guessed too low.")
  elif user_guess > secret_number:
    print("You guessed too high.")
  else:
    break

if user_guess == secret_number:
  print(f"Good job! You guessed my number in {guesses_taken} guesses!")
else:
  print('Nope. The number I was thinking of was ' + str(secret_number))
