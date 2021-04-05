import pandas as pd
import time


def save_csv_header_w(path, data_frame, columns=True, w_or_a='w'):
    data_frame.to_csv(path, mode=w_or_a, encoding='utf-8', index=False, header=columns)


def save_excel(path, data_frame, columns=True):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False, header=columns)
    writer_on.save()


start_time = time.time()
df_2019 = pd.read_csv('link_table_2019.csv')
df_2019 = df_2019.assign(year=2019)
df_2020 = pd.read_csv('link_table_2020.csv')
df_2020 = df_2020.assign(year=2020)
df_pay_2019 = pd.read_csv('full_pay_2019.csv')
df_pay_2019 = df_pay_2019.assign(year=2019)
# save_csv_header_w('link_2019-2020.csv', df_2019)
# save_csv_header_w('link_2019-2020.csv', w_or_a='a', data_frame=df_2020)
# df = pd.read_csv('link_2019-2020.csv')
save_excel('full_pay_2019.xlsx', df_pay_2019)

print("--- %s seconds ---" % (time.time() - start_time))
