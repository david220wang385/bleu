"""
References:
https://www.geeksforgeeks.org/hashlib-sha3_384-in-python/
https://www.tutorialspoint.com/sha-in-python
https://www.geeksforgeeks.org/os-walk-python/
https://stackoverflow.com/a/14334768
https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory
"""

import hashlib
from hashlib import sha3_384
from os import listdir
from os.path import isfile, join, splitext

def cipher(message, key):
     return bytes([message[i] ^ key[i % len(key)] for i in range(0, len(message))])

directory = '../wf_proj_backup'
key = "my_frame_is_the_hand_and_i_am_the_will"

# Hash key to create keystream and XOR to encrypt
# Using hashlib.sha3_384() method 
keystream = sha3_384()
keystream.update(key.encode())
print(keystream.digest())

# Get all files in the directory
file_list = [f for f in listdir(directory) if (isfile(join(directory, f)) and splitext(f)[1]=='.py' and splitext(f)[0][-4:]=='_enc') ]
print(file_list)

for file_ in file_list:
     with open(join(directory, file_), 'rb') as file:
          msg = file.read()
          ciphertext = cipher(msg, keystream.digest())

     # reverse = cipher(ciphertext, keystream.digest())
     filename_out = splitext(file_)[0] + "_dec" + splitext(file_)[1]
     with open(filename_out, 'wb') as file:
          file.write(ciphertext)