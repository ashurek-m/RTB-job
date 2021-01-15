import os, glob

print(os.getcwd())
list_dir = os.listdir(path=".")
print(list_dir)

lop = glob.glob('*.txt')
print(lop)
print()
print(glob.glob(f'{os.getcwd()}\*'))

os.chdir('.\op_10')
print(os.getcwd())

os.chdir('E:\Games')
print(os.getcwd())

path = 'E:\Games\city\Tropico5'
os.chdir(path)
print(os.getcwd())