import random
#variables
game = None
guess = None
guesses = 3
print("Welcome to the Hangman Game! You have 3 guesses to save the man from being hanged!")
print("The number is between 1 and 10. Good luck!")
number = random.randint(1,10)

#body
rope = "------"
rope2 = "     |"
head = "    😨"
body = "     |"
legs = "    / /"

#game

while guesses != 0:
    try:
        guess = int(input("Choose your number: "))
    except ValueError:
        print("Please enter a valid number.")
        continue
    if guess == number:
        game = "win"
        break
    else:
        print(f"\nWrong guess! You have {str(guesses - 1)} guess{'es' if guesses - 1 != 1 else ''} left.")
        print(rope)
        print(rope2)
        if guesses == 2:
            print(head)
        elif guesses == 1:
            print(head)
            print(body)
        guesses -= 1

if game == "win":
    print(f"You saved him with {guesses} guesses to spare!")
else:
    print(legs)
    print(f"You lost! The correct number was {number}!")
