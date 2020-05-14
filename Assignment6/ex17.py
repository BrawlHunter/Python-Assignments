num = int(input("Enter the number: "))
cpy = num
num1 = 0
rev = 0
while num > 0:
    num1 = num % 10
    num //= 10
    rev = (rev * 10) + num1
if rev == cpy:
    print("%r is a palindrome no." % cpy)
else:
    print("%r is not a palindrome no." % cpy)
