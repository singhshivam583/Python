import sys

# maxdigits must be 0 or larger than 64
sys.set_int_max_str_digits(10000)

# a = 2**10000
# print(a)
# print(len(str(a)))

# repr('chai')
# str('chai')
# print('chai')


# conversions
# by default base is 10 , so no prefix needed for decimal numbers 
import math 

# print(hex(65)) 
# print(oct(65))
# print(bin(65)) 

# convert any number in int
# int('number', base)
# a = int('010',2)
# a = int('14',8)
# a = int('141F',16)
# print(a)

import random

# print(random.random())
# print(random.randint(1,10))

choice = ['lemon', 'masala', 'ginger', 'elaichi']
# print(random.choice(choice)) 

# shuffling array elements
arr = [1,3,7,9]
# random.shuffle(arr)
# print(arr)

from decimal import Decimal

# print(0.1+0.1+0.1)
# print(0.1+0.1+0.1 - 0.3)

# print(decimal(0.1) + decimal(0.1) + decimal(0.1))
# print(decimal(0.1) + decimal(0.1) + decimal(0.1) - decimal(0.3))

from fractions import Fraction

# print(Fraction(2,8))


# sets
# a = {1,2,3,4,5,6}
# b = {1,2,4,6,8}

# print(a & b)
# print(a | b)
# print(a ^ b)
# print(a - b)
print(type(a))









