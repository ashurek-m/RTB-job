import csv
import glob
import time
import pandas as pd


def csv_writer_spisok(data, path):
    new_list = []
    for i in range(len(data)):
        listys = [data[i]]
        new_list.append(listys)
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(new_list)
        csv_file.close()


def csv_reader(file_obj):
    """
    Read a csv file
    """
    reader = csv.reader(file_obj)
    for row in reader:
        print(" ".join(row))


start_time = time.time()
'''
# encoding = 'utf-8'
way_list_xls = glob.glob(
    'W:\\Theoretical Planning\\02 - Бланки заказов (All foto cmd)\\**\\*.xls',
    recursive=True)
name = "C:\\Python's_project\\RTB-job\создание единого расчетного файла\\new22_general_address_file2021(xls).csv"
csv_writer_spisok(way_list_xls, name)

way_list_xlsx = glob.glob(
    'W:\\Theoretical Planning\\02 - Бланки заказов (All foto cmd)\\**\\*.xlsx',
    recursive=True)
name = "C:\\Python's_project\\RTB-job\создание единого расчетного файла\\new_general_address_file2021(xlsx).csv"
csv_writer_spisok(way_list_xlsx, name)
'''
df_new = pd.read_csv("C:\\Python's_project\\RTB-job\создание единого расчетного файла\\new22_general_address_file2021(xls).csv", names=['path'])
df_old = pd.read_csv("C:\\Python's_project\\RTB-job\создание единого расчетного файла\\new_general_address_file2021(xls).csv", names=['path'])

new = df_new.loc[:, 'path']
old = df_old.loc[:, 'path']
print(len(new), len(old))
new_set = set(new)
old_set = set(old)
new_set.symmetric_difference_update(old_set)
new_list = list(new_set)
print(len(new_list))


print("--- %s seconds ---" % (time.time() - start_time))
