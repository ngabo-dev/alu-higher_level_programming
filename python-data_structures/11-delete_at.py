#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    for i in range(len(my_list)):
        if i != idx:
            return i

        if idx < 0 or idx >= len(my_list):
            return my_list
        
