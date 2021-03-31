import pandas as pd
import time
import csv


def csv_writer(data, path):
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer_csv = csv.writer(csv_file)
        writer_csv.writerows(data)
        csv_file.close()


def csv_writer_spisok(data, path):
    new_list = []
    for i in range(len(data)):
        listys = [data[i]]
        new_list.append(listys)
    with open(path, "w", encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(new_list)
        csv_file.close()


def save_excel(path, data_frame, columns):
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
    name = 'address_and_order' + '.csv'
    csv_writer(address_file_client, name)


def list_shape_fyn(list_addres):
    df_data = pd.read_csv(list_addres, names=['path', 'order'])
    df_data = df_data[df_data['order'] < 40000].reset_index(drop=True)
    df_data_addres = df_data.loc[:, 'path']
    shape_list_2 = []
    error_list = []
    not_found_list = []
    for i in range(len(df_data_addres)):
        try:
            shape_list_1 = []
            df_file = pd.read_excel(str(df_data_addres[i]), sheet_name='расчет', header=13)
            df_file = df_file.loc[:, 'Unnamed: 0': 'час']
            shape_list_1.append(df_data_addres[i])
            shape_list_1.append(df_data.loc[i, 'order'])
            shape_list_1.append(df_file.shape[1])
            shape_list_2.append(shape_list_1)
        except KeyError:
            error_list.append(df_data_addres[i])
            continue
        except FileNotFoundError:
            not_found_list.append(df_data_addres[i])
            continue
    csv_writer_spisok(error_list, 'странные файлы.csv')
    csv_writer_spisok(not_found_list, 'нет файлов.csv')
    csv_writer(shape_list_2, 'открылись.csv')


def shape_62(address_file, number=62):
    counter = 0
    name_file_csv = 'shape_' + str(number) + '.csv'
    name_file_exel = 'shape_' + str(number) + '.xlsx'
    address_data = pd.read_csv(address_file, names=['path', 'order', 'shape'])
    address_data = address_data[address_data['shape'] == number].reset_index(drop=True)
    for i in range(address_data.shape[0]):
        payment_file = pd.read_excel(address_data.loc[i, 'path'], sheet_name='расчет', header=13)
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


def shape_63(address_file, number=63):
    counter = 0
    name_file_csv = 'shape_' + str(number) + '.csv'
    name_file_exel = 'shape_' + str(number) + '.xlsx'
    address_data = pd.read_csv(address_file, names=['path', 'order', 'shape'])
    address_data = address_data[address_data['shape'] == number].reset_index(drop=True)
    for i in range(address_data.shape[0]):
        payment_file = pd.read_excel(address_data.loc[i, 'path'], sheet_name='расчет', header=13)
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


def shape_64(address_file, number=64):
    counter = 0
    name_file_csv = 'shape_' + str(number) + '.csv'
    name_file_exel = 'shape_' + str(number) + '.xlsx'
    address_data = pd.read_csv(address_file, names=['path', 'order', 'shape'])
    address_data = address_data[address_data['shape'] == number].reset_index(drop=True)
    for i in range(address_data.shape[0]):
        payment_file = pd.read_excel(address_data.loc[i, 'path'], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=address_data.loc[i, 'order'])
        # columns_drop = ['Unnamed: 7', 'price']
        # payment_file_1.drop(columns_drop, inplace=True, axis=1)
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


def shape_65(address_file, number=65):
    counter = 0
    name_file_csv = 'shape_' + str(number) + '.csv'
    name_file_exel = 'shape_' + str(number) + '.xlsx'
    address_data = pd.read_csv(address_file, names=['path', 'order', 'shape'])
    address_data = address_data[address_data['shape'] == number].reset_index(drop=True)
    for i in range(address_data.shape[0]):
        payment_file = pd.read_excel(address_data.loc[i, 'path'], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=address_data.loc[i, 'order'])
        # columns_drop = ['Unnamed: 7', 'Unnamed: 8', 'Unnamed: 33']
        # payment_file_1.drop(columns_drop, inplace=True, axis=1)
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


def shape_66(address_file, number=66):
    counter = 0
    name_file_csv = 'shape_' + str(number) + '.csv'
    name_file_exel = 'shape_' + str(number) + '.xlsx'
    address_data = pd.read_csv(address_file, names=['path', 'order', 'shape'])
    address_data = address_data[address_data['shape'] == number].reset_index(drop=True)
    for i in range(address_data.shape[0]):
        payment_file = pd.read_excel(address_data.loc[i, 'path'], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=address_data.loc[i, 'order'])
        # columns_drop = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 10']
        # payment_file_1.drop(columns_drop, inplace=True, axis=1)
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


def shape_67(address_file, number=67):
    counter = 0
    name_file_csv = 'shape_' + str(number) + '.csv'
    name_file_exel = 'shape_' + str(number) + '.xlsx'
    address_data = pd.read_csv(address_file, names=['path', 'order', 'shape'])
    address_data = address_data[address_data['shape'] == number].reset_index(drop=True)
    for i in range(address_data.shape[0]):
        payment_file = pd.read_excel(address_data.loc[i, 'path'], sheet_name='расчет', header=13)
        payment_file_1 = payment_file.loc[:, 'Unnamed: 1': 'час']
        payment_file_1 = payment_file_1.assign(order=address_data.loc[i, 'order'])
        # columns_drop = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 10', 'Unnamed: 35']
        # payment_file_1.drop(columns_drop, inplace=True, axis=1)
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

# search_by_numder_order('good_file2020(xls).csv')
# list_shape_fyn('address_and_order.csv')
df = pd.read_csv('открылись.csv', names=['path', 'order', 'shape'])
list_shape = df['shape'].unique()
print(list_shape)
# shape_62('открылись.csv')
# shape_63('открылись.csv')
# shape_64('открылись.csv')
# shape_65('открылись.csv')
# shape_66('открылись.csv')
# shape_67('открылись.csv')

df_shape_62 = pd.read_csv('shape_62.csv')
df_shape_63 = pd.read_csv('shape_63.csv')
df_shape_64 = pd.read_csv('shape_64.csv')
df_shape_65 = pd.read_csv('shape_65.csv')
# df_shape_66 = pd.read_csv('shape_66.csv')
# df_shape_67 = pd.read_csv('shape_67.csv')
# df_shape_68 = pd.read_csv('shape_68.csv')

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
print(len(columns_for_excel))

save_csv_header_w('united_pay_file_2020.csv', df_shape_62, columns=False)
columns_drop63 = ['price, $']
df_shape_63.drop(columns_drop63, inplace=True, axis=1)
save_csv_header_w('united_pay_file_2020.csv', df_shape_63, columns=False, w_or_a='a')
columns_drop64 = ['Unnamed: 7', 'price, $']
df_shape_64.drop(columns_drop64, inplace=True, axis=1)
save_csv_header_w('united_pay_file_2020.csv', df_shape_64, columns=False, w_or_a='a')
columns_drop65 = ['..\..\..\Department - Quality\Metrology\Calibers', 'Unnamed: 27', 'price, $']
df_shape_65.drop(columns_drop65, inplace=True, axis=1)
save_csv_header_w('united_pay_file.csv', df_shape_65, columns=False, w_or_a='a')
# columns_drop66 = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 10']
# df_shape_66.drop(columns_drop66, inplace=True, axis=1)
# save_csv_header_w('united_pay_file.csv', df_shape_66, columns=False, w_or_a='a')
# columns_drop67 = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 10', 'Unnamed: 35']
# df_shape_67.drop(columns_drop67, inplace=True, axis=1)
# save_csv_header_w('united_pay_file.csv', df_shape_67, columns=False, w_or_a='a')
# columns_drop68 = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 10', 'Unnamed: 27', '$.2']
# df_shape_68.drop(columns_drop68, inplace=True, axis=1)
# save_csv_header_w('united_pay_file_2020.csv', df_shape_68, columns=False, w_or_a='a')
print('next')
input()
df_united = pd.read_csv('united_pay_file_2020.csv')
save_excel('united_pay_file_2020.xlsx', df_united, columns_for_excel)
print("--- %s seconds ---" % (time.time() - start_time))
