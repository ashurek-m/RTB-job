import os, glob, csv

def spisok_spiskov(data):
    new_list = []
    for i in range(len(data)):
       listys = [data[i]]
       new_list.append(listys)
    return new_list

def csv_writer(data, path):
    """
    Write data to a CSV file path
    """
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        writer.writerows(data)
        csv_file.close()

#encoding='utf-8'
way_list = glob.glob('W:\Department - External Economic\ЗАКАЗЫ ВНУТРЕННИХ ПОТРЕБИТЕЛЕЙ\Consultations RTB-2018\**\*.xls', recursive=True)
path = 'address_file.csv'

csv_writer(spisok_spiskov(way_list), path)

