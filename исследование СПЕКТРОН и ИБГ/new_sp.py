import pandas as pd
import time


start_time = time.time()
df_pay = pd.read_excel('спектронус-плюс.xlsx')
df_pay =df_pay.assign(dart_prepa=lambda x: x['dart_т_подг_мин'] + x['mx\dart-tour_т_подг_мин'])
df_pay = df_pay.assign(dart_catting=lambda x: x['dart_т_маш_мин'] + x['mx\dart-tour_т_ман_мин'])
df_tech = pd.read_excel('АРХИВ ТЕХНОЛОГИЙ плюс.xlsx')
iter = df_pay.shape[0]
time_list = []
time_list1 = []
support_list = ['REF_BAAN',
                'ИНДЕКС',
                'номер_заказа',
                'cn_т_подг_мин',
                'cn_т_маш_мин',
                'dart_prepa',
                'dart_catting',
                'tour_т_подг_мин',
                'tour_т_маш_мин',
                ]
print(iter)
for j in range(iter):
    df_tech1 = df_tech[df_tech['name_3'] == df_pay.loc[j, 'name_2']]
    df_tech2 = df_tech1[df_tech1['ИНДЕКС'] == df_pay.loc[j, 'index_2']].reset_index(drop=True)
    time_prepa = df_tech2.groupby('Tache')['Tpc prepa'].sum()
    time_catting = df_tech2.groupby('Tache')['Tpc exec'].sum()
    time_prepa_200 = time_prepa[200]
    time_prepa_205 = time_prepa[205]
    time_prepa_200 = time_prepa[200]
    time_prepa_200 = time_prepa[200]
    time_prepa_200 = time_prepa[200]
    # print(time_prepa)
    print(time_prepa_200)
    # print(time_catting)
    print(type(time_catting))
    df_pay1 = df_pay.loc[j, ['cn_т_подг_мин',
                             'cn_т_маш_мин',
                             'dart_prepa',
                             'dart_catting',
                             'tour_т_подг_мин',
                             'tour_т_маш_мин',
                             'номер_заказа',
                             ]]
    time_list1.append(df_tech2.loc[0, support_list[0]])
    time_list1.append(df_tech2.loc[0, support_list[1]])
    time_list1.append(df_pay.loc[j, support_list[2]])
    time_list1.append(df_pay.loc[j, support_list[3]])
    time_list1.append(df_pay.loc[j, support_list[4]])
    time_list1.append(df_pay.loc[j, support_list[5]])
    time_list1.append(df_pay.loc[j, support_list[6]])
    time_list1.append(df_pay.loc[j, support_list[7]])
    time_list1.append(df_pay.loc[j, support_list[8]])
    print(time_list1)
    print('stop')
    input()
print("--- %s seconds ---" % (time.time() - start_time))
