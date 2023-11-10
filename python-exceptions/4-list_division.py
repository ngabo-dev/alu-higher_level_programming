#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
  uptodate_list = []
  for index in range(list_length):
    try:
      uptodate_list.append(my_list_1[index] / my_list_2[index])
    except TypeError:
      print("wrong type")
      uptodate_list.append(0)
    except ZeroDivisionError:
      print("division by 0")
      uptodate_list.append(0)
    except IndexError:
      print("out of range")
      uptodate_list.append(0)
    finally:
      pass
  return uptodate_list
