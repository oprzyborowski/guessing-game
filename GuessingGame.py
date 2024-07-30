import random

print("Computer is going to pick a random number in range from 1 to 100.")
print("You have to guess the number!")

def number_checker(picked_number):
    if picked_number in range (1,101):
        return True
    else:
        print("Please guess a number from 1 to 100!")
        return False

random_number = random.randint(1,100)

guessing_game = True
while True:
    try:
        user_input = int(input("What is your guess? --> "))
    except ValueError:
        print("Invalid Input! Please guess a number from 1 to 100!")

    number_checker(user_input)

    if user_input > random_number:
        print("Your guess is too high!")
        continue
    elif user_input < random_number:
        print("Your guess is too low!")
        continue
    else:
        print("Congrats! You guessed the number!")
        break