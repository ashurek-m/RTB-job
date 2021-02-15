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


start_time = time.time()
df_spektr = pd.read_excel('СПЕКТРОНУС.xlsx')
names_detals = df_spektr['обозначение'].unique()
names_detals_df = pd.DataFrame(names_detals, columns=['обозначение'])
new_names = names_detals_df.replace('АГ.01.01.07 ', 'АГ.01.01.07')
new_names.sort_values(by='обозначение')

# save_csv_header_w('уникальные_наименования_деталей.csv', new_names)
# csv_writer(names_detals, 'уникальные_наименования_деталей.csv')
print("--- %s seconds ---" % (time.time() - start_time))