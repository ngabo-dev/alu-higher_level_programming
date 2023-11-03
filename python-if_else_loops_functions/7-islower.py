#!/usr/bin/python3
def islower(c):
    return 97 <= ord(c) <= 122

character = input("Enter a character: ")
if islower(character):
    print(f"{character} is lower.")
else:
    print(f"{character} is upper.")
