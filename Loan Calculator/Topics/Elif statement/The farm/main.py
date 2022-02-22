money = int(input())

chicken = 23
goat = 678
pig = 1296
cow = 3848
sheep = 6769

if chicken <= money < goat:
    cost = money//chicken
    if cost == 1:
        print(cost, "chicken")
    else:
        print(cost, "chickens")
elif goat <= money < pig:
    cost = money // goat
    print(cost, "goat")
elif pig <= money < cow:
    cost = money // pig
    if cost == 1:
        print(cost, "pig")
    else:
        print(cost, "pigs")
elif cow <= money < sheep:
    cost = money // cow
    print(cost, "cow")
elif sheep <= money:
    cost = money // sheep
    print(cost, "sheep")

else:
    print("None")
