def make_change(denomination_list, amount):
    denomination_list = sorted(denomination_list, reverse = True)
    total = 0
    for money in denomination_list:
        if(money <= amount):
            total += amount // money
            amount -= (amount // money) * money
    return total

#Pass different values to the function and test your program
amount= 20
denomination_list = [1,15,10]
print(make_change(denomination_list, amount))