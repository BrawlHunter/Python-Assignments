import glob
import os

# for listing files in the given path
path = r"C:\Users\dell\Desktop"
file = os.listdir(path)
print(file)

# for listing full path of files
for root, dirs, files in os.walk(path):
    for f in files:
        print(os.path.join(path, f))

# Another method using glob
g = glob.glob('*')
for f in g:
    print(os.path.join(path, f))

