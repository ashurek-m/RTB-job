import numpy as np
import pandas as pd
import datetime as dt
import time
import matplotlib.pyplot as plt
import seaborn as sns


def save_excel(path, data_frame):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False)
    writer_on.save()


df_pr = pd.read_excel('C:\\Users\\oshurek_m\\Desktop\\proizv.xlsx')
df_oper = pd.read_excel('C:\\Users\\oshurek_m\\Desktop\\oper.xlsx')
print(df_oper.shape)
df = df_oper.merge(df_pr, how='outer', on='N° ITEM')
print(df.shape)

df_1 = df.loc[:, ['НомерОперации', 'N° ITEM']]
df_1.fillna(0, inplace=True)
df_1['НомерОперации'] = df_1['НомерОперации'].astype(int)
df_1 = df_1[df_1['НомерОперации'] == 0]
save_excel('C:\\Users\\oshurek_m\\Desktop\\rez1.xlsx', df_1)

df_2 = df.loc[:, ['КодBAAN', 'N° ITEM']]
df_2.fillna(0, inplace=True)
df_2 = df_2[df_2['КодBAAN'] == 0]
save_excel('C:\\Users\\oshurek_m\\Desktop\\rez2.xlsx', df_2)
