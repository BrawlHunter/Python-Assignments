file = open(r"C:\Users\dell\Desktop\akshay.txt", 'r')

username = input("Enter username: ")
password = input("Enter password: ")

data = file.read()
words = data.split()

if username == words[0] and password == words[1]:
    print("Welcome, " + username)
else:
    print("Credentials Mismatch !")
