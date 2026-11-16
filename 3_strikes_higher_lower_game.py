import random

print("Welcome to the 3-Strikes Higher/Lower Game, Bella!")
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

while lower_bound >= upper_bound:
    print("The lower bound must be less than the upper bound.")
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))

secret_number = random.randint(lower_bound, upper_bound)
strikes = 0
max_strikes = 3
won = False

while strikes < max_strikes and not won:
    guess = int(input(f"\nGuess a number between {lower_bound} and {upper_bound}: "))

    if guess == secret_number:
        won = True
    else:
        strikes += 1
        if guess < secret_number:
            print(f"Strike {strikes}! Nope, too low.")
        else:
            print(f"Strike {strikes}! Nope, too high.")

if won:
    print("You got it!")
else:
    print(f"Strike 3 — you're out! The number was {secret_number}.")