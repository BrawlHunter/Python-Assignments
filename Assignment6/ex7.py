num = int(input("Enter the number: "))
result = 0
for n in range(num + 1):
    if n % 2 == 0:
        result = result + n
    else:
        continue
print("Sum of all even nos. from 1 to %r is: " % num, result)
