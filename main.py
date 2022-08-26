from utils import (
    generate_key_from_password, 
    encrypt_json_information, 
    decrypt_json_information
)


message = [
    {
        "application" : "PayPal",
        "username": "michaels username",
        "password": "michaels password"
    }
]

key = generate_key_from_password("my pass")

enc = encrypt_json_information(key, message)

print(decrypt_json_information(key, enc))
