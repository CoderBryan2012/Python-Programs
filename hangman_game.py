import random

number = random.randint(1,10)

rope = "------"
rope2 = "     |"
head = "    😨"
body = "     |"
legs = "    / /"

def play_game():
    won = False
    print("Welcome to the Hangman Game! You have 3 guesses to save the man from being hanged!")
    print("The number is between 1 and 10. Good luck!")

    for remaining in range(3, 0, -1):
        while True:
            try:
                guess = int(input("Choose your number: "))
            except ValueError:
                print("Please enter a valid number.")
                continue
            if not 1 <= guess <= 10:
                print("Please enter a number between 1 and 10.")
                continue
            break

        if guess == number:
            won = True
            break
        else:
            print(f"\nWrong guess! You have {str(remaining - 1)} guess{'es' if remaining - 1 != 1 else ''} left.")
            print(rope)
            print(rope2)
            if remaining == 2:
                print(head)
            elif remaining == 1:
                print(head)
                print(body)

    if won:
        print(f"You saved him with {remaining} guesses to spare!")
    else:
        print(legs)
        print(f"You lost! The correct number was {number}!")

if __name__ == "__main__":
    play_game()
