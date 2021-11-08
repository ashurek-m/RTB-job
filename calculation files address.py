import csv
import glob
import time


def csv_writer_spisok(data, path):
    new_list = []
    for i in range(len(data)):
        listys = [data[i]]
        new_list.append(listys)
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(new_list)
        csv_file.close()


start_time = time.time()
# encoding='utf-8'
way_list = glob.glob(
    'W:\\Department - External Economic\\ЗАКАЗЫ ВНУТРЕННИХ ПОТРЕБИТЕЛЕЙ\\Consultations RTB-2017\\**\\*.xlsx',
    recursive=True)
name = "C:\\Python's_project\\RTB-job\создание единого расчетного файла\\new_general_address_file(xlsx).csv"
csv_writer_spisok(way_list, name)
print("--- %s seconds ---" % (time.time() - start_time))
