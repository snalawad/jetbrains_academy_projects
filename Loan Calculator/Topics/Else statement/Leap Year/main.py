# put your python code here
a = int(input())

leap_yr = a % 4 == 0 and (a % 400 == 0 or a % 100 != 0)

if leap_yr is True:
    print("Leap")
else:
    print("Ordinary")
    