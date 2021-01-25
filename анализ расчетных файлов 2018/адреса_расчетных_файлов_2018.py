import pandas as pd
import xlrd
import time
import os, glob, csv

def spisok_spiskov(data):
    new_list = []
    for i in range(len(data)):
       listys = [data[i]]
       new_list.append(listys)
    return new_list

def csv_writer(data, path):
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
        csv_file.close()

start_time = time.time()
csv1 = pd.read_csv(r"C:\Python's_project\RTB-job\address_file.csv", names=['path'])
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


print(len(clean_address))
print(f'открылось файлов {sum1}')
print(f'не открылось файлов из-за отсуствия листа расчет {sum2}')
print(f'не открылось по другой причине {sum3}')
print("--- %s seconds ---" % (time.time() - start_time))
path = "good_address_file.csv"
path1 = "error_address_file.csv"
print(type(good_list), type(csv))
csv_writer(spisok_spiskov(good_list), path)
csv_writer(spisok_spiskov(error_list), path1)
print("--- %s seconds ---" % (time.time() - start_time))