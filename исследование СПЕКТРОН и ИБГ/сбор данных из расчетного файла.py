import pandas as pd
import time
import csv
import numpy as np


def csv_writer(data, path):
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(data)
        csv_file.close()


start_time = time.time()
address_file = pd.read_csv("Спектрон.csv", names=['path', 'order'])
df = address_file.loc[:, 'path']
shape_list = []
for i in range(len(df)):
    payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
    shape_list.append(payment_file.shape[1])

df_shape = pd.DataFrame(data=shape_list, columns=['кол-во_столбцов'])

list_columns = []
for i in range(len(df)):
    payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
    x_shape = payment_file.shape[1]
    if x_shape == shape_list[0]:
        list_columns.append(payment_file.columns)
csv_writer(list_columns, 'columns.csv')

matrix_a = np.array(list_columns)
matrix_b = np.transpose(matrix_a)
atr_s = 0
for i in range(matrix_b.shape[0]):
    atr_a = 0
    for j in range(matrix_b.shape[1] - 1):
        if matrix_b[i][j] == matrix_b[i][j + 1]:
            atr_a += 1
    if atr_a == matrix_b.shape[1] - 1:
        atr_s += 1
print(atr_s == matrix_b.shape[0])
print("--- %s seconds ---" % (time.time() - start_time))
