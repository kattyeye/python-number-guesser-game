# Level Four
# In level four, give the user an option to play against the computer or to think of a number for the computer to guess.

from random import randint

i = input ("Enter the letter k for computer to play, enter the letter u to play against the computer: ")

if i == "k":
    print("let the games begin")
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


if i == "u":
    print("play!")
    x = randint(1,10)
number_of_guesses = 0

guess = None

while number_of_guesses < 3:
    print("guess a number between 1 and 10")
    guess = input()
    guess = int(guess)

    number_of_guesses += 1

    if guess < x:
        print("your guess is too LOW")
    if guess > x:
        print("your guess is too HIGH")
    if guess == x:
        break
if guess == x:
    number_of_guesses = str(number_of_guesses)
    print("Good job, you guessed in " + number_of_guesses)
if guess != x:
    x = str(x)
    print("Nope, the number I was thinking of was" + x)