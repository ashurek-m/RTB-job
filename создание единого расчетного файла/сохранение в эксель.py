import pandas as pd


def save_excel(path, data_frame, columns=True):
    writer_on = pd.ExcelWriter(path, engine='xlsxwriter')
    data_frame.to_excel(writer_on, index=False, header=columns)
    writer_on.save()


df = pd.read_csv('link_table_2019-2021rev2.csv')
save_excel('link_table_2019-2021rev2.xlsx', df)
