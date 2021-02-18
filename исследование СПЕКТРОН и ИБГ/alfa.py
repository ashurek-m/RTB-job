import pandas as pd
import time
import csv


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
# Подготовка данных
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
df_spektr = df_spektr.fillna(0)
df_spektr.drop_duplicates().reset_index(drop=True)
df_spektr = df_spektr.assign(t_prepa=lambda x: x['cn_т_подг_мин'] + x['dart_т_подг_мин'] + x['tour_т_подг_мин'])
df_spektr = df_spektr.assign(t_cutting=lambda x: x['cn_т_маш_мин'] + x['dart_т_маш_мин'] + x['tour_т_маш_мин'])
# Анализ данных
detali_list = df_spektr['обозначение'].unique()
for i in range(len(detali_list)):
    one_detal = df_spektr[df_spektr['обозначение'] == detali_list[i]]
    one_detal = one_detal.sort_values(by='номер_заказа')
    one_detal = one_detal.loc[:, 'номер_заказа': 't_cutting']
    first_order = one_detal['номер_заказа'].min()
    extreme_order = one_detal['номер_заказа'].max()
    df_first_order = one_detal[one_detal['номер_заказа'] == first_order].reset_index(drop=True)
    df_extreme_order = one_detal[one_detal['номер_заказа'] == extreme_order].reset_index(drop=True)
    first_change_cutting = df_first_order.loc[0, 't_cutting']
    second_change_cutting = df_extreme_order.loc[0, 't_cutting']
    first_change_prepa = df_first_order.loc[0, 't_prepa']
    second_change_prepa = df_extreme_order.loc[0, 't_prepa']
    if first_change_cutting != 0:
        connection_cutting = second_change_cutting / first_change_cutting
    else:
        connection_cutting = 0
    if first_change_prepa != 0:
        connection_prepa = second_change_prepa / first_change_prepa
    else:
        connection_prepa = 0
    if connection_prepa < 1 or connection_cutting < 1:
        print('{:.1%}, {:.1%}'.format(connection_prepa, connection_cutting))
print("--- %s seconds ---" % (time.time() - start_time))
