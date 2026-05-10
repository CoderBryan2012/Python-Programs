import random, time

money = 100
rolls = 0

symbols = ["🍒", "🍋", "🔔", "🍫", "7️⃣"]
print("Welcome to the Casino!")
print("There is a slot machine in front of you.")
while money > 9:
    print("You have $", money)
    time.sleep(1)
    gamble = input("Do you want to gamble? ($10) ")
    if gamble.lower() == "yes" or gamble.lower() == "y":
        if money >= 10:
            money -= 10
            rolls += 1
            print("\n")
            for i in range(1, 4):
                print(f"Rolling... {i}")
                time.sleep(0.5)
            result = [random.choice(symbols) for _ in range(3)]
            print("You got: ", result)
            if result == ["7️⃣", "7️⃣", "7️⃣"]:
                print("Jackpot! You win $1,000,000!")
                money += 1000000
            elif result[0] == result[1] == result[2]:
                time.sleep(0.5)
                print("Congratulations! You win $500!")
                money += 500
            elif result[0] == result[1] or result[1] == result[2] or result[0] == result[2] or result[0] == result[1] == result[2]:
                time.sleep(0.5)
                print("Congratulations! You win $20!")
                money += 20
    elif gamble.lower() == "no" or gamble.lower() == "n":
        print("Okay, maybe next time!")
        break
        
    else:
        print("Please enter 'yes' or 'no'.")
print("Game over! You have $", money)
print(f"Your rolled {rolls} times.")
