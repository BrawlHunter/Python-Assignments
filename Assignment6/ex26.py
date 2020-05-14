num = int(input("Enter a number : "))
count = len(str(num))
temp = num
result = 0
for n in range(1, count + 1):
    while temp > 0:
        digit = temp % 10
        result = result + (digit ** 3)
        temp //= 10
if result == num:
    print("%r is an armstrong number." % result)
else:
    print("Not an armstrong no.")
