num = int(input("Enter the range: "))
# for n in range(1, num + 1):
for n in range(2, num + 1):
    prime = True
    for m in range(2, n):
        if n % m == 0:
            prime = False
        else:
            prime = True
    if prime:
        print(n)
