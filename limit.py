from my_functions import *
from calculate_uncertainty import *


class Limit(object):
    """class limit"""
    def __init__(self, function, arg, side=''):
        self.function = convert_function(function)
        self.arg = arg
        self.side = side

    def print_init(self):
        print('_______________________________________')
        print('Рассчитаем предел функции ', self.function)
        print('при стремлении аргумента к ', self.arg, self.side)
        print('_______________________________________')

    def calculate_limit(self):
        """calculating the limit"""
        x = self.arg

        try:
            if isnan(eval(self.function)):
                print("it is nan. Let's check for uncertainty...")
                test_uncertainty(self.function, x)

        except ZeroDivisionError:  # Check for zero division
            if numerator_is_not_zero(self.function, x):
                return print(float('inf'))

            else:
                division_zero_by_zero(self.function, x)
                return print('здесь будет решаться неоределенность [0/0]')

