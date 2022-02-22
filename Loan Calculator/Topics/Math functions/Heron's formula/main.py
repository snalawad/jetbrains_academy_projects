# put your python code here
import math

a, b, c = map(int, input().split())
p = (a + b + c) / 2
root = p * (p-a) * (p-b) * (p-c)
herons = math.sqrt(root)
print(herons)
