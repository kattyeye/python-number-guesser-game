# Level Three
# In level three, the computer's guesses are optimized to refine the range on the guesses based on whether they are too high or too low. Print how many guesses it takes the computer before it correctly guesses the number.

from random import randint

def computer_guess(x):
    low = 1
    high = x
    feedback =  ""
    computer_guess = 0;
    while feedback != 'c':
        if low != high:
            guess = randint(low, high)
            computer_guess += 1
        else:
            guess = low
        feedback = input(f'is{guess} too high(H), too low (L), or correct (C)?')
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"Yay the computer guessed correct in {computer_guess} guesses ")
computer_guess(10)