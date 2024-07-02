import random
import string


def password(n, p):
  if p == 'hard' or 'Hard':
    pass1 = ""
    ch = string.ascii_letters + string.digits + '!@#$%&'
    pass1 = ''.join(random.choice(ch) for _ in range(n))
    return pass1
  elif p == 'medium' or 'Medium':
    pass1 = ""
    ch = string.ascii_letters + string.digits
    pass1 = ''.join(random.choice(ch) for _ in range(n))
    return pass1
  elif p == 'easy' or 'Easy':
    pass1 = ""
    ch = string.ascii_letters
    pass1 = ''.join(random.choice(ch) for _ in range(n))
    return pass1
  else:
    return 'Invalid Input'


length = int(input("Enter the length of the password to be generated"))
password_intensity = input("Enter the password intensity")
print(password(length, password_intensity))
