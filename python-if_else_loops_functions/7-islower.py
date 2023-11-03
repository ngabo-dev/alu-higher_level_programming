#!/usr/bin/python3
def islower(c):
    return 97 <= ord(c) <= 122

character = input("")
if islower(character):
    print(f"{character} => lower.")
else:
    print(f"{character} => upper.")
