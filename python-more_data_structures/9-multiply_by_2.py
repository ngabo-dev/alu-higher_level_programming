#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dict = 1
    for key in a_dictionary:
        new_dict *= a_dictionary[key]
    return new_dict
