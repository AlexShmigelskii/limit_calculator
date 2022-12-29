# # file for random stuff
#
# x = float('0')
# f = 'x/x'
#
#
# def numerator_is_zero(s):
#     return eval(s.split('/')[0]) == 0
#
#
# def main():
#     try:
#         eval(f)
#     except ZeroDivisionError:
#         if not numerator_is_zero(f):
#             print(float('inf'))
#
#         else:
#             print('не, ну тут другой случай [0/0]')
#             return 1
#
#
# if __name__ == '__main__':
#     main()
from math import *


x = float('inf')
f = 'x**3/x**4'

print(isinf(eval(f.split('/')[0] and f.split('/')[1])))
