num = int(input("Enter range: "))
num1 = 0
num2 = 1
result = num1 + num2
print(num1)
print(num2)
for n in range(0, num + 1):
    result = num1 + num2
    num1 = num2
    num2 = result
    print(result)
