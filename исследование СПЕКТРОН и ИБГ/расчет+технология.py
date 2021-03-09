import pandas as pd
import time
import re


start_time = time.time()
df_pay = pd.read_excel('СПЕКТРОНУС.xlsx')
index = df_pay['индекс'].unique()
print(index, len(index))
index_replacement = {}
index_list = ['01', '11', '00', '02', '04', '03', '10', '06', '05', '07']
for i in range(len(index)):
    index_replacement[index[i]] = index_list[i]
print(index_replacement)
df_index = df_pay.loc[:, 'индекс']
for row in index_replacement:
    df_index = df_index.replace(row, index_replacement[row])
df_pay = df_pay.assign(index_2=df_index)
df_pay = df_pay.assign(name=''.join(filter()))
print("--- %s seconds ---" % (time.time() - start_time))
