import pandas as pd
import time


start_time = time.time()
df_pay = pd.read_csv('full_pay.csv')
df_table = pd.read_csv('table_arch.csv', low_memory=False)

link_table = []
link_table_1 = []
df_filter_table_1 = df_table[df_table['N°CMD'] == df_pay.loc[0, 'номер_заказа']]
df_filter_table_2 = df_filter_table_1[df_filter_table_1['full_cod3'] == df_pay.loc[0, 'full_cod1']].reset_index(
    drop=True)
link_table_1.append(df_filter_table_2.loc[0, 'N° ITEM'])
link_table_1.append(df_filter_table_2.loc[0, 'N°CMD'])
link_table_1.append(df_filter_table_2.loc[0, 'PRODUIT'])
link_table_1.append(str(int(df_filter_table_2.loc[0, 'N°PIECE'])))
link_table_1.append(df_filter_table_2.loc[0, 'IND PROD'])
link_table_1.append(df_filter_table_2.loc[0, 'REF_BAAN'])
link_table_1.append(df_pay.loc[0, 'full_cod1'])
link_table_1.append(df_pay.loc[0, 'обозначение'])

print(link_table_1)
print("--- %s seconds ---" % (time.time() - start_time))
