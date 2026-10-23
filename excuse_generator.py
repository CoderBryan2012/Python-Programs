import random

normal_actions = ["my Mom took my", "I lost my", "somebody stole my", "I can't find my", "I broke my"]
exaggerated_actions = ["my dog ate my", "aliens abducted my", "I shot a bazooka on my", "I fought a bear for my"]
randomized_reactions = ["I can't believe this...", "Oh man.", "Are you serious?!", ]
while True:
  user_object = input("What is your object? ")
  exaggeration = input("Would you like your excuse to be normal, exaggerated or chaos? ")
  if not exaggeration or not user_object:
    print('Your object orexaggeration cannot be empty.')
    continue

  if exaggeration.lower() == "normal":
    print(f"{random.choice(randomized_reactions)} {random.choice(normal_actions).title()} {user_object}!")

  elif exaggeration.lower() == "exaggerated":
    print(f"{random.choice(randomized_reactions)} {random.choice(exaggerated_actions)} {user_object}!")
  elif exaggeration.lower() == "chaos":
    print(f"{random.choice(randomized_reactions)} {random.choice(exaggerated_actions)} {user_object} and {random.choice(normal_actions)} it!")
  else:
    print("Invalid choice.")
  quit_choice = input("\nDo you want to make another excuse? (yes/no) ")
  if quit_choice.lower() == "no" or quit_choice.lower().startswith('n'):
    break
