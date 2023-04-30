import math
a = int(input("enter value A: "))
print(a)
b = int(input("enter value B: "))
print(b)
c = int(input("enter value C: "))
print(c)
p = (a + b + c)/2
print("value:", p)
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("result: ", s)
