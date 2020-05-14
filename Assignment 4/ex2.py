file = open("C:\\Users\\dell\\Desktop\\akshay.txt", 'r+')
# file1 = open("C:\\Users\\dell\\Desktop\\akshay.txt", 'w')

data = file.read()
data1 = data[::-1]
# print(data1)
file.seek(0)
file.truncate()
file.write(data1)
file.close()


