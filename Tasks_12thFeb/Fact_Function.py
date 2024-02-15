def facto(num2):
    fact = 1
    for i in range(num2):
        fact = fact * num2
        num2 = num2 - 1
    print(fact)
    return num2


num = int(input("Enter the number:"))

facto(num)