#!/usr/bin/python3
""" defining class to inherit from list"""


class MyList(list):
    """
    A custom list class that inherits from the built-in.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        new_list = self.copy()
        new_list.sort()
        print(new_list)
