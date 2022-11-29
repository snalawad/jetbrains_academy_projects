from math import ceil, log, pow
import argparse


def incorrect():
    print("Incorrect parameters")
    quit()


parser = argparse.ArgumentParser(description="Loan Calculator")
parser.add_argument("--type", choices=["annuity", "diff"])
parser.add_argument("--principal", type=int)
parser.add_argument("--payment", type=int)
parser.add_argument("--periods", type=int)
parser.add_argument("--interest", type=float)
args = parser.parse_args()

if args.interest:
    interest = args.interest
    nominal = (interest / 100) / 12
else:
    incorrect()

if args.type == "diff":
    if not args.payment:
        principal = args.principal
        periods = args.periods
        if principal < 0 or periods < 0:
            incorrect()
        overpayment = 0
        for m in range(1, periods + 1):
            paren = principal - ((principal * (m - 1)) // periods)
            dm = ceil((principal // periods) + (nominal * paren))
            overpayment += dm
            print(f"Month {m}: payment is {dm}")
        print()
        print(f"Overpayment = {overpayment - principal}")
    else:
        incorrect()
elif args.type == "annuity":
    if not args.periods:
        payment = int(args.payment)
        principal = int(args.principal)
        periods = ceil(log(payment / (payment - nominal * principal), 1 + nominal))
        if periods % 12 == 0:
            print(f"It will take {periods // 12} years to repay this loan!")
        else:
            if periods > 12:
                print(f"It will take {periods // 12} years and {periods % 12} months to repay this loan!")
            else:
                print(f"It will take {periods % 12} months to repay this loan!")
        print(f"Overpayment = {(payment * periods) - principal}")
    elif not args.payment:
        principal = int(args.principal)
        periods = int(args.periods)
        fraction = (nominal * pow(1 + nominal, periods)) / (pow(1 + nominal, periods) - 1)
        payment = int(principal * fraction + 1)
        print(f"Your monthly payment = {payment}!")
        print(f"Overpayment = {(payment * periods) - principal}")
    elif not args.principal:
        payment = int(args.payment)
        periods = int(args.periods)
        fraction = (nominal * pow(1 + nominal, periods)) / (pow(1 + nominal, periods) - 1)
        principal = int(payment // fraction)
        print(f"Your loan principal = {principal}!")
        print(f"Overpayment = {(payment * periods) - principal}")
else:
    incorrect()
