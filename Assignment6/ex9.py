num = int(input("Enter a number: "))
result = 1
for n in range(1, 11):
    result = num * n
    print("%r x %r = %r" % (num, n, result))
