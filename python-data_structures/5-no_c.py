#!/usr/bin/python3
def no_c(my_string):
    new_string = ''
    for c in [c for c in my_string if c != 'c']:
      new_string += c
