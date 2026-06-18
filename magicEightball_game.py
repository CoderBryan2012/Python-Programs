#magic eightball game
import random, time


affirmative_responses = [
   "It is certain",
   "It is decidedly so",
   "Without a doubt",
   "Yes definitely",
   "You may rely on it",
   "As I see it, yes",
   "Most likely",
   "Outlook good",
   "Yes",
   "Signs point to yes"
]

non_committal_responses = [
   "Reply hazy, try again",
   "Ask again later",
   "Better not tell you now",
   "Cannot predict now",
   "Concentrate and ask again"
]

negative_responses = [
   "Don't count on it",
   "My reply is no",
   "My sources say no",
   "Outlook not so good",
   "Very doubtful"
]

# A master list containing all 20 responses
all_responses = affirmative_responses + non_committal_responses + negative_responses

while True:
   user_input = input("Type a yes or no question: ")
   print(time.sleep(random.randint(1,10)))
   print(random.choice(all_responses))
