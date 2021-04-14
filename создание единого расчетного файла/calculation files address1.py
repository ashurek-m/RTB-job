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
# way_list_xls = glob.glob(
    # 'W:\\Theoretical Planning\\02 - Бланки заказов (All foto cmd)\\**\\*.xls',
    # recursive=True)
# name = "C:\\Python's_project\\RTB-job\создание единого расчетного файла\\new_general_address_file2021(xls).csv"
# csv_writer_spisok(way_list_xls, name)
way_list_xlsx = glob.glob(
    'W:\\Theoretical Planning\\02 - Бланки заказов (All foto cmd)\\**\\*.xlsx',
    recursive=True)
name = "C:\\Python's_project\\RTB-job\создание единого расчетного файла\\new_general_address_file2021(xlsx).csv"
csv_writer_spisok(way_list_xlsx, name)
print("--- %s seconds ---" % (time.time() - start_time))
