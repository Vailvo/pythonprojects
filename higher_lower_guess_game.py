import random

print("Welcome to the higher/lower game, Bella!")
lower_bound = int(input("Enter the lower bound: "))
upper_bound = int(input("Enter the upper bound: "))

while lower_bound >= upper_bound:
    print("The lower bound must be less than the upper bound.")
    lower_bound = int(input("Enter the lower bound: "))
    upper_bound = int(input("Enter the upper bound: "))

secret_number = random.randint(lower_bound, upper_bound)
guess = int(input(f"\nGreat, now guess a number between {lower_bound} and {upper_bound}: "))

while guess != secret_number:
    if guess < secret_number:
        print("Nope, too low.")
    else:
        print("Nope, too high.")
    
    guess = int(input("\nGuess another number: "))

print("You got it!")