num = int(input("Enter a number: "))
cpy = num
num1 = 0
rev = 0
while num > 0:
    num1 = num % 10
    num //= 10
    rev = (rev * 10) + num1
print("%r reversed to %r\n" % (cpy, rev))
