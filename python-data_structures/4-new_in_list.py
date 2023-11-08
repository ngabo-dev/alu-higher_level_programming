#!/usr/bin/python3
def new_in_list(my_list, idx, element):
        if idx < 0 and idx >= len(my_list):
            return my_list[:]

    list_storage = my_list[:]
    list_storage[idx] = element
    return list_storage
