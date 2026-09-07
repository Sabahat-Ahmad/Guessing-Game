import random  # needed to generate a random secret number

# ---------------- Single-line comment ----------------
# Different data types used in the program
low = 1                     # int
high = 100                  # int
max_attempts = 7            # int
player_name = ""            # string (str)
play_again = True           # boolean (bool)
attempt_count = 0           # int
guess = 0                   # int (will hold user's guess)

"""
Multi-line comment:
The secret number is randomly generated between 'low' and 'high'
using the random module. The user then tries to guess it within
a limited number of attempts.
"""

print("===== WELCOME TO THE NUMBER GUESSING GAME =====")
player_name = input("Enter your name: ")
print("Hello,", player_name, "! Let's play a guessing game.")

# ---------------- Outer while loop: allows multiple games ----------------
while play_again:

    secret_number = random.randint(low, high)  # generate secret number
    attempt_count = 0
    guessed_correctly = False

    print("\nI have selected a number between", low, "and", high)
    print("You have", max_attempts, "attempts. Type 'quit' anytime to exit.")

    # ---------------- Nested for loop ----------------
    # Just a small visual countdown display before the game starts,
    # demonstrating nested for loops.
    for i in range(1, 3):
        for j in range(1, 3):
            print("Get ready" + "." * (i + j))

    # ---------------- for loop controlling attempts ----------------
    for attempt in range(1, max_attempts + 1):

        attempt_count = attempt  # arithmetic operator (=) / assignment

        user_input = input("\nAttempt " + str(attempt) + " - Enter your guess: ")

        # Allow the user to quit using exit() function
        if user_input == "quit":
            print("Thanks for playing,", player_name, "! Goodbye.")
            exit()  # terminates the program immediately

        # Basic validation using pass statement
        if user_input == "":
            pass  # do nothing special, just fall through to eval error handling
        # eval() function: evaluates the input expression as a number
        try:
            guess = eval(user_input)
        except:
            print("Invalid input! Please enter a valid number.")
            continue  # continue statement: skip rest of loop, ask again

        # Ensure guess is an integer type
        if type(guess) != int:
            print("Please enter a whole number (integer).")
            continue

        # ---------------- Comparison & Logical operators ----------------
        if guess < low or guess > high:
            print("Please guess a number within the valid range.")
            continue

        # ---------------- Bitwise operator demonstration ----------------
        # Check if the guess is even or odd using bitwise AND
        if (guess & 1) == 0:
            parity = "even"
        else:
            parity = "odd"
        print("(Hint: your guess is an", parity, "number)")

        # ---------------- Nested if / if-elif-else ----------------
        if guess == secret_number:
            guessed_correctly = True
            break  # break statement: exit the for loop, guess is correct
        else:
            if guess > secret_number:
                difference = guess - secret_number  # arithmetic operator
                if difference > 20:
                    print("Too High! And quite far off.")
                else:
                    print("Too High! But you're getting close.")
            elif guess < secret_number:
                difference = secret_number - guess
                if difference > 20:
                    print("Too Low! And quite far off.")
                else:
                    print("Too Low! But you're getting close.")

        # Logical operator: warn when attempts are running out
        remaining = max_attempts - attempt_count
        if remaining <= 2 and remaining > 0:
            print("Warning: only", remaining, "attempt(s) left!")

    # ---------------- if-else after the for loop ----------------
    if guessed_correctly:
        print("\nCongratulations,", player_name, "! You guessed the number",
              secret_number, "in", attempt_count, "attempts.")
    else:
        print("\nOut of attempts! The secret number was:", secret_number)

    # ---------------- Ask to play again ----------------
    choice = input("\nDo you want to play again? (yes/no): ")

    # while loop for validating yes/no input
    while choice != "yes" and choice != "no":
        choice = input("Please type 'yes' or 'no': ")

    if choice == "yes":
        play_again = True
    else:
        play_again = False

print("\nThank you for playing,", player_name, "! See you next time.")
exit()  # explicit program termination