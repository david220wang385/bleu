import hashlib, binascii
from hashlib import md5, sha3_384
"""
References:
https://www.geeksforgeeks.org/hashlib-sha3_384-in-python/
https://www.tutorialspoint.com/sha-in-python
https://stackoverflow.com/questions/16862497/python-bytes-literal-has-extra-characters-that-arent-hex-but-alter-the-value-o
https://docs.python.org/3.1/library/binascii.html#binascii.b2a_hex
"""

def cipher(message, key):
     return bytes([message[i] ^ key[i % len(key)] for i in range(0, len(message))])

msg = "This is a haiku; it is not too long I think; but you may disagree"
key1 = "But there's one sound that no one knows... What does the Fox say?"
key2 = "I didn't like that haiku. I should try another one..."

# Hash key to create keystream and XOR to encrypt
# Using hashlib.sha3_384() method 
keystream1 = sha3_384()
keystream1.update(key1.encode())

keystream2 = sha3_384()
keystream2.update(key2.encode())

int_key = cipher(keystream2.digest(), keystream1.digest())
ciphertext = cipher(msg.encode(), int_key)

firstback = cipher(ciphertext, keystream1.digest())
secondback = cipher(firstback, keystream2.digest())

# Prove cipher works
print(msg.encode())
print(ciphertext)
print(firstback)
print(secondback)
