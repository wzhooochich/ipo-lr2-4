import math

x = int(input("Введи x: "))
y = int(input("Введи y: "))
z = float(input("Введи z: "))

b = math.sqrt(10 * (x * (1. / 3.) + x * (y + 2))) * (math.asin(z) ** 2) - abs(x - y)
print(b)