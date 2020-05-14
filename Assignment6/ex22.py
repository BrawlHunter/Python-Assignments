def find_hcf(x, y):
    if x > y:
        small = y
    else:
        small = x
        for n in range(1, small + 1):
            if x % n == 0 and y % n == 0:
                hcf = n
    return hcf


num1 = int(input("Enter no.: "))
num2 = int(input("Enter no.: "))
print(find_hcf(num1, num2))
