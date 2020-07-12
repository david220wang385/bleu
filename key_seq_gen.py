import hashlib, binascii
from hashlib import md5, sha3_384
"""
References:
https://www.geeksforgeeks.org/hashlib-sha3_384-in-python/
https://www.tutorialspoint.com/sha-in-python
https://stackoverflow.com/questions/16862497/python-bytes-literal-has-extra-characters-that-arent-hex-but-alter-the-value-o
"""

def cipher(message, key):
     return bytes([message[i] ^ key[i % len(key)] for i in range(0, len(message))])

msg = "This is a haiku; it is not too long I think; but you may disagree"
key = "But there's one sound that no one knows... What does the Fox say?"

# Hash key to create keystream and XOR to encrypt
# Using hashlib.sha3_384() method 
# keystream = sha3_384()
# keystream.update(key.encode())
# print(keystream.digest())

ciphertext = cipher(msg.encode(), key.encode())
print(ciphertext)
print(ciphertext.hex())

# YES JUST WHAT I WANTED
print(binascii.hexlify(ciphertext))
cipher_read = bytes(ciphertext)
