#!/usr/bin/python3
def no_c(my_string):
    upper_case_string = my_string.upper()
    new_string = ''.join([c for c in my_string if c != 'c'])
    new_string = ''.join([c for c in my_string if c != 'C'])
    return new_string
