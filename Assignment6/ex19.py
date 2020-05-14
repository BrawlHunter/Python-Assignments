num = int(input("Enter a number: "))
power = int(input("Enter the power: "))
result = 1
for n in range(1, power + 1):
    result = result * num
print("%r ^ %r = %r" % (num, power, result))
