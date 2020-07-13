"""
References:
https://www.geeksforgeeks.org/hashlib-sha3_384-in-python/
https://www.tutorialspoint.com/sha-in-python
https://www.geeksforgeeks.org/os-walk-python/
https://stackoverflow.com/a/14334768
https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory
https://ttboj.wordpress.com/2010/02/03/getopt-vs-optparse-vs-argparse/
https://docs.python.org/3/howto/argparse.html
"""

import sys, argparse
from hashlib import sha3_384
from os import listdir, walk
from os.path import isfile, join, splitext


def main():

    parser = argparse.ArgumentParser(description='Enrypt all the files in the given directory with the provided key')
    parser.add_argument('directory')
    parser.add_argument('key')
    args = parser.parse_args()
    
    start_directory = args.directory
    key = args.key
    # # Set variables based on command line arguments
    # start_directory = '../wf_proj_backup/'
    # key = "my_frame_is_the_hand_and_i_am_the_will"

    # # Hash key to create keystream to be used in XOR cipher
    # keystream = sha3_384()
    # keystream.update(key.encode())

    # # Iterate through all the files in the directory tree (depth-first)
    # for (root, directories, files) in walk(start_directory, topdown=False):

    #     # Get all files in the current directory
    #     file_list = [f for f in listdir(root) if isfile(join(root, f))]
        
    #     for file_ in file_list:

    #         filepath = join(root, file_)
    #         with open(filepath, 'rb+') as file:

    #             # Read file contents, apply the cipher, and write the result back to the file
    #             msg = file.read()
    #             ciphertext = cipher(msg, keystream.digest())
    #             file.seek(0, 0)
    #             file.write(ciphertext)

def cipher(message, key):
    return bytes([message[i] ^ key[i % len(key)] for i in range(0, len(message))])

if __name__ == "__main__":
    main()

    # TODO Add a separate single file encrypt mode so you can encrypt single files inside of an entire directory