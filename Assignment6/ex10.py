num = int(input("Enter a Number: "))
# count = len(num)
# print("There are %r no. of digits in %r" % (count, num))

count = 0
while num > 0:
    count += 1
    num //= 10
print("The digit count is: ", count)
