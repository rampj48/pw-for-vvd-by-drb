import math
from math import *

x = 2.444
y = 0.869 * 10 ** (-2)
z = -0.13 * 10 ** 3

s = ((x ** (y + 1)) + (math.e ** (y - 1))) / (1 + x * (abs(y - tan(z)))) * (1 + (abs(y - x))) + (
        ((abs(y - x)) ** 2) / 2) - (((abs(y - x)) ** 3) / 3)
print(s)  # -0.49870726733226345
