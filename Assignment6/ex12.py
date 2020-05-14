num = int(input("Enter number: "))
first = num
last = num
while first >= 10:
    first //= 10
last %= 10
print("The sum of 1st and last digit of %r is: " % num, first + last)
