import os
import json
import base64
from typing import TypedDict, List

from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.backends import default_backend
from cryptography.fernet import Fernet


AuthenticationInformation = TypedDict(
    'AuthenticationInformation', 
    application=str,
    username=str,
    password=str, 
    label=str
)

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


def encrypt_json_information(
        key: bytes, 
        data: List[AuthenticationInformation]
    ):
    """
    Encrypts a json object into bytes.

    Parameters:
    key (bytes) - encryption key
    data (List[AuthenticationInformation]) - json information

    Returns:
    (bytes) - json information encrypted into bytes
    """

    fernet = Fernet(key)
 
    return fernet.encrypt(json.dumps(data).encode())


def decrypt_json_information(
        key: bytes, 
        data: bytes
    ):
    """
    Decrypts a bytes object into json

    Parameters:
    key (bytes) - encryption key
    data (List[AuthenticationInformation]) - json information

    Returns:
    (List[AuthenticationInformation]) - json information decrypted from bytes
    """

    fernet = Fernet(key)
 
    return fernet.decrypt(data).decode()