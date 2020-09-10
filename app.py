import random


guessedNo = int(input("guess a number between 1 - 9 : "))
no = random.randint(1, 9)
if guessedNo == no:
    print('yay!! you guessed the correct no. {}'.format(guessedNo))
else:
    print('oh no!! the no. was {}'.format(no))
