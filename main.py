from cryptography.fernet import Fernet
import hashlib
import base64

my_password = 'swordfish'
key = hashlib.md5(my_password.encode('ascii')).hexdigest()
key_64 = base64.urlsafe_b64encode()
cipher = Fernet(key_64).encrypt("My dirty secrets")