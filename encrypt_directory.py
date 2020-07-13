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

    # Provide decription of the program
    parser = argparse.ArgumentParser(description='Enrypt all the files in the given directory with the provided key')
    op_mode = parser.add_mutually_exclusive_group()

    # Optional flag for individual file mode of operation, if not included use directory mode
    op_mode.add_argument('-d', '--dirmode',
                        help='Use to encrypt an entire directory as opposed to a single file',
                        action='store_true')
    op_mode.add_argument('-f', '--filemode',
                        help='Use to encrypt a single file as opposed to an entire directory',
                        action='store_true')

    # Positional arguments for specifying target directory/file and key to be used in the keystream
    parser.add_argument('target', help='The directory that you want to encrypt; If file mode is used this becomes a file')
    parser.add_argument('key', help='The key to be used in the encryption process')
    args = parser.parse_args()
    
    print(args.dirmode)
    print(args.filemode)
    start_directory = args.target
    print(start_directory)
    key = args.key
    print(key)
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