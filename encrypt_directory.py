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
from os import listdir, walk, sep, mkdir
from os.path import isfile, join, splitext
from pathlib import Path

def cipher(message, key):
     return bytes([message[i] ^ key[i % len(key)] for i in range(0, len(message))])

# Hash key to create keystream and XOR to encrypt
# Using hashlib.sha3_384() method 
key = "my_frame_is_the_hand_and_i_am_the_will"
keystream = sha3_384()
keystream.update(key.encode())

start_directory = '../wf_proj_backup/'
for (root, directories, files) in walk(start_directory, topdown=False):

    Path(join(*root.split(sep)[1:])).mkdir(parents=True, exist_ok=True)

    # Get all files in the current directory
    file_list = [f for f in listdir(root) if (isfile(join(root, f)) and splitext(f)[1]=='.py')]

    for file_ in file_list:
        with open(join(root, file_), 'rb') as file:
            msg = file.read()
            ciphertext = cipher(msg, keystream.digest())

        filename_out = join('.', *root.split(sep)[1:], (splitext(file_)[0] + "_enc" + splitext(file_)[1]))
        with open(filename_out, 'wb') as file:
            file.write(ciphertext)