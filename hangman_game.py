import random
#variables
game = None
guess = None
guesses = 3
number = random.randint(1,10)

#body
rope = "------"
rope2 = "     |"
head = "    😨"
body = "     |"
legs = "    / /"

#game

while guesses != 0:
    guess = int(input("Choose your number: "))
    if guess == number:
        game = "win"
        break
    else:
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
