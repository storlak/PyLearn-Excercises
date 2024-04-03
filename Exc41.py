# encryption programme with key

import random
import string

chars = " " + string.ascii_letters + string.punctuation + string.digits
chars = list(chars)
key = chars.copy()
random.shuffle(key)

print(f"chars:{chars}")
print(f"key: {key}")

# Encrypt
plain_text = input("Enter your message to encrypt: ")
cipher_text = ""
for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]
print(f"original message: {plain_text}")
print(f"ciphered message: {cipher_text}")
