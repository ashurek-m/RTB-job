import pandas as pd


def save_excel(path, data_frame, columns=True):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False, header=columns)
    writer_on.save()


df = pd.read_csv('full_pay_2019-2021.csv')
save_excel('full_pay_2019-2021.xlsx', df)
