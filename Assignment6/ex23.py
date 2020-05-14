def find_hcf(x, y):
    if x > y:
        small = y
    else:
        small = x
        for n in range(1, small + 1):
            if x % n == 0 and y % n == 0:
                hcf = n
    return hcf


def find_lcm(x, y):
    lcm = (x * y) // find_hcf(x, y)
    return lcm


num1 = int(input("No.1 :"))
num2 = int(input("No.2 :"))

print("LCM of %r and %r is : " % (num1, num2), find_lcm(num1, num2))
