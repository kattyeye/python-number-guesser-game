from random import randint

# Level One
# In level one, the computer generates a random number between 1 and 10 and the user has 3 guesses to pick the correct number. The computer will tell you if you are too high or too low.
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



