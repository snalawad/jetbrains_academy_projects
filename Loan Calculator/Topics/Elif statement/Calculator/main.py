# put your python code here
operations = ["mod", "pow", "div"]

num1 = float(input())
num2 = float(input())
operation = (input())

if num2 == 0.0 and operation in ["mod", "/", "div"]:
    print("Division by 0!")
elif operation == "/":
    calc = num1 / num2
    print(calc)
elif operation == "mod":
    calc = num1 % num2
    print(calc)
elif operation == "div":
    calc = num1 // num2
    print(calc)
elif operation == "+":
    calc = num1 + num2
    print(calc)
elif operation == "-":
    calc = num1 - num2
    print(calc)
elif operation == "*":
    calc = num1 * num2
    print(calc)
elif operation == "pow":
    calc = num1 ** num2
    print(calc)

