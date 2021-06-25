import pandas as pd
import preparation as prepa


if __name__ in '__main__':
    '''
    print('1')
    columns = ['det', 'ind', 'count']
    data = [['1', '1', 15], ['2', '3', 21], ['1', '1', 52], ['2', '2', 33]]
    df = pd.DataFrame(data=data, columns=columns)
    #df = df[(df['count'] > 0) & (df['count'] < 1000)]
    df = df.groupby(['det', 'ind']).size().reset_index()
    print(df)
    '''
    var = int(input('var = '))
    if var == 1:
        print('0')
        df = pd.read_excel('courant.xlsx')
        df = df.loc[:, ['N° ITEM', 'COMMENTAIRE PROD', 'N°CMD', 'PRODUIT', 'N°PIECE', 'DESIGNATION', 'IND PROD', 'REF_BAAN']]
        print('1')
        df1 = prepa.transformation_table_courant(df)
        print('2')
        df_table = pd.read_csv(df1)
        df_pay = pd.read_excel('pay_2021_rev1.xlsx')
        df_pay = df_pay.fillna(0)
        df_table = df_table.fillna(0)
        counter = df_table.shape[0]
        print(counter)
        print('3')
        link_table = []
        for i in range(counter):
            df_filter_table_2_g = prepa.filter_link(i, df_table, df_pay)
            link_1 = prepa.append_in_list(i, df_table, df_filter_table_2_g)
            link_table.append(link_1)
        print('4')
        columns = ['N° ITEM', 'COMMENTAIRE PROD', 'N°CMD', 'PRODUIT', 'N°PIECE', 'IND PROD', 'REF_BAAN', 'full_cod1',
                   'обозначение', 'индекс', 'номер_заказа']
        df_link_table = pd.DataFrame(data=link_table, columns=columns)
        prepa.save_csv_header_w('link_table.csv', df_link_table)
    elif var == 2:
        df_pay = pd.read_excel('pay_2021_rev1.xlsx')
        df_pay_groupby = df_pay.groupby(['обозначение', 'индекс']).size().reset_index()
        shape1 = df_pay_groupby.shape[0]
        id_pay = [105867]
        for i in range(1, shape1):
            id_pay.append(id_pay[i - 1] + 1)
        df_pay_groupby = df_pay_groupby.assign(id_name_pay=id_pay)
        df_pay_groupby = df_pay_groupby.loc[:, ['обозначение', 'индекс', 'id_name_pay']]
        df_pay_groupby.info()
        prepa.save_excel('id_name.xlsx', df_pay_groupby)
    elif var == 3:
        df = pd.read_csv('link_table.csv')
        prepa.save_excel('link_table.xlsx', df)
    elif var == 4:
        df = pd.read_excel('pay_id_name.xlsx')
        df_pay_groupby = df.groupby('обозначение').size().reset_index()
        df_pay_groupby.info()



