MONGODB_SETTINGS ={
    'db' : 'Application',
    'host' : 'localhost'
}

DEBUG = True # Turns on debugging features in Flask
BCRYPT_LOG_ROUNDS = 12 # Configuration for the Flask-Bcrypt extension
MAIL_FROM_EMAIL = "robert@example.com"

import random
import string
N = 26
string_values = ''.join(random.SystemRandom().choice(string.ascii_uppercase
                + string.digits +string.ascii_lowercase) for _ in range(N))

# print(string_values)
SECRET_KEY = string_values