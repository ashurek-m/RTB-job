import pandas as pd
import time
import csv
import numpy as np


def csv_writer(data, path):
    new_list = []
    for i in range(len(data)):
        listys = [data[i]]
        new_list.append(listys)
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(new_list)
        csv_file.close()


def save_csv_header_w(path, data_frame, columns=True, w_or_a='w'):
    data_frame.to_csv(path, mode=w_or_a, encoding='utf-8', index=False, header=columns)


def save_excel(path, data_frame, columns=True):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False, header=columns)
    writer_on.save()


start_time = time.time()
df_spektr = pd.read_excel('СПЕКТРОНУС.xlsx')
df_spektr = df_spektr.replace('АГ.01.01.07 ', 'АГ.01.01.07')
df_spektr = df_spektr.replace('АГ.02.01.07 ', 'АГ.02.01.07')
df_spektr = df_spektr.replace('АГ.02.01.08M ', 'АГ.02.01.08M')
df_spektr = df_spektr.replace('РА1.040.002M', 'РА1.040.002М')
df_spektr = df_spektr.replace('РА1.040.009 M', 'РА1.040.009М')
df_spektr = df_spektr.replace('РА1.040.020 ', 'РА1.040.020')
df_spektr = df_spektr.replace('РА1.040.021 М2', 'РА1.040.021М2')
df_spektr = df_spektr.replace('РА1.040.021M2', 'РА1.040.021М2')
df_spektr = df_spektr.replace('РА7.200.011 - 01', 'РА7.200.011-01')
df_spektr = df_spektr.replace('РА7.200.012 - 03', 'РА7.200.012-03')
df_spektr = df_spektr.replace('СДТ1.040.301 ', 'СДТ1.040.304')
df_spektr = df_spektr.replace('ЭЛ 4.00.002 ', 'ЭЛ4.00.002')

df_spektr.drop_duplicates().reset_index(drop=True)
detali_list = df_spektr['обозначение'].unique()

one_detal = df_spektr[df_spektr['обозначение'] == detali_list[200]]
one_detal = one_detal.sort_values(by='номер_заказа')
first_order = one_detal['номер_заказа'].min()
extreme_order = one_detal['номер_заказа'].max()
df_first_order = one_detal[one_detal['номер_заказа'] == first_order]
df_extreme_order = one_detal[one_detal['номер_заказа'] == extreme_order]
#time_relation_cn_podg = (df_extreme_order.loc[0, 'cn_т_подг_мин']) / (df_first_order.loc[0, 'cn_т_подг_мин'])
print(one_detal)
print(first_order, extreme_order)
print(df_extreme_order.loc[:, 'cn_т_подг_мин'], df_first_order.loc[:, 'cn_т_подг_мин'])
# print(time_relation_cn_podg)
print("--- %s seconds ---" % (time.time() - start_time))
