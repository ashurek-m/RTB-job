import pandas as pd
import step_1 as s1


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
            #print(df_data.loc[i, 'order'])
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

    s1.csv_writer_spisok(error_list, 'странные файлы.csv')
    s1.csv_writer_spisok(not_found_list, 'нет файлов.csv')
    s1.csv_writer(shape_list_2, 'открылись.csv')
    return 'открылись.csv'


def analysis(data_file):
    df = pd.read_csv(data_file, names=['path', 'order', 'shape'])
    list_shape = df['shape'].unique()
    list_shape.sort()
    # print(list_shape)
    return list_shape


def save_excel(path, data_frame, columns):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False, header=columns)
    writer_on.save()


def shape_(address_file, number):
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
    save_excel.to_excel(writer, sheet_name='расчет', index=False)
    writer.save()
    return name_file_csv


def shape_podr(address_file, number):
    counter = 0
    name_file_csv = 'shape_' + str(number) + '.csv'
    name_file_exel = 'shape_' + str(number) + '.xlsx'
    address_data = pd.read_csv(address_file, names=['path', 'order', 'shape'])
    address_data = address_data[address_data['shape'] == number].reset_index(drop=True)
    for i in range(address_data.shape[0]):
        payment_file = pd.read_excel(address_data.loc[i, 'path'], sheet_name='расчет', header=12)
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
    save_excel.to_excel(writer, sheet_name='расчет', index=False)
    writer.save()
    return name_file_csv