<<<<<<< HEAD
import random 
number = random.randint(1, 10) 
print("Guess a number between 1 and 10") 
guess = int(input()) 
if guess == number: 
 print("You win!") 
else: 
 print(f"Wrong! The number was {number}")

 while True: 
    # (paste existing code here) 
    print("Play again? (y/n)") 
    if input().lower() != 'y': 
        break
=======
import random
number = random.randint(1, 10)
print("Guess a number between 1 and 10")
guess = int(input())
if guess == number:
    print("You win!")
else:
    print(f"Wrong! The number was {number}")
>>>>>>> 561f7382de7d64718cccd7ee9bbeb2d2dbd12975
