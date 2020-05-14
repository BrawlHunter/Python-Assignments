num = int(input("Enter number: "))
first = num
last = num
while first >= 10:
    first //= 10
last %= 10
print("1st digit is '%r' and last digit is '%r' in %r." % (first, last, num))
