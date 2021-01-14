import os

print(os.getcwd())
list_dir = os.listdir(path=".")
print(len(list_dir))
for i in range(len(list_dir)):
    print(list_dir[i])

os.chdir(r"E:\Games")
print(os.getcwd())
list_dir = os.listdir(path=".")
print(len(list_dir))
for i in range(len(list_dir)):
    print(list_dir[i])