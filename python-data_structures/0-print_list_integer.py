#!/usr/bin/python3
def print_list_integer(my_list=[]):
    for number in my_list:
        print("{:d}".format(number))
number = [1, 2, 3]
print_list_integer()
