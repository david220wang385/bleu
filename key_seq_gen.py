key = "tiger"
dictionary = 'abcdefghijklmnopqrstuvwxyz'

# Get all two character pairs
pairs = [key[i]+key[i+1] for i in range(len(key)-1)]
print(pairs)

# Assume key is lowercase
for pair in pairs:
    (ord(pair[0]) - 97) + (ord(pair[1]) - 97)