import random
user_object = input("What is your object? ")
exaggeration = input("Would you like your excuse to be normal or exaggerated? ")

normal_actions = ["my Mom took my", "I lost my", "somebody stole my", "I can't find my", "I broke my",]
exaggerated_actions = ["my dog ate my", "aliens abducted my", "I shot a bazooka on my", "I fought my"]

if exaggeration == "normal":
   print(f"I can't believe this, {random.choice(normal_actions)} {user_object}!")
elif exaggeration == "exaggerated":
   print(f"Bro no way, {random.choice(exaggerated_actions)} {user_object}!")
else:
   print("Invalid choice.")
   print("Run the game to have another go.")
quit()
