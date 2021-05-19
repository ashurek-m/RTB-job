import pandas as pd


def save_excel(path, data_frame, columns=True):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False, header=columns)
    writer_on.save()


df = pd.read_csv('full_union_file_2020.csv')
df = df.assign(year=2020)
df = df.fillna(0)
save_excel('full_pay_2020.xlsx', df)
