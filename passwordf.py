import random
import string

def password_generator(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

password_length = int(input("Enter the desired password length: "))
print(password_generator(password_length))