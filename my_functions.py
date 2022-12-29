from math import *


def ln(x):
    return log(x)


def numerator_is_not_zero(function, a):
    x = a
    return eval(function.split('/')[0]) != 0


def convert_function(function):
    """replace all bad symbols"""
    if '^' in function:
        function = function.replace('^', '**')
    return function


def test_uncertainty(function, a):
    x = a
    if isinf(eval(function.split('/')[0])):
        print('всё хуйня - давай поновой')

