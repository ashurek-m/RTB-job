import pandas as pd


def save_csv_header_w(path, data_frame, columns=True, w_or_a='w'):
    data_frame.to_csv(path, mode=w_or_a, encoding='utf-8', index=False, header=columns)


def transformation_table_courant(data):
    #df_table = pd.read_excel(path)
    df_cod_baan = data.loc[:, 'REF_BAAN']
    cod_baan = []
    for i in range(len(df_cod_baan)):
        format_cod_baan = str(df_cod_baan[i]).strip()
        one_cod_baan = [x for x in format_cod_baan]
        cod_baan.append(one_cod_baan)
    df_full_cod = []
    for i in range(len(cod_baan)):
        full_cod = [x for x in cod_baan[i] if x.isalpha() == False]
        df_full_cod.append(''.join(full_cod))
    print(len(cod_baan) == len(df_full_cod))
    df_table = data.assign(full_cod3=df_full_cod)
    save_csv_header_w('table.csv', df_table)
    return 'table.csv'


def append_in_list(k, data, data_pay):
    link_table_1 = []
    if data_pay.shape[0] > 0:
        link_table_1.append(data.loc[k, 'N° ITEM'])
        link_table_1.append(data.loc[k, 'COMMENTAIRE PROD'])
        link_table_1.append(data.loc[k, 'N°CMD'])
        link_table_1.append(data.loc[k, 'PRODUIT'])
        link_table_1.append(data.loc[k, 'N°PIECE'])
        link_table_1.append(data.loc[k, 'IND PROD'])
        link_table_1.append(data.loc[k, 'REF_BAAN'])
        link_table_1.append(data_pay.loc[0, 'full_cod1'])
        link_table_1.append(data_pay.loc[0, 'обозначение'])
        link_table_1.append(data_pay.loc[0, 'индекс'])
        link_table_1.append(data_pay.loc[0, 'номер_заказа'])
        return link_table_1
    else:
        link_table_1.append(data.loc[k, 'N° ITEM'])
        link_table_1.append(data.loc[k, 'COMMENTAIRE PROD'])
        link_table_1.append(data.loc[k, 'N°CMD'])
        link_table_1.append(data.loc[k, 'PRODUIT'])
        link_table_1.append(data.loc[k, 'N°PIECE'])
        link_table_1.append(data.loc[k, 'IND PROD'])
        link_table_1.append(data.loc[k, 'REF_BAAN'])
        for g in range(4):
            link_table_1.append(0)
        return link_table_1


def filter_link(k, data, data_pay):
    df_filter_table_1 = data_pay[data_pay['номер_заказа'] == data.loc[k, 'N°CMD']]
    df_filter_table_2 = df_filter_table_1[df_filter_table_1['full_cod1'] == data.loc[k, 'full_cod3']].reset_index(
        drop=True)
    return df_filter_table_2
