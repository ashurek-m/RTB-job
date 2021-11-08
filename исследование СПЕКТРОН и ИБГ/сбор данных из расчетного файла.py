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


def shape_62(address_file, number=62):
    counter = 0
    name_file_csv = 'shape_' + str(number) + 'csv'
    name_file_exel = 'shape_' + str(number) + 'xlsx'
    address_data = pd.read_csv(address_file, names=['path', 'order', 'shape'])
    address_data = address_data[address_data['shape'] == number].reset_index(drop=True)
    for i in range(address_data.shape[0]):
        payment_file = pd.read_excel(df[i], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=address_data.loc[i, 'order'])
        payment_file_1.dropna(subset=['Unnamed: 1'], inplace=True)
        if counter == 0:
            counter += 1
            payment_file_1.to_csv(name_file_csv, mode='w', encoding='utf-8', index=False, header=True)
        else:
            payment_file_1.to_csv(name_file_csv, mode='a', encoding='utf-8', index=False, header=False)
    save_excel = pd.read_csv(name_file_csv)
    writer = pd.ExcelWriter(name_file_exel, engine='xlsxwriter')
    save_excel.to_excel(writer, sheet_name='welcome', index=False)
    writer.save()


start_time = time.time()
runner = 60
if runner != 60:
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
    # Выводим на экран результат проверки True - все совподает, False - не совподает, необходимо определить что не
    # совподает
    print(output)

# Группируем расчетные файлы с одинаковым кол-вом столбоц в подгенеральныей файлы. Это делается из-за разного
# наименования столбов в файлах. Хотя можно было присвоить свои наименования столбов в каждом файле.

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

# Прочитаем подгенеральные планы и сведм их в один, нам нужен размер дата фрейма в 62 столбца
df_shape_62 = pd.read_excel('shape_62.xlsx', sheet_name='welcome')
df_shape_63 = pd.read_excel('shape_63.xlsx', sheet_name='welcome')
df_shape_64 = pd.read_excel('shape_64.xlsx', sheet_name='welcome')
df_shape_65 = pd.read_excel('shape_65.xlsx', sheet_name='welcome')
df_shape_66 = pd.read_excel('shape_66.xlsx', sheet_name='welcome')
df_shape_67 = pd.read_excel('shape_67.xlsx', sheet_name='welcome')

columns_for_excel = ['обозначение',
                     'наименование',
                     'индекс',
                     'коэф_входимости',
                     'заказанное_кол',
                     'уровень_критичности',
                     'примечания',
                     'наименование_материала',
                     'locmat_name',
                     'locmat',
                     'уд_вес',
                     'стоимость_мат_за_1кг_м',
                     'заг_диаметр',
                     'заг_толщина',
                     'заг_длина',
                     'заг_ширина',
                     'заг_на_кол_во',
                     'прутки',
                     'плиты',
                     'вес',
                     'стоимость_мат_ла',
                     'индустриализация_вид',
                     'индустриализация_стоимость',
                     'подряд_вид',
                     'подряд_стоимость',
                     'термообработка_вид',
                     'терообработка_стоимость',
                     'покрытие_площадь',
                     'покрытие_вид',
                     'покрытие_стоимость',
                     'резка_т_подг_мин',
                     'резка_т_маш_мин',
                     'резка_т_сум_ч',
                     'cn_т_подг_мин',
                     'cn_т_маш_мин',
                     'cn_т_сум_ч',
                     'dart_т_подг_мин',
                     'dart_т_маш_мин',
                     'dart_т_сум_ч',
                     'mx-cn_т_подг_мин',
                     'mx-cn_т_маш_мин',
                     'mx-cn_т_сум_ч',
                     'tour_т_подг_мин',
                     'tour_т_маш_мин',
                     'tour_т_сум_ч',
                     'mx\\dart-tour_т_подг_мин',
                     'mx\\dart-tour_т_ман_мин',
                     'mx\\dart-tour_т_сум_ч',
                     'финишная_т_подг_мин',
                     'финишная_т_маш_мин',
                     'финишная_т_сум_ч',
                     'слесарная_т_подг_мин',
                     'слесарная_т_маш_мин',
                     'слесарная_т_сум_ч',
                     'шлифовальная_т_подг_мин',
                     'шлифовальная_т_маш_мин',
                     'шлифовальная_т_сум_ч',
                     'резерв_т_подг_мин',
                     'резерв_т_маш_мин',
                     'резерв_т_сум_ч',
                     'т_партии_ч',
                     'номер_заказа']

save_csv_header_w('СПЕКТРОНУС.csv', df_shape_62)
save_csv_header_w('СПЕКТРОНУС.csv', df_shape_63, w_or_a='a')
columns_drop64 = ['Unnamed: 7', 'price']
df_shape_64.drop(columns_drop64, inplace=True, axis=1)
save_csv_header_w('СПЕКТРОНУС.csv', df_shape_64, w_or_a='a')
columns_drop65 = ['Unnamed: 33']
df_shape_65.drop(columns_drop65, inplace=True, axis=1)
save_csv_header_w('СПЕКТРОНУС.csv', df_shape_65, w_or_a='a')
save_csv_header_w('СПЕКТРОНУС.csv', df_shape_66, w_or_a='a')
columns_drop67 = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 35']
df_shape_67.drop(columns_drop67, inplace=True, axis=1)
save_csv_header_w('СПЕКТРОНУС.csv', df_shape_67, w_or_a='a')
spektronus = pd.read_csv('СПЕКТРОНУС.csv')
save_excel('СПЕКТРОНУС.xlsx', spektronus, columns=columns_for_excel)
print("--- %s seconds ---" % (time.time() - start_time))
