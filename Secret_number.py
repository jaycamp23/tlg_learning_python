# random number guessing game

import random

num = random.randint(1, 100)
print('find the secret number')


guess = 0
while guess != num:
    guess = int(input('guess between 1,100:'))

    if guess == num:
        print('correct')
        print('congrats')
        break

    elif guess < num:
        print('too low, try again')
    elif guess > num:
        print('to high,try again')

