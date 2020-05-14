def length(string1, string2):
    if len(string1) == len(string2):
        return string1, string2
    else:
        if len(string1) > len(string2):
            return string1
        else:
            return string2


str1 = input("Enter first string: ")
str2 = input("Enter second string: ")
result = length(str1, str2)
print(result)
