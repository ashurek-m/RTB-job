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
    if x_shape == unique_shape[5]:
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
runner = 60
if runner == 66:
    counter = 0
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
                payment_file_1.to_csv('shape_66.csv', mode='w', encoding='utf-8', index=False, header=True)
            else:
                payment_file_1.to_csv('shape_66.csv', mode='a', encoding='utf-8', index=False, header=False)
    save_excel = pd.read_csv('shape_66.csv')
    writer = pd.ExcelWriter('shape_66.xlsx', engine='xlsxwriter')
    save_excel.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()
elif runner == 62:
    counter = 0
    for i in range(len(df)):
        payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=df_order[i])
        x_shape = payment_file_1.shape[1]
        if x_shape == unique_shape[1]:
            payment_file_1.dropna(subset=['Unnamed: 1'], inplace=True)
            if counter == 0:
                counter += 1
                payment_file_1.to_csv('shape_62.csv', mode='w', encoding='utf-8', index=False, header=True)
            else:
                payment_file_1.to_csv('shape_62.csv', mode='a', encoding='utf-8', index=False, header=False)
    save_excel = pd.read_csv('shape_62.csv')
    writer = pd.ExcelWriter('shape_62.xlsx', engine='xlsxwriter')
    save_excel.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()
elif runner == 65:
    counter = 0
    for i in range(len(df)):
        payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=df_order[i])
        x_shape = payment_file_1.shape[1]
        if x_shape == unique_shape[2]:
            columns_drop = ['Unnamed: 7', 'Unnamed: 8']
            payment_file_1.drop(columns_drop, inplace=True, axis=1)
            payment_file_1.dropna(subset=['Unnamed: 1'], inplace=True)
            if counter == 0:
                counter += 1
                payment_file_1.to_csv('shape_65.csv', mode='w', encoding='utf-8', index=False, header=True)
            else:
                payment_file_1.to_csv('shape_65.csv', mode='a', encoding='utf-8', index=False, header=False)
    save_excel = pd.read_csv('shape_65.csv')
    writer = pd.ExcelWriter('shape_65.xlsx', engine='xlsxwriter')
    save_excel.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()
elif runner == 67:
    counter = 0
    for i in range(len(df)):
        payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=df_order[i])
        x_shape = payment_file_1.shape[1]
        if x_shape == unique_shape[3]:
            columns_drop = ['Unnamed: 10']
            payment_file_1.drop(columns_drop, inplace=True, axis=1)
            payment_file_1.dropna(subset=['Unnamed: 1'], inplace=True)
            if counter == 0:
                counter += 1
                payment_file_1.to_csv('shape_67.csv', mode='w', encoding='utf-8', index=False, header=True)
            else:
                payment_file_1.to_csv('shape_67.csv', mode='a', encoding='utf-8', index=False, header=False)
    save_excel = pd.read_csv('shape_67.csv')
    writer = pd.ExcelWriter('shape_67.xlsx', engine='xlsxwriter')
    save_excel.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()
elif runner == 64:
    counter = 0
    for i in range(len(df)):
        payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=df_order[i])
        x_shape = payment_file_1.shape[1]
        if x_shape == unique_shape[4]:
            payment_file_1.dropna(subset=['Unnamed: 1'], inplace=True)
            if counter == 0:
                counter += 1
                payment_file_1.to_csv('shape_64.csv', mode='w', encoding='utf-8', index=False, header=True)
            else:
                payment_file_1.to_csv('shape_64.csv', mode='a', encoding='utf-8', index=False, header=False)
    save_excel = pd.read_csv('shape_64.csv')
    writer = pd.ExcelWriter('shape_64.xlsx', engine='xlsxwriter')
    save_excel.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()
elif runner == 63:
    counter = 0
    for i in range(len(df)):
        payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=df_order[i])
        x_shape = payment_file_1.shape[1]
        if x_shape == unique_shape[5]:
            columns_drop = ['price']
            payment_file_1.drop(columns_drop, inplace=True, axis=1)
            payment_file_1.dropna(subset=['Unnamed: 1'], inplace=True)
            if counter == 0:
                counter += 1
                payment_file_1.to_csv('shape_63.csv', mode='w', encoding='utf-8', index=False, header=True)
            else:
                payment_file_1.to_csv('shape_63.csv', mode='a', encoding='utf-8', index=False, header=False)
    save_excel = pd.read_csv('shape_63.csv')
    writer = pd.ExcelWriter('shape_63.xlsx', engine='xlsxwriter')
    save_excel.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()

print("--- %s seconds ---" % (time.time() - start_time))
