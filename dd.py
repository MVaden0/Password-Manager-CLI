import json
import base64
from math import ceil
from cryptography.fernet import Fernet


def process_password(
        password: str, 
        byte_count: int=32
    ) -> str:
    """
    Determines the number of bytes in a password and appends extra 'a'
    characters to the password string to make the password reach a set number
    of bytes when encoded.

    Parameters:
    password (str) - the password given by a user
    byte_count (int) - the number of bytes required for encoded output

    Returns:
    (str) the password with appended characters
    """

    # computing number of bytes in password once encoded
    _byte_count = ceil(len(password) / 3)

    # recursively append bytes until required byte count reached
    if _byte_count != byte_count / 4:
        _appended_char_password = password + 'a'

        return process_password(_appended_char_password, byte_count)
    
    return str(password)


def generate_key_from_password(
        password: str
    ) -> str:
    """
    Encodes a password in base64 format.

    Paramaters:
    password (str): password to be encoded

    Returns:
    (str) the base64 encoded password
    """

    _processed_password = process_password(password)
    _encoded_password = base64.urlsafe_b64encode(_processed_password.encode('ascii'))

    return _encoded_password

        



passsword = "x9mzyx9cu26hlpsw!"

print(process_password(passsword))
# 1 - 4
# 2 - 4
# 3 - 4
#4 - 8
# 5 - 8
# 6 - 8
# 7 - 12
# 8 - 12


message_bytes = passsword.encode('ascii')
base64_bytes = base64.b64encode(message_bytes)

base64_message = base64_bytes.decode('ascii')

print(len(generate_key_from_password(passsword)))
print(len(Fernet.generate_key()))
print(generate_key_from_password(passsword))
print(Fernet.generate_key())

fernet = Fernet(generate_key_from_password(passsword))
"""
# we will be encrypting the below string.
message = [
    {
        "application" : "PayPal"
    }
]
 
key = Fernet.generate_key()
 
# Instance the Fernet class with the key
 
fernet = Fernet(key)
 
# then use the Fernet class instance
# to encrypt the string string must
# be encoded to byte string before encryption
encMessage = fernet.encrypt(json.dumps(message).encode())
 
print("original string: ", message)
print("encrypted string: ", encMessage)
 
# decrypt the encrypted string with the
# Fernet instance of the key,
# that was used for encrypting the string
# encoded byte string is returned by decrypt method,
# so decode it to string with decode methods
decMessage = fernet.decrypt(encMessage).decode()
 
print("decrypted string: ", decMessage)
"""