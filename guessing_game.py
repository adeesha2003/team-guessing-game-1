<<<<<<< HEAD
import random 
number = random.randint(1, 100)
print("Guess a number between 1 and 100")
guess = int(input()) 
if guess == number: 
    print("You win!") 
else: 
=======
import random
number = random.randint(1, 10)
print("Guess a number between 1 and 10")
guess = int(input())
if guess == number:
    print("You win!")
else:
>>>>>>> 561f7382de7d64718cccd7ee9bbeb2d2dbd12975
    print(f"Wrong! The number was {number}")