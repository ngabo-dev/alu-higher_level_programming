#!/usr/bin/python3
alphabet = ''.join(chr(char) for char in range(ord('a'), ord('z') + 1)
    if chr(char) not in ['e', 'q'])
print("{}".format(alphabet), end='')
