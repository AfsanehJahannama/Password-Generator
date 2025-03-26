import random
import string

t = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.sample(t+t, 8))
print(password)