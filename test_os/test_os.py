import os, glob,csv

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "a", newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in data:
            writer.writerow(line)
        csv_file.close()

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
        })
    # print(list_dir[i].isdigit())

way_list = glob.glob('W:\Department - External Economic\ЗАКАЗЫ ВНУТРЕННИХ ПОТРЕБИТЕЛЕЙ\Consultations RTB-2018\**\*.xls', recursive=True)

