import math

calculate = input('''What do you want to calculate?
type "n" for number of monthly payments,
type "a" for annuity monthly payment amount,
type "p" for loan principal:
''')
if calculate == "n":
    principal = int(input('Enter the loan principal:'))
    payment = int(input('Enter the monthly payment:'))
    interest = input('Enter the loan interest:')
    i = (12 / 100 * float(interest)) / (12 * 12 / 100 * 100)
    a = (payment / (payment - i * principal))
    n = round(math.log(a, (i + 1)))
    if n <= 12:
        print("It will take", n, "months to repay this loan!")
    elif n > 12:
        print("It will take", n // 12, "years and", n % 12 + 1, "months to repay this loan!")
if calculate == "a":
    principal = int(input('Enter the loan principal:'))
    periods = int(input('Enter the number of periods:'))
    interest = input('Enter the loan interest:')
    i = (12 / 100 * float(interest)) / (12 * 12 / 100 * 100)
    a = math.ceil(principal * ((i * (1 + i)**periods) / ((1 + i)**periods - 1)))
    print(f"Your monthly payment = {a}!")
if calculate == "p":
    annuity = float(input('Enter the annuity payment:'))
    periods = int(input('Enter the number of periods:'))
    interest = float(input('Enter the loan interest:'))
    i = (12 / 100 * interest) / (12 * 12 / 100 * 100)
    p = math.floor(annuity / ((i * (1 + i)**periods) / ((1 + i)**periods - 1)))
    print(f"Your loan principal = {p}!")
