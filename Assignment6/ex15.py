num = int(input("Enter number: "))
num1 = num
result = 1
while num > 0:
    result *= num % 10
    num //= 10
print("The product of all digits in %r is : " % num1, result)
