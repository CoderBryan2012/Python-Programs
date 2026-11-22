import random

def word_giver(words):
    points = 0
    for i in range(words): # Starts a loop that runs based on the number of words given.
        word_requirement = random.randint(3,6) # Assigns a random amount of letters for current word. 
        print(f"Points: {points}")
        print(f"You need {word_requirement} letters.")
        word = input("Your word: ").strip()
        if len(word) == word_requirement and world.isalpha(): # Gives the user a point if thw word meets the criteria. 
            points += 1
            print("Correct!")
            print(f"+1 Point!")
        else:
            print("Incorrect.")
    # Prints the user's final score.
    print()
    print("Result:")
    print(f"{points}/{words}")
    print(f"Score: {(points/words) * 100:.0f}%")
