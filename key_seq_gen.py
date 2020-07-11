import hashlib
from hashlib import md5, sha3_384
"""
References:
https://www.geeksforgeeks.org/hashlib-sha3_384-in-python/
https://www.tutorialspoint.com/sha-in-python

"""

def cipher(message, key):
     return bytes([message[i] ^ key[i % len(key)] for i in range(0, len(message))])

key = "tiger"
msg = "nobody expects the spammish repitition"

# Hash key to create keystream and XOR to encrypt
# Using hashlib.sha3_384() method 
keystream = sha3_384() 
keystream.update(key.encode())

print(keystream.hexdigest().encode())

ciphertext = cipher(msg.encode(), key.encode())
print(ciphertext)
cipher_read = bytes(ciphertext)
print(cipher_read.decode())