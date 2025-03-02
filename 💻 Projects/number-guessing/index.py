import random

print("Welcome to the game!\nYou have 5 attempts to guess the number between 50 and 100.")

number_to_guess = random.randint(50, 100)

chances = 5
guess_counter = 0

while guess_counter < chances:
    guess_counter += 1
    try:
        my_guess = int(input("Enter your guess: "))
    except ValueError:
        print("Invalid input! Please enter a number.")
        guess_counter -= 1
        continue  

    if my_guess == number_to_guess:
        print(f"Congratulations! The number was {number_to_guess} and you found it in {guess_counter} attempts.")
        break
    elif my_guess < number_to_guess:
        print("Your guess is too low! Try again.")
    elif my_guess > number_to_guess:
        print("Your guess is too high! Try again.")

    if guess_counter == chances: 
        print(f"Oops! You've used all your attempts. The number was {number_to_guess}. Better luck next time!")