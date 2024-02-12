import math
a = int(input())
b = int(input())
area = (1/4) * a * b**2 / math.tan(math.pi / a)
print (round(area, 0))