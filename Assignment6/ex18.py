from collections import Counter
# 1 Using counter from collections
num = int(input("Enter a Number: "))
frequency = Counter(str(abs(num)))
print(frequency)


# 2 using dictionary
def frequency(no):
    freq = dict()
    while no > 0:
        index = no % 10
        if index in freq:
            freq[index] = freq[index] + 1
        else:
            freq[index] = 1
        no = no // 10
    return freq


num1 = int(input("Enter a no. : "))
print(frequency(abs(num1)))
