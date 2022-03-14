import csv
import glob
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


def csv_writer(data, path):
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
        csv_file.close()


def file_search(way, name):
    way_list_xls = glob.glob(way, recursive=True)
    name_ = name
    csv_writer_spisok(way_list_xls, name_)
    '''
    way_list_xlsx = glob.glob(
        'W:\\Theoretical Planning\\02 - Бланки заказов (All foto cmd)\\**\\*.xlsx',
        recursive=True)
    name1 = "C:\\Python's_project\\RTB-job\\отгрузочные часы\\new_general_address_file2022(xlsx).csv"
    csv_writer_spisok(way_list_xlsx, name1)
    '''
    return [name, 'new_general_address_file2022(xlsx).csv']


def search_by_client(address_file, year):
    file_csv = pd.read_csv(address_file, names=['path'])
    address_file_client = []
    file = file_csv.loc[:, 'path']
    for i in range(len(file)):
        file_adrress_client = []
        name_file = file[i].split("\\")
        try:
            if not 'рхив' in name_file[-2]:
                num_order = int(name_file[-1][:5])
                file_adrress_client.append(file[i])
                file_adrress_client.append(num_order)
                address_file_client.append(file_adrress_client)
        except ValueError:
            continue
    name = 'address_and_order_' + str(year) + '.csv'
    csv_writer(address_file_client, name)
    return name
