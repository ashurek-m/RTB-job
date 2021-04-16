import pandas as pd
import time


def append_in_list(k, data, data_pay):
    link_table_1 = []
    if data_pay.shape[0] > 0:
        link_table_1.append(data.loc[k, 'N° ITEM'])
        link_table_1.append(data.loc[k, 'N°CMD'])
        link_table_1.append(data.loc[k, 'COMMENTAIRE PROD'])
        link_table_1.append(data.loc[k, 'PRODUIT'])
        link_table_1.append(str(int(data.loc[k, 'N°PIECE'])))
        link_table_1.append(data.loc[k, 'IND PROD'])
        link_table_1.append(data.loc[k, 'REF_BAAN'])
        link_table_1.append(data_pay.loc[0, 'full_cod1'])
        link_table_1.append(data_pay.loc[0, 'обозначение'])
        link_table_1.append(data_pay.loc[0, 'номер_заказа'])
        return link_table_1
    else:
        link_table_1.append(data.loc[k, 'N° ITEM'])
        link_table_1.append(data.loc[k, 'N°CMD'])
        link_table_1.append(data.loc[k, 'COMMENTAIRE PROD'])
        link_table_1.append(data.loc[k, 'PRODUIT'])
        link_table_1.append(str(int(data.loc[k, 'N°PIECE'])))
        link_table_1.append(data.loc[k, 'IND PROD'])
        link_table_1.append(data.loc[k, 'REF_BAAN'])
        for g in range(3):
            link_table_1.append(0)
        return link_table_1


def filter_link(k, data, data_pay):
    df_filter_table_1 = data_pay[data_pay['номер_заказа'] == data.loc[k, 'N°CMD']]
    df_filter_table_2 = df_filter_table_1[df_filter_table_1['full_cod1'] == data.loc[k, 'full_cod3']].reset_index(
        drop=True)
    return df_filter_table_2


def save_csv_header_w(path, data_frame, columns=True, w_or_a='w'):
    data_frame.to_csv(path, mode=w_or_a, encoding='utf-8', index=False, header=columns)


def save_excel(path, data_frame, columns):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False, header=columns)
    writer_on.save()


start_time = time.time()
df_pay = pd.read_csv('full_pay_2019-2021.csv')
df_table = pd.read_csv('table_arch.csv', low_memory=False)
df_pay = df_pay.fillna(0)
df_table = df_table.fillna(0)
counter = df_table.shape[0]
link_table = []
for i in range(counter):
    df_filter_table_2_g = filter_link(i, df_table, df_pay)
    link_1 = append_in_list(i, df_table, df_filter_table_2_g)
    link_table.append(link_1)

columns = ['item', 'number_cmd', 'COMMENTAIRE PROD', 'PRODUIT', 'N°PIECE', 'IND PROD', 'REF_BAAN', 'full_cod1',
           'обозначение', 'номер_заказа']
df_link_table = pd.DataFrame(data=link_table, columns=columns)
save_csv_header_w('link_table_2019-2021rev2.csv', df_link_table)
print("--- %s seconds ---" % (time.time() - start_time))
