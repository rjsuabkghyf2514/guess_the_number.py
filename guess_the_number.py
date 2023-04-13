import random

def play_game():
    """Main function for playing the game"""
    print("Welcome to the Guess the Number game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have 10 guesses to get it right.")
    print("Let's begin!\n")

    number_to_guess = random.randint(1, 100)
    guesses_left = 10

    while guesses_left > 0:
        guess = int(input(f"You have {guesses_left} guesses left. What's your guess? "))
        guesses_left -= 1

        if guess == number_to_guess:
            print("Congratulations! You guessed the number!")
            return
        elif guess < number_to_guess:
            print("Too low. Guess higher.\n")
        else:
            print("Too high. Guess lower.\n")

    print(f"Sorry, you ran out of guesses. The number was {number_to_guess}. Better luck next time!")

play_game()
