import math
from math import pi
length_str = input("Enter radius of square:")
length_int = int(length_str)
radius_square = 2 * (length_int ** 2)
area = math.pi * radius_square
print("Area =",area)
