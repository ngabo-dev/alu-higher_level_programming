#!/usr/bin/python3
def uppercase(input_string):
    output_string = ""
    for char in input_string:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        output_string += char
    print(f"{output_string}\n")
input_string = input("Enter a string: ")
uppercase(input_string)
