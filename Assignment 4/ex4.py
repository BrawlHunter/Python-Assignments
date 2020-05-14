file = open(r"C:\Users\dell\Desktop\akshay.txt", 'r')
data = file.read()
words = len(data.split())
print("Total %d words in %r" % (words, data))

