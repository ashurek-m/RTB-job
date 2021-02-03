import pandas as pd
import time, csv


def csv_writer(data, path):
    new_list = []
    for i in range(len(data)):
        listys = [data[i]]
        new_list.append(listys)
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(new_list)
        csv_file.close()


start_time = time.time()
csv1 = pd.read_csv("good_address_file.csv", names=['path'])
name_list = []
order_number = []
file = csv1.loc[:, 'path']
for i in range(len(file)):
    if 'IBG' in file[i]:
        name_file = file[i].split("\\")
        name_list.append(name_file)
        order_number.append(name_file[-1][:5])

print(name_list[0])
print(order_number[0])