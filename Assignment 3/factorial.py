num = int(input("Enter the number:"))
factorial = 1
if num < 0:
    print("Please enter a no. >= 0:")
elif num == 0:
    print("Factorial of 0 is: 1")
else:
    for x in range(1, num+1):
        factorial = factorial * x
print("The factorial of %r is: %r" % (num, factorial))
