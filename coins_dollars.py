total_change = int(input())

if total_change <= 0:
    print("No change")
else:
    num_dollars = total_change // 100
    total_change %= 100

    num_quarters = total_change // 25
    total_change %= 25

    num_dimes = total_change // 10
    total_change %= 10

    num_nickels = total_change // 5
    num_pennies = total_change % 5

    if num_dollars > 0:
        if num_dollars == 1:
            print("1 Dollar")
        else:
            print(f"{num_dollars} Dollars")

    if num_quarters > 0:
        if num_quarters == 1:
            print("1 Quarter")
        else:
            print(f"{num_quarters} Quarters")

    if num_dimes > 0:
        if num_dimes == 1:
            print("1 Dime")
        else:
            print(f"{num_dimes} Dimes")

    if num_nickels > 0:
        if num_nickels == 1:
            print("1 Nickel")
        else:
            print(f"{num_nickels} Nickels")

    if num_pennies > 0:
        if num_pennies == 1:
            print("1 Penny")
        else:
            print(f"{num_pennies} Pennies")