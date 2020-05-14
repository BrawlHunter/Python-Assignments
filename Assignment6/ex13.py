num = int(input("Enter a number: "))
num1 = num
# first we will count the digits
count = 0
while num1 > 0:
    count += 1
    num1 //= 10
# then we will use count-1 as power of 10
# and find 1st and last nos.
power = 10 ** (count - 1)
first = num // power
last = num % 10
# then we find the number without 1st and last nos.
num3 = num % (first * power)
num3 //= 10
# now we finally find the swapped output
swap = (last * power) + (num3 * 10) + first
print("After swapping first and last digit of %r we get: " % num, swap)
