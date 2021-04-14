import pandas as pd
import time


def save_csv_header_w(path, data_frame, columns=True, w_or_a='w'):
    data_frame.to_csv(path, mode=w_or_a, encoding='utf-8', index=False, header=columns)


def save_excel(path, data_frame, columns=True):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False, header=columns)
    writer_on.save()


start_time = time.time()

df_2019 = pd.read_csv('full_pay_2019.csv')
df_2019 = df_2019.assign(year=2019)
df_2020 = pd.read_csv('full_pay_2020.csv')
df_2020 = df_2020.assign(year=2020)
df_2021 = pd.read_csv('full_pay_2021.csv')
df_2021 = df_2021.assign(year=2021)
save_csv_header_w('full_pay_2019-2021.csv', df_2019)
save_csv_header_w('full_pay_2019-2021.csv', w_or_a='a', data_frame=df_2020)
save_csv_header_w('full_pay_2019-2021.csv', w_or_a='a', data_frame=df_2021)
print('next')
input()
df = pd.read_csv('full_pay_2019-2021.csv')
save_excel('full_pay_2019-2021.xlsx', df)

print("--- %s seconds ---" % (time.time() - start_time))
