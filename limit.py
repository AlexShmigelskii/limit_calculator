from my_functions import *


class Limit(object):
    """class limit"""
    def __init__(self, function, arg, side=''):
        self.function = self.convert_function(function)
        self.arg = arg
        self.side = side

    def print_init(self):
        print(self.function, self.arg, self.side)

    @staticmethod
    def convert_function(function):
        """replace all bad symbols"""
        if '^' in function:
            function = function.replace('^', '**')
        return function

    def calculate_limit(self):
        """calculating the limit"""
        x = self.arg
        return print(eval(self.function))

