import pandas as pd
import time


def append_in_list(k, data, data_pay):
    link_table_1 = []
    if data.shape[0] > 0:
        link_table_1.append(data.loc[0, 'N° ITEM'])
        link_table_1.append(data.loc[0, 'N°CMD'])
        link_table_1.append(data.loc[0, 'PRODUIT'])
        link_table_1.append(str(int(data.loc[0, 'N°PIECE'])))
        link_table_1.append(data.loc[0, 'IND PROD'])
        link_table_1.append(data.loc[0, 'REF_BAAN'])
        link_table_1.append(data_pay.loc[k, 'full_cod1'])
        link_table_1.append(data_pay.loc[k, 'обозначение'])
        link_table_1.append(data_pay.loc[k, 'номер_заказа'])
        return link_table_1
    else:
        for g in range(6):
            link_table_1.append(0)
        link_table_1.append(data_pay.loc[k, 'full_cod1'])
        link_table_1.append(data_pay.loc[k, 'обозначение'])
        link_table_1.append(data_pay.loc[k, 'номер_заказа'])
        return link_table_1


def filter_link(k, data, data_pay):
    df_filter_table_1 = data[data['N°CMD'] == data_pay.loc[k, 'номер_заказа']]
    df_filter_table_2 = df_filter_table_1[df_filter_table_1['full_cod3'] == data_pay.loc[k, 'full_cod1']].reset_index(
        drop=True)
    return df_filter_table_2


def save_csv_header_w(path, data_frame, columns=True, w_or_a='w'):
    data_frame.to_csv(path, mode=w_or_a, encoding='utf-8', index=False, header=columns)


start_time = time.time()
df_pay = pd.read_csv('full_pay.csv')
df_table = pd.read_csv('table_arch.csv', low_memory=False)
df_pay = df_pay.fillna(0)
df_table = df_table.fillna(0)
counter = df_pay.shape[0]
link_table = []
for i in range(counter):
    df_filter_table_2_g = filter_link(i, df_table, df_pay)
    link_1 = append_in_list(i, df_filter_table_2_g, df_pay)
    link_table.append(link_1)

columns = ['item', 'number_cmd', 'PRODUIT', 'N°PIECE', 'IND PROD', 'REF_BAAN', 'full_cod1', 'обозначение',
           'номер_заказа']
df_link_table = pd.DataFrame(data=link_table, columns=columns)
save_csv_header_w('link_table.csv', df_link_table)
print("--- %s seconds ---" % (time.time() - start_time))
