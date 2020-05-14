file = open("C:\\Users\\dell\\Desktop\\akshay.txt", 'r')
data = file.read()

words = len(data.split())
lines = len(data.splitlines())
chars = len(data)

print("There are %r words, %r lines and %r characters in this file." % (words, lines, chars))
