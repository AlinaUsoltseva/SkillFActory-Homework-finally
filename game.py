"""Guess the number game"""

import numpy as np

number = np.random.randint(1, 101) # Generating numbers from 1 to 101

# Number of attempts

count = 0

while True:
    count += 1
    predict_number = int(input("Guess number from 1 to 100 "))
    
    if predict_number > number:
        print("The number must be less")
        
    elif predict_number < number:
        print("The number must be greater")
        
    else:
        print(f"You guessed the number! The number is {number}, in {count} attempts")
        break # The end of game
    