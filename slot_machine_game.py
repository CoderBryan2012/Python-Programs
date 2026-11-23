import random, time

money, rolls = 100, 0
symbols = ["🍒", "🍋", "🔔", "🍫", "7️⃣"]

def play_game():
  global money, rolls
  print("Welcome to the Casino!")
  print("There is a slot machine in front of you.")
  while money > 9: # The game continues until the player quits or runs out of money.
      print(f"You have ${money}.")
      time.sleep(1)
      gamble = input("Do you want to gamble? ($10) ") # The player chooses if they want to start or continue gambling.
      if gamble.lower() == "yes":
          if money >= 10:
              money -= 10
              rolls += 1
              print("\n")
              for i in range(1, 4):
                  print(f"Rolling... {i}")
                  time.sleep(random.randint(1,10) / 10)
              result = [random.choice(symbols) for _ in range(3)]
              print("You got: ", result)

              if result == ["7️⃣", "7️⃣", "7️⃣"]: # Jackpot winner
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

      elif gamble.lower() == "no": # Quit Session
          print("Okay, maybe next time!")
          break
          
      else:
          print("Please enter 'yes' or 'no'.")

  if rolls > 0: # Outcome algorithm, only runs when the player gambles at least once. 
    outcome = "You went home feeling proud." if money >= 10000 else "You went home happy." if money >= 1000 else "You feel great." if money >= 200 else "You feel fine." if money >= 100 else "You feel unlucky." 
    print(f"{outcome} You have ${money}.", end=' ')
    print(f"You rolled {rolls} time{"s" if rolls > 1 else ""}.")
if __name__ == "__main__":
    play_game()
