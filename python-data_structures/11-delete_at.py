#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0 or idx >= len(my_list):
        return my_list

    new_list = my_list[:idx] + my_list[idx+1:]
   # return new_list

original_list = [1, 2, 3, 4, 5, 6, 7]
modified_list = delete_at(original_list, 4)
print(modified_list)
