import random

# Different data types
low = 1
high = 100
max_attempts = 7
player_name = ""
play_again = True

"""
The program generates a random secret number.
The player has 7 attempts to guess the number.
"""

print("===== NUMBER GUESSING GAME =====")
print()

player_name = input("Enter your name: ")
print()
print("Hello,", player_name, "! Let's play.")
print()

# Allows multiple games
while play_again:

    secret_number = random.randint(low, high)
    guessed_correctly = False

    print("I have selected a number between", low, "and", high)
    print("You have", max_attempts, "attempts.")
    print()

    print("Get ready")
    print()

    # Controls attempts
    for attempt in range(1, max_attempts + 1):

        user_input = input("Attempt " + str(attempt) +
                           " - Enter your guess: ")

        if user_input == "quit":
            print()
            print("Thanks for playing,", player_name, "!")
            exit()

        if user_input == "":
            pass

        guess = eval(user_input)

        if guess < low or guess > high:
            print("Please enter a number between 1 and 100.")
            print()
            continue

        if (guess & 1) == 0:
            print("Hint: Your guess is even.")
        else:
            print("Hint: Your guess is odd.")

        if guess == secret_number:
            guessed_correctly = True
            break

        elif guess > secret_number:
            difference = guess - secret_number

            if difference > 20:
                print("Too High! You are quite far off.")
            else:
                print("Too High! You are getting close.")

        else:
            difference = secret_number - guess

            if difference > 20:
                print("Too Low! You are quite far off.")
            else:
                print("Too Low! You are getting close.")

        remaining = max_attempts - attempt

        if remaining <= 2 and remaining > 0:
            print("Warning:", remaining, "attempt(s) left!")

        print()

    print()

    if guessed_correctly:
        print("Congratulations,", player_name, "!")
        print("You guessed the number in", attempt, "attempts.")
    else:
        print("Out of attempts!")
        print("The secret number was:", secret_number)

    print()

    choice = input("Do you want to play again? (yes/no): ")

    while choice != "yes" and choice != "no":
        choice = input("Please type 'yes' or 'no': ")

    print()

    if choice == "yes":
        play_again = True
    else:
        play_again = False

print()
print("Thank you for playing,", player_name, "!")
exit()