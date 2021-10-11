# Level Three
# In level three, the computer's guesses are optimized to refine the range on the guesses based on whether they are too high or too low. Print how many guesses it takes the computer before it correctly guesses the number.

from random import randint


# def computer_guess():
#     input("What's your number?")
#     low = 1
#     high = 10
#     feedback = ""
#     computer_guess = 0
#     while feedback != 'c':
#         if low != high:
#             guess = randint(low, high)
#             computer_guess += 1
#         else:
#             guess = low
#         feedback = input(
#             f'is{guess} too high(H), too low (L), or correct (C)?')
#         if feedback == "h":
#             high = guess - 1
#         elif feedback == "l":
#             low = guess + 1
#     print(f"Yay the computer guessed correct in {computer_guess} guesses ")


# computer_guess(10)


def play():

    random_number = int(
        input("Type a number between 1 and 100 for the computer to guess: "))
    counter = 0

    low_num = 1
    high_num = 100

    while True:
        # https://docs.python.org/3/library/stdtypes.html?highlight=integer%20division#numeric-types-int-float-complex
        comp_guess = (low_num + high_num) // 2
        print("The computer guessed: ", comp_guess)

        if comp_guess > random_number:
            high_num = comp_guess - 1
        elif comp_guess < random_number:
            low_num = comp_guess + 1
        elif comp_guess == random_number:
            print("Computer guessed your number in {} tries".format(counter))
            break


play()
