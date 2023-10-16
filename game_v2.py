"""The computer makes its own guess and guesses the number itself"""

import numpy as np

def random_predict(number:int = 1) -> int:
    """Random makes a number

    Args:
        number (int, optional): makes a number. Defaults to 1.

    Returns:
        int: count
    """
    
    count = 0
    
    while True:
        count += 1
        predict_number = np.random.randint(1, 101)
        if number == predict_number:
            break
           
    return(count)

def score_game(random_predict) -> int:
    """How many guesses on average

    Args:
        random_predict (_type_): guessing function

    Returns:
        int: average number of attempts
    """
    
    count_ls = []
    np.random.seed(1)
    random_array = np.random.randint(1, 101, size = (1000))
    for number in random_array:
        count_ls.append(random_predict(number))
        
    score = int(np.mean(count_ls))
    
    print(f'Your algorithm guesses the number on average for: {score} attempts')
    return(score)

if __name__ == '__main__':
    score_game(random_predict)

lsit = [1, 2, 3]