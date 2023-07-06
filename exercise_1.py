import random
import string

def generate_random_string(length):
    letters = string.ascii_letters + string.digits
    random_string = ''.join(random.choice(letters) for _ in range(length))
    return random_string

def generate_random_email():
    username_length = random.randint(10, 20)
    domain = "makingscience.com"

    username = generate_random_string(username_length)
    email = "test" + username + "@" + domain
    return email

for i in range(10):
    random_email = generate_random_email()
    print(random_email)






