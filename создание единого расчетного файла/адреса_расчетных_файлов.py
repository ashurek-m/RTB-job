import pandas as pd
import xlrd
import time
import csv


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
csv1 = pd.read_csv("C:\\Python's_project\\RTB-job\\создание единого расчетного файла\\new_general_address_file2019("
                   "xls).csv", names=['path'])
clean_address = csv1.loc[:, 'path']
sum1 = 0
sum2 = 0
sum3 = 0
error_list = []
good_list = []
for i in range(len(clean_address)):
    try:
        way = str(clean_address[i])
        df = pd.read_excel(way, sheet_name='расчет')
        sum1 += 1
        good_list.append(clean_address[i])
    except xlrd.biffh.XLRDError:
        error_list.append(clean_address[i])
        sum2 += 1
        continue
    except PermissionError:
        error_list.append(clean_address[i])
        sum3 += 1
        continue
    except KeyError:
        error_list.append(clean_address[i])
        sum2 += 1
        continue
    except ValueError:
        error_list.append(clean_address[i])
        sum3 += 1
        continue


print(len(clean_address))
print(f'открылось файлов {sum1}')
print(f'не открылось файлов из-за отсуствия листа расчет {sum2}')
print(f'не открылось по другой причине {sum3}')
names = "C:\\Python's_project\\RTB-job\\создание единого расчетного файла\\good_file2019(xls).csv"
csv_writer_spisok(good_list, names)
print("--- %s seconds ---" % (time.time() - start_time))
