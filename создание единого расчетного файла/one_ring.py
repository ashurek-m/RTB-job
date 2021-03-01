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


start_time = time.time()
# search_by_numder_order('good_file.csv')
shape_list = list_shape_fyn('address_and_order.csv')
df_data = pd.read_csv('addres_and_order.csv', names=['path', 'order'])
df_data_addres = df_data.loc[:, 'path']
print(len(df_data_addres))
j = 4073
list_error = []
for i in range(4073, len(df_data_addres), 1):
    if df_data.loc[i, 'order'] == 36685:
        df_file = pd.read_excel(str(df_data_addres[i]), sheet_name='расчет', header=13)
        df_file.info()
        list_error.append(df_data_addres[i])
        print(df_file.shape, df_data.loc[i, 'order'], j)
        j += 1
    elif df_data.loc[i, 'order'] == 38063:
        list_error.append(df_data_addres[i])
        print(0, df_data.loc[i, 'order'], j)
        j += 1
    elif df_data.loc[i, 'order'] == 38579:
        list_error.append(df_data_addres[i])
        print(0, df_data.loc[i, 'order'], j)
        j += 1
    elif df_data.loc[i, 'order'] == 39271:
        list_error.append(df_data_addres[i])
        print(0, df_data.loc[i, 'order'], j)
        j += 1
    elif df_data.loc[i, 'order'] == 39291:
        list_error.append(df_data_addres[i])
        print(0, df_data.loc[i, 'order'], j)
        j += 1
    elif df_data.loc[i, 'order'] == 39337:
        list_error.append(df_data_addres[i])
        print(0, df_data.loc[i, 'order'], j)
        j += 1
    elif df_data.loc[i, 'order'] == 39339:
        list_error.append(df_data_addres[i])
        print(0, df_data.loc[i, 'order'], j)
        j += 1
    elif df_data.loc[i, 'order'] == 60471:
        list_error.append(df_data_addres[i])
        print(0, df_data.loc[i, 'order'], j)
        j += 1
    elif df_data.loc[i, 'order'] == 60472:
        list_error.append(df_data_addres[i])
        print(0, df_data.loc[i, 'order'], j)
        j += 1
    else:
        df_file = pd.read_excel(str(df_data_addres[i]), sheet_name='расчет', header=13)
        df_file = df_file.loc[:, 'Unnamed: 0': 'час']
        print(df_file.shape, df_data.loc[i, 'order'], j)
        j += 1

print("--- %s seconds ---" % (time.time() - start_time))
