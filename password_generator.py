from wonderwords import RandomWord # Make sure to have wonderworlds library downloaded
import random, string
alphanumeric_list = list(string.ascii_letters + string.digits) # Combines the Ascii letters and string digits for an alphanumeric list.

def generate_password(length, type): # A function with diverse types of passwords.
    password = [] 
    if type.lower() == 'alphanumeric': # ex. zoFSmB
      for _ in range(length):
        password.append(str(random.choice(alphanumeric_list))) 
      return "".join(password)

    elif type.lower() == 'passphrase': # ex. MOTIVE-COUNCILMAN-PREDECESSOR-BURRITO-AMOUNT-AFTERSHOCK
      for _ in range(length):
        r = RandomWord()
        word = r.word().upper()
        password.append(word)
      return "-".join(password)

    elif type.lower() == 'pin': # ex. 266381
      for _ in range(length):
        password.append(str(random.randint(1,9)))
      return "".join(password)
    else:
      raise ValueError(f"Password type '{type}' not found.")
