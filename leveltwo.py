# Level Two
# In level two, the game is reversed and the user picks a number and the computer then has 3 guesses to select the correct answer.

from random import randint

user_guess = int(input("Choose a number you want the computer to guess from  1-10: "))

number_of_guesses = 0
computer_guess = randint(1,10)

while number_of_guesses < 3 and 10 > user_guess > 1 and computer_guess != user_guess: #the computer has 3 chances to guess
    print("The computer's guess is: ", computer_guess)
    if computer_guess > user_guess:
        computer_guess = randint(1, computer_guess)
    elif computer_guess < user_guess:
        computer_guess = randint(computer_guess, computer_guess)
        number_of_guesses +=1
if computer_guess == user_guess and number_of_guesses < 3:
    print("The computer guessed your number")
    number_of_guesses +=1
elif number_of_guesses >= 10 and computer_guess != user_guess:
    print("The computer couldn't guess your number, well done.")












