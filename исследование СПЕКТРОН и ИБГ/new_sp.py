import pandas as pd
import time


def zero_or_no(what_we_compare, compare_it_with, data):
    if what_we_compare == compare_it_with:
        save1 = data[what_we_compare]
        return save1
    else:
        save1 = 0
        return save1


def to_be(numder, what_we_compare, what_look):
    check = numder in what_we_compare
    if check == True:
        save = what_look[numder]
        return save
    else:
        save = 0
        return save


start_time = time.time()
df_pay = pd.read_excel('спектронус-плюс.xlsx')
df_pay =df_pay.assign(dart_prepa=lambda x: x['dart_т_подг_мин'] + x['mx\dart-tour_т_подг_мин'])
df_pay = df_pay.assign(dart_catting=lambda x: x['dart_т_маш_мин'] + x['mx\dart-tour_т_ман_мин'])
df_tech = pd.read_excel('АРХИВ ТЕХНОЛОГИЙ плюс.xlsx')
iter = df_pay.shape[0]
time_list = []
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
tech_number = [200, 205, 209, 210, 211, 215]

for j in range(iter):
    time_list1 = []
    df_tech1 = df_tech[df_tech['name_3'] == df_pay.loc[j, 'name_2']]
    df_tech2 = df_tech1[df_tech1['ИНДЕКС'] == df_pay.loc[j, 'index_2']].reset_index(drop=True)
    if df_tech2.shape[0] != 0:
        time_prepa = df_tech2.groupby('Tache')['Tpc prepa'].sum()
        time_catting = df_tech2.groupby('Tache')['Tpc exec'].sum()
        index1 = time_prepa.index
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
        for i in range(len(tech_number)):
            time_list1.append(to_be(tech_number[i], index1, time_prepa))
        for i in range(len(tech_number)):
            time_list1.append(to_be(tech_number[i], index1, time_catting))
        time_list1.append('технология есть')
        print(time_list1)
    else:
        time_list1.append(df_pay.loc[j, 'обозначение'])
        time_list1.append(df_pay.loc[j, 'индекс'])
        time_list1.append(df_pay.loc[j, support_list[2]])
        time_list1.append(df_pay.loc[j, support_list[3]])
        time_list1.append(df_pay.loc[j, support_list[4]])
        time_list1.append(df_pay.loc[j, support_list[5]])
        time_list1.append(df_pay.loc[j, support_list[6]])
        time_list1.append(df_pay.loc[j, support_list[7]])
        time_list1.append(df_pay.loc[j, support_list[8]])
        zetta = 12
        for i in range(zetta):
            time_list1.append(0)
        time_list1.append('технология нет')
        print(time_list1)
    # print('stop')
    # input()
print("--- %s seconds ---" % (time.time() - start_time))
