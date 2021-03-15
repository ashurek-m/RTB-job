import pandas as pd
import time

start_time = time.time()
df_pay = pd.read_excel('спектронус-плюс.xlsx')
df_pay = df_pay.assign(dart_prepa=lambda x: x['dart_т_подг_мин'] + x[r'mx\dart-tour_т_подг_мин'])
df_pay = df_pay.assign(dart_catting=lambda x: x['dart_т_маш_мин'] + x[r'mx\dart-tour_т_ман_мин'])
df_tech = pd.read_excel('АРХИВ ТЕХНОЛОГИЙ плюс.xlsx')
iteration = df_pay.shape[0]
time_list = []
print(iteration)
for j in range(iteration):
    df_tech1 = df_tech[df_tech['name_3'] == df_pay.loc[j, 'name_2']]
    df_tech2 = df_tech1[df_tech1['ИНДЕКС'] == df_pay.loc[j, 'index_2']]
    time_prepa = df_tech2.groupby('Tache')['Tpc prepa'].sum()
    time_catting = df_tech2.groupby('Tache')['Tpc exec'].sum()
    print(time_prepa)
    print(time_catting)
    df_pay1 = df_pay.loc[j, ['cn_т_подг_мин',
                             'cn_т_маш_мин',
                             'dart_prepa',
                             'dart_catting',
                             'tour_т_подг_мин',
                             'tour_т_маш_мин']]
    print(df_pay1)
    print('stop')
    input()
print("--- %s seconds ---" % (time.time() - start_time))
