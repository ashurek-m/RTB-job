import pandas as pd
import time, csv
import xlrd

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
material = pd.read_csv("info_mat.csv")
locmat = pd.read_excel("Копия справочник материалов LOCMAT.xls",
                       sheet_name='locmat')
print(material.duplicated(subset='наименование_материала').sum())
print(len(material['наименование_материала'].unique()))
#ynic = material['наименование_материала'].unique()
#path = 'уникальные_наименования_материалов.csv'
#csv_writer(spisok_spiskov(ynic), path)

print("--- %s seconds ---" % (time.time() - start_time))