from wonderwords import RandomWord
import random, string #inserts the library
alphanumeric_list = list(string.ascii_letters + string.digits)

def generate_password(length, type): #types alphanumberic, passphrase,  PINs
    password = [] 
    if type.lower() == 'alphanumeric':
      for _ in range(length):
        password.append(str(random.choice(alphanumeric_list))) 
      return "".join(password)

    elif type.lower() == 'passphrase':
      for _ in range(length):
        r = RandomWord()
        word = r.word().upper()
        password.append(word)
      return "-".join(password)

    elif type.lower() == 'pin':
      for _ in range(length):
        password.append(str(random.randint(1,9)))
      return "".join(password)

password = generate_password(6, 'pin') # amount of digits, type of password
print(f"Password: {password}")
