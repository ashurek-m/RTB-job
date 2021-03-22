import pandas as pd
import time
import csv


def save_csv_header_w(path, data_frame, columns=True, w_or_a='w'):
    data_frame.to_csv(path, mode=w_or_a, encoding='utf-8', index=False, header=columns)


start_time = time.time()
a = 's pam123.456-01'
b = [x for x in a if x.isalpha() == False]
print(b)
df_pay_data = pd.read_excel('united_pay_file_2019.xlsx')
df_cod_baan = df_pay_data.loc[:, 'обозначение']
cod_baan = []
for i in range(len(df_cod_baan)):
    format_cod_baan = df_cod_baan[i].strip()
    one_cod_baan = [x for x in format_cod_baan]
    cod_baan.append(one_cod_baan)

df_full_cod = []
for i in range(len(cod_baan)):
    full_cod = [x for x in cod_baan[i] if x.isalpha() == False]
    df_full_cod.append(''.join(full_cod))

df_pay_data = df_pay_data.assign(full_cod1=df_full_cod)

df_tech_data = pd.read_excel('АРХИВ ТЕХНОЛОГИЙ.xlsx')
df_cod_baan = df_tech_data.loc[:, 'REF_BAAN']
cod_baan = []
for i in range(len(df_cod_baan)):
    format_cod_baan = str(df_cod_baan[i]).strip()
    one_cod_baan = [x for x in format_cod_baan]
    cod_baan.append(one_cod_baan)

df_full_cod = []
for i in range(len(cod_baan)):
    full_cod = [x for x in cod_baan[i] if x.isalpha() == False]
    df_full_cod.append(''.join(full_cod))
print(len(cod_baan) == len(df_full_cod))
df_tech_data = df_tech_data.assign(full_cod2=df_full_cod)
save_csv_header_w('full_tech.csv', df_tech_data)
print("--- %s seconds ---" % (time.time() - start_time))
