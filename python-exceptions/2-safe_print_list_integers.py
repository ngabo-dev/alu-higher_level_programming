#!/usr/bin/python3
def safe_print_list_integers(my_list=[], count=0):
  for i in range(count):
    try:
      print("{:d}".format(my_list[i]), end="")
    except (ValueError, TypeError):
      pass
  print()
