from random import randint
random_number = randint(1,100)

print("Welcome to the guessing game. Your job is to guess a number between 1 and 100.\n Whether you are close or far, I will let you know.")

guess = 0
list_of_guesses = []
while True:
  guess = int(input('Enter your guess here: '))
  list_of_guesses.append(guess)
  if guess == random_number:
    print(f'{guess} is it! You guessed it in {len(list_of_guesses)} guesses')
    break
  elif len(list_of_guesses) == 1:
    if abs(random_number - guess) < 10:
      print('WARM!')
    else:
      print('COLD')
  else:
    if abs(list_of_guesses[-2] - random_number) > abs(guess - random_number):
      print('WARMER!')
    elif abs(list_of_guesses[-2] - random_number) < abs(guess - random_number):
      print('COLDER')




