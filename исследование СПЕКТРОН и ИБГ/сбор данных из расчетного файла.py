import pandas as pd
import time
import csv
import numpy as np


def csv_writer(data, path):
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer_csv = csv.writer(csv_file)
        writer_csv.writerows(data)
        csv_file.close()


start_time = time.time()
# Сделали список где содержится кол-во столбцов в расчетном файле
# Для того что бы рассортировать схожие файлы по конфигурации
address_file = pd.read_csv("Спектрон.csv", names=['path', 'order'])
df = address_file.loc[:, 'path']
df_order = address_file.loc[:, 'order']
shape_list = []
for i in range(len(df)):
    payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
    payment_file = payment_file.loc[:, 'Unnamed: 0': 'час']
    shape_list.append(payment_file.shape[1])
# Преобразовали список в датафрейм
df_shape = pd.DataFrame(data=shape_list, columns=['кол-во_столбцов'])
unique_shape = df_shape['кол-во_столбцов'].unique()
print(df_shape['кол-во_столбцов'].unique())
# Создаем список с названием столбцов для всех расчетных файлов с одинаковым кол-вом столбцов
# Сохраняем результат в csv файл для просмотра
# Рассматриваем пока конкретно по одному варианту
list_columns = []
for i in range(len(df)):
    payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
    payment_file = payment_file.loc[:, 'Unnamed: 0': 'час']
    x_shape = payment_file.shape[1]
    if x_shape == unique_shape[2]:
        print(df_order[i])
        list_columns.append(payment_file.columns)
csv_writer(list_columns, 'columns.csv')
# Из списка создаем матрицу и транспонируем ее.
matrix_a = np.array(list_columns)
matrix_b = np.transpose(matrix_a)
# Проверяем совподают ли наименования колонок в расчетных файлах с одинаковым кол-вом колонок
atr_s = 0
for i in range(matrix_b.shape[0]):
    atr_a = 0
    for j in range(matrix_b.shape[1] - 1):
        if matrix_b[i][j] == matrix_b[i][j + 1]:
            atr_a += 1
        else:
            print(f'строка = {i}, значение({matrix_b[i][j]}, {matrix_b[i][j + 1]})')
    if atr_a == matrix_b.shape[1] - 1:
        atr_s += 1
output = atr_s == matrix_b.shape[0]
# Выводим на экран результат проверки True - все совподает, False - не совподает, необходимо определить что не совподает
print(output)
counter = 0
runner = 65
if runner == 66:
    for i in range(len(df)):
        payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=df_order[i])
        x_shape = payment_file_1.shape[1]
        if x_shape == unique_shape[0]:
            columns_drop = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 10']
            payment_file_1.drop(columns_drop, inplace=True, axis=1)
            payment_file_1.dropna(subset=['Unnamed: 1'], inplace=True)
            if counter == 0:
                counter += 1
                payment_file_1.to_csv('file_zero.csv', mode='w', encoding='utf-8', index=False, header=True)
            else:
                payment_file_1.to_csv('file_zero.csv', mode='a', encoding='utf-8', index=False, header=False)
elif runner == 62:
    for i in range(len(df)):
        payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=df_order[i])
        x_shape = payment_file_1.shape[1]
        if x_shape == unique_shape[1]:
            payment_file_1.dropna(subset=['Unnamed: 1'], inplace=True)
            payment_file_1.to_csv('file_zero.csv', mode='a', encoding='utf-8', index=False, header=False)
elif runner == 65:
    for i in range(len(df)):
        payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=df_order[i])
        x_shape = payment_file_1.shape[1]
        if x_shape == unique_shape[2]:
            columns_drop = ['Unnamed: 7', 'Unnamed: 8']
            payment_file_1.drop(columns_drop, inplace=True, axis=1)
            payment_file_1.dropna(subset=['Unnamed: 1'], inplace=True)
            payment_file_1.to_csv('file_zero.csv', mode='a', encoding='utf-8', index=False, header=False)

save_excel = pd.read_csv('file_zero.csv', names=['Unnamed: 1',
                                                 'Unnamed: 1.1',
                                                 'Unnamed: 1.2',
                                                 'Unnamed: 2',
                                                 'Unnamed: 3',
                                                 '1',
                                                 '1.1',
                                                 'Unnamed: 6',
                                                 'Unnamed: 9',
                                                 'Unnamed: 10',
                                                 'Материалы!A1',
                                                 'Unnamed: 12',
                                                 'г/см3',
                                                 '$',
                                                 'мм',
                                                 'мм.1',
                                                 'мм.2',
                                                 'мм.3',
                                                 'шт,м',
                                                 'м2',
                                                 'кг',
                                                 '$.1',
                                                 'Unnamed: 24',
                                                 'Unnamed: 25',
                                                 'Unnamed: 26',
                                                 'Unnamed: 27',
                                                 'Unnamed: 28',
                                                 '3',
                                                 'm2',
                                                 'Unnamed: 31',
                                                 '50',
                                                 'price',
                                                 "Т подг, мин",
                                                 "Т маш, мин",
                                                 "Т сум, ч",
                                                 "Т подг, мин.1",
                                                 "Т маш, мин.1",
                                                 "Т сум, ч.1",
                                                 "Т подг, мин.2",
                                                 "Т маш, мин.2",
                                                 "Т сум, ч.2",
                                                 "Т подг, мин.3",
                                                 "Т маш, мин.3",
                                                 "Т сум, ч.3",
                                                 "Т подг, мин.4",
                                                 "Т маш, мин.4",
                                                 "Т сум, ч.4",
                                                 "Т подг, мин.5",
                                                 "Т маш, мин.5",
                                                 "Т сум, ч.5",
                                                 "Т подг, мин.6",
                                                 "Т маш, мин.6",
                                                 "Т сум, ч.6",
                                                 "Т подг, мин.7",
                                                 "Т маш, мин.7",
                                                 "Т сум, ч.7",
                                                 "Т подг, мин.8",
                                                 "Т маш, мин.8",
                                                 "Т сум, ч.8",
                                                 "Т подг, мин.9",
                                                 "Т маш, мин.9",
                                                 "Т сум, ч.9",
                                                 'час'
                                                 ])
writer = pd.ExcelWriter('file_zero.xlsx', engine='xlsxwriter')
save_excel.to_excel(writer, sheet_name='welcome', index=False)
writer.save()


print("--- %s seconds ---" % (time.time() - start_time))
