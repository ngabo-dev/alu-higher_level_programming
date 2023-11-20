#!/usr/bin/python
""" defining class to inherit from list"""


class MyList(list):
    """
    A custom list class that inherits from the built-in.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
