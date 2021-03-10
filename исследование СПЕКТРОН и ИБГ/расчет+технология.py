import pandas as pd
import time


start_time = time.time()
df_pay = pd.read_excel('СПЕКТРОНУС.xlsx')
index = df_pay['индекс'].unique()
index_replacement = {}
index_list = ['01', '11', '00', '02', '04', '03', '10', '06', '05', '07']
for i in range(len(index)):
    index_replacement[index[i]] = index_list[i]
df_index = df_pay.loc[:, 'индекс']
for row in index_replacement:
    df_index = df_index.replace(row, index_replacement[row])
df_pay = df_pay.assign(index_2=df_index)
df_name = df_pay.loc[:, 'обозначение']
list_name = []
for i in range(len(df_name)):
    list_name.append(''.join(filter(str.isdigit, df_name[i])))
df_pay = df_pay.assign(name_2=list_name)

df_tech = pd.read_excel('АРХИВ ТЕХНОЛОГИЙ.xlsx')
df_refbaan = df_tech.loc[:, 'REF_BAAN']
for i in range(len(df_refbaan)):
    df_refbaan[i] = str(df_refbaan[i])
refbaan_list = []
for i in range(len(df_refbaan)):
    if type(df_refbaan[i]) != 'float':
        refbaan_list.append(filter(str.isdigit, df_refbaan[i]))
    else:
        refbaan_list.append(df_refbaan[i])
df_tech = df_tech.assign(name_3=refbaan_list)

iter = df_pay.shape[0]
for j in range(iter):
    df_tech = df_tech[df_tech['REF_BAAN'] == df_pay.loc[j, 'name_2']]
    df_tech = df_tech[df_tech['ИНДЕКС'] == df_pay.loc[j, 'index_2']]
    print(df_tech.loc[:, 'Tpc prepa': 'Tpc exec'])
    t_cn_prepa = df_tech.groupby('Tache')['Tpc prepa'].sum()
    print(t_cn_prepa)
    input()

print("--- %s seconds ---" % (time.time() - start_time))
