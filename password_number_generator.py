import random #inserts the library

def generate_password(letters): 
    password = [] 

    for _ in range(letters):
        password.append(random.randint(1,9)) #adds a random number to the list
    return password #=

password = generate_password(6) #amount of digits
print(f"Password: {password}")
