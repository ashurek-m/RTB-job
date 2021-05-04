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
