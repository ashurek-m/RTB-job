import os

print(os.getcwd())
list_dir = os.listdir(path=".")

for i in range(len(list_dir)):
    print(list_dir[i])

os.chdir(r"W:\Department - External Economic\ЗАКАЗЫ ВНУТРЕННИХ ПОТРЕБИТЕЛЕЙ\Consultations RTB-2018")
print(os.getcwd())
list_dir = os.listdir(path=".")

order_list = []
for i in range(len(list_dir)):
    if list_dir[i][0:5].isdigit():
        order_list.append({
            'numder_order': list_dir[i][0:5],
            'full_name': list_dir[i],
            'directory_path': "W:\Department - External Economic\ЗАКАЗЫ ВНУТРЕННИХ ПОТРЕБИТЕЛЕЙ\Consultations RTB-2018\\" + list_dir[i] ,
        })
    # print(list_dir[i].isdigit())

print(order_list[0]['directory_path'])
print('W:\\Department - External Economic\\ЗАКАЗЫ ВНУТРЕННИХ ПОТРЕБИТЕЛЕЙ\\Consultations RTB-2018\\36885 - Унитехпром БГУ')
os.chdir(r'W:\\Department - External Economic\\ЗАКАЗЫ ВНУТРЕННИХ ПОТРЕБИТЕЛЕЙ\\Consultations RTB-2018\\36885 - Унитехпром БГУ')
print('N ',os.getcwd())