import math


# your code here
def math_factorial(x):
    print("Don't cheat!")
    return x


math.factorial = math_factorial

# don't delete this line, please
math.factorial(23)
