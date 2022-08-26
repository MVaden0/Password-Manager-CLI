import os
import json
import base64

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


def generate_key_from_password(
        password: str
    ) -> bytes:
    """
    Generates a fernet acceptible key from a given password.

    Parameters:
    password (str) - the given password

    Returns:
    (bytes) - encoded fernet key
    """
    _backend = default_backend()
    _salt = os.urandom(16)

    _kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=_salt,
        iterations=100000,
        backend=_backend
    )

    _encoded_password = bytes(password, encoding='utf-8')

    _key = base64.urlsafe_b64encode(_kdf.derive(_encoded_password))

    return _key

# we will be encrypting the below string.
message = [
    {
        "application" : "PayPal"
    }
]
 
 
# Instance the Fernet class with the key
 
fernet = Fernet(generate_key_from_password("my pass"))
 
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
