"""
References:
https://www.geeksforgeeks.org/hashlib-sha3_384-in-python/
https://www.tutorialspoint.com/sha-in-python
https://www.geeksforgeeks.org/os-walk-python/
https://stackoverflow.com/a/14334768
https://stackoverflow.com/questions/273192/how-can-i-safely-create-a-nested-directory
https://ttboj.wordpress.com/2010/02/03/getopt-vs-optparse-vs-argparse/
https://docs.python.org/3/howto/argparse.html
https://thispointer.com/python-how-to-get-the-current-working-directory/
https://codeigo.com/python/get-directory-of-a-file
"""

import argparse, os
from hashlib import sha3_384
from os import listdir, walk
from os.path import isfile, isdir, join, splitext

def main():

    # Provide decription of the program
    parser = argparse.ArgumentParser(
        description='Enrypt all the files in the given directory with the provided key; program encrypts directories by default'
    )
    op_mode = parser.add_mutually_exclusive_group()

    # Optional flag for individual file mode of operation; if not included, program uses directory mode
    op_mode.add_argument(
        '-d', '--dirmode',
        help='Use to encrypt an entire directory as opposed to a single file',
        action='store_true'
    )
    op_mode.add_argument(
        '-f', '--filemode',
        help='Use to encrypt a single file as opposed to an entire directory',
        action='store_true'
    )

    # Positional arguments for specifying target directory/file and key to be used in the keystream
    parser.add_argument(
        'target',
        help='The directory that you want to encrypt; If file mode is used this becomes a file'
    )
    parser.add_argument(
        'key',
        help='The key to be used in the encryption process'
    )

    # Parse arguments and initialize variables
    args = parser.parse_args()
    target = args.target
    key = args.key

    # Hash key to create keystream to be used in XOR cipher
    keystream = sha3_384()
    keystream.update(key.encode())

    # Filemode operation explicitly provided
    if args.filemode:
        
        # Verify that target is actually a file and exists
        if not isfile(target):
            raise SystemExit("ERROR: The provided argument for target: " + target + " is not a file or doesn't exist")

        # Verify that the file is not in the current working directory
        abs_filepath = os.path.realpath(target)
        dir_path = os.path.dirname(abs_filepath)
        if dir_path == os.getcwd():
            raise SystemExit('ERROR: The file is in the same directory as the current working directory')

        # Only one file to apply the cipher to
        cipher_file(target, keystream.digest())

    # Otherwise dirmode is explicitly provided or excluded (default program mode is dirmode)
    else:
        
        # Verify that target is actually a directory and exists
        if not isdir(target):
            raise SystemExit("ERROR: The provided argument for target: " + target + " is not a directory or doesn't exist")

        #  Verify that target is not the current working directory
        abs_filepath = os.path.realpath(target)
        if abs_filepath == os.getcwd():
            raise SystemExit('ERROR: The file is in the same directory as the current working directory')

        # Iterate through all the files in the directory tree (depth-first)
        for (root, directories, files) in walk(target, topdown=False):

            # Get all files in the current directory
            file_list = [join(root, f) for f in files]
            for filepath in file_list:
                cipher_file(filepath, keystream.digest())

# Apply XOR cipher over two byte sequences and return the resulting list of bytes
def cipher(message, key):
    return bytes([message[i] ^ key[i % len(key)] for i in range(0, len(message))])

# Read file contents, apply the cipher, and write the result back to the file
def cipher_file(filepath, key_bytes):

    with open(filepath, 'rb+') as file:
        file_contents = file.read()
        ciphertext = cipher(file_contents, key_bytes)
        file.seek(0, 0)
        file.write(ciphertext)

# Only execute if called directly
if __name__ == "__main__":
    main()