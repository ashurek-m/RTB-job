import pandas as pd
import time


def save_excel(path, data_frame, columns=True):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False, header=columns)
    writer_on.save()


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
df_refbaan_str = []
for i in range(len(df_refbaan)):
    df_refbaan_str.append(str(df_refbaan[i]))
refbaan_list = []
for i in range(len(df_refbaan)):
    if type(df_refbaan[i]) != 'float':
        refbaan_list.append(''.join(filter(str.isdigit, df_refbaan_str[i])))
    else:
        refbaan_list.append(df_refbaan[i])
df_tech = df_tech.assign(name_3=refbaan_list)

# save_excel('спектронус-плюс.xlsx', df_pay)
save_excel('АРХИВ ТЕХНОЛОГИЙ плюс.xlsx', df_tech)
print("--- %s seconds ---" % (time.time() - start_time))
