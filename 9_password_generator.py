import random

def generate(length):
    # Define the character sets
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    digits = '0123456789'
    special = '!@#$%^&*()-_=+[]{}|;:,.<>?/'

    all = lowercase + uppercase + digits + special
    password = random.sample(all, length)
    
    return "".join(password)

print("5 Generated Passwords of length 15:")
for i in range(5):
    print(generate(15))