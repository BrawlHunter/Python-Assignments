num = int(input("Enter Number: "))
factorial = 1
for n in range(1, num + 1):
    factorial = factorial * n
print("Factorial of %r is : " % num, factorial)
