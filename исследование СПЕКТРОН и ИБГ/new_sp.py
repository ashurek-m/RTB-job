import pandas as pd
import time


start_time = time.time()
df_pay = pd.read_excel('спектронус-плюс.xlsx')
df_tech = pd.read_excel('АРХИВ ТЕХНОЛОГИЙ плюс.xlsx')
iter = df_pay.shape[0]
print(iter)
for j in range(iter):
    df_tech1 = df_tech[df_tech['name_3'] == df_pay.loc[j, 'name_2']]
    df_tech2 = df_tech1[df_tech1['ИНДЕКС'] == df_pay.loc[j, 'index_2']]
    print(df_pay.loc[j, 'name_2'])
    print(df_tech2.loc[:, 'Tpc prepa': 'Tpc exec'])
    t_cn_prepa = df_tech2.groupby('Tache')['Tpc prepa'].sum()
    print(t_cn_prepa)
    input()
print("--- %s seconds ---" % (time.time() - start_time))
