
num = int(input("Enter a limit: "))
for n in range(1, num + 1):
    result = 0
    temp = n
    while temp > 0:
        digit = temp % 10
        result = result + (digit ** 3)
        temp //= 10
    if n == result:
        print(n)
