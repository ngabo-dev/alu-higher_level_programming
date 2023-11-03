#!/usr/bin/python3
def uppercase(input_string):
    output_string = ""
    for char in input_string:
        if 97 <= ord(char) <= 122:
            char = chr(ord(char) - 32)
        output_string += char
    print("{}\n".format(output_string))

#test cases
test_cases = [
    "holberton",
    "Holberton School",
    "Holberton School, 98 battery street",
    "",
    "98",
    "z"
]

for test_case in test_cases:
    print("Input: {}".format(test_case))
    uppercase(test_case)
