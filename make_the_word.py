import random

def word_giver(words):
    points = 0
    for i in range(words):#starts a loop
        word_requirement = random.randint(3,6) #assigns a random amount of letters
        print(f"Points: {points}")
        print(f"You need {word_requirement} letters.")
        word = input("Your word: ")
        if len(word) == word_requirement: #if they get the correct word
            points =+ 1 #adds a point
            print("Correct!")
            print(f"+1 Point!")
        else:
            print("Incorrect.")
    print()
    print("Result:")
    print(f"{points}/{words}")
    print(f"Score: {points/words}%") #final score
word_giver(3) #amount of words
