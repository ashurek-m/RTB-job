import pandas as pd
import time
import csv
import numpy as np


def csv_writer(data, path):
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer_csv = csv.writer(csv_file)
        writer_csv.writerows(data)
        csv_file.close()


def save_excel(path, data_frame, columns=True):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False, header=columns)
    writer_on.save()


def save_csv_header_w(path, data_frame, columns=True, w_or_a='w'):
    data_frame.to_csv(path, mode=w_or_a, encoding='utf-8', index=False, header=columns)


def search_by_numder_order(address_file):
    file_csv = pd.read_csv(address_file, names=['path'])
    address_file_client = []
    file = file_csv.loc[:, 'path']
    for i in range(len(file)):
        file_adrress_client = []
        name_file = file[i].split("\\")
        try:
            num_order = int(name_file[-1][:5])
            file_adrress_client.append(file[i])
            file_adrress_client.append(num_order)
            address_file_client.append(file_adrress_client)
        except ValueError:
            continue
    path = 'addres_and_order' + '.csv'
    csv_writer(address_file_client, path)


def list_shape_fyn(list_addres):
    shape_list_ = []
    for i in range(len(list_addres)):
        df_file = pd.read_excel(str(list_addres[i]), sheet_name='расчет', header=13)
        df_file = df_file.loc[:, 'Unnamed: 0': 'час']
        shape_ = df_file.shape()
        shape_list_.append(shape_[1])
    return shape_list_


start_time = time.time()
# search_by_numder_order('good_address_file1.csv')
df = pd.read_csv('addres_and_order.csv', names=['path', 'order'])
df_addres = df.loc[:, 'path']

print("--- %s seconds ---" % (time.time() - start_time))
