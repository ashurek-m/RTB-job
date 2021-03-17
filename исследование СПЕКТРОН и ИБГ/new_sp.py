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


def save_excel(path, data_frame, columns=True):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False, header=columns)
    writer_on.save()


start_time = time.time()
df_pay = pd.read_excel('спектронус-плюс.xlsx')
df_pay = df_pay.fillna(0)
df_pay = df_pay.assign(dart_prepa=lambda x: x['dart_т_подг_мин'] + x['mx\dart-tour_т_подг_мин'] + x['mx-cn_т_подг_мин'])
df_pay = df_pay.assign(dart_catting=lambda x: x['dart_т_маш_мин'] + x['mx\dart-tour_т_ман_мин'] +
                                              x['mx-cn_т_маш_мин'])
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
                'финишная_т_подг_мин',
                'финишная_т_маш_мин',
                'слесарная_т_подг_мин',
                'слесарная_т_маш_мин',
                'шлифовальная_т_подг_мин',
                'шлифовальная_т_маш_мин',
                't_prepa_200',
                't_prepa_205',
                't_prepa_209',
                't_prepa_210',
                't_prepa_211',
                't_prepa_215',
                't_prepa_220',
                't_prepa_233',
                't_prepa_225',
                't_catting_200',
                't_catting_205',
                't_catting_209',
                't_catting_210',
                't_catting_211',
                't_catting_215',
                't_catting_220',
                't_catting_233',
                't_catting_225',
                'технология'
                ]
tech_number = [200, 205, 209, 210, 211, 215, 220, 233, 225]

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
        time_list1.append(df_pay.loc[j, support_list[9]])
        time_list1.append(df_pay.loc[j, support_list[10]])
        time_list1.append(df_pay.loc[j, support_list[11]])
        time_list1.append(df_pay.loc[j, support_list[12]])
        time_list1.append(df_pay.loc[j, support_list[13]])
        time_list1.append(df_pay.loc[j, support_list[14]])
        for i in range(len(tech_number)):
            time_list1.append(to_be(tech_number[i], index1, time_prepa))
        for i in range(len(tech_number)):
            time_list1.append(to_be(tech_number[i], index1, time_catting))
        time_list1.append('технология есть')
        print(time_list1)
        time_list.append(time_list1)
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
        time_list1.append(df_pay.loc[j, support_list[9]])
        time_list1.append(df_pay.loc[j, support_list[10]])
        time_list1.append(df_pay.loc[j, support_list[11]])
        time_list1.append(df_pay.loc[j, support_list[12]])
        time_list1.append(df_pay.loc[j, support_list[13]])
        time_list1.append(df_pay.loc[j, support_list[14]])
        zetta = 18
        for i in range(zetta):
            time_list1.append(0)
        time_list1.append('технология нет')
        print(time_list1)
        time_list.append(time_list1)
    # print('stop')
    # input()
df_all_time = pd.DataFrame(data=time_list, columns=support_list)
df_all_time = df_all_time.assign(total_prepa_pay=lambda x: x['cn_т_подг_мин'] + x['dart_prepa'] +
                                                           x['tour_т_подг_мин'])
df_all_time = df_all_time.assign(total_prepa_tech=lambda x: x['t_prepa_200'] + x['t_prepa_205'] +
                                                            x['t_prepa_209'] + x['t_prepa_210'] +
                                                            x['t_prepa_211'] + x['t_prepa_215'])
df_all_time = df_all_time.assign(relation_prepa=lambda x: x['total_prepa_pay'] / x['total_prepa_tech'])
df_all_time = df_all_time.assign(total_catting_pay=lambda x: x['cn_т_маш_мин'] + x['dart_catting'] +
                                                             x['tour_т_маш_мин'])
df_all_time = df_all_time.assign(total_catting_tech=lambda x: x['t_catting_200'] + x['t_catting_205'] +
                                                            x['t_catting_209'] + x['t_catting_210'] +
                                                            x['t_catting_211'] + x['t_catting_215'])
df_all_time = df_all_time.assign(relation_catting=lambda x: x['total_catting_pay'] / x['total_catting_tech'])
df_all_time = df_all_time.fillna(0)
# df_all_time.info()
save_excel('all_time.xlsx', df_all_time)
print("--- %s seconds ---" % (time.time() - start_time))
