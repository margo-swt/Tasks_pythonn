import random
import string


def generate_password():
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    numbers = string.digits
    special_chars = string.punctuation

    all_chars = lowercase_letters + uppercase_letters + numbers + special_chars

    password = ''

    for i in range(8):
        password += random.choice(all_chars)


    return password


password = generate_password()
print(password)
