import secrets
import string

def password_generator():
    how_many=int(input("Kolko hesiel treba veducko?: "))
    for i in range(0,how_many):
        letters = string.ascii_letters
        digits = string.digits
        special_chars = string.punctuation  
        alphabet = letters + digits + special_chars
        pwd_length = 12
        pwd = ''
        for i in range(pwd_length):
            pwd += ''.join(secrets.choice(alphabet))

        print(pwd)

password_generator()

