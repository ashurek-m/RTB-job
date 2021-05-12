import pandas as pd
import step_3 as s3


def transformation_pay(path, name, year_1):
    df_pay_data = pd.read_csv(path)
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
    df_pay_data = df_pay_data.assign(year=year_1)
    s3.save_csv_header_w(name, df_pay_data)


def transformation_table_courant(path):
    df_table = pd.read_excel(path)
    df_cod_baan = df_table.loc[:, 'REF_BAAN']
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
    df_table = df_table.assign(full_cod3=df_full_cod)
    s3.save_csv_header_w('table_arch.csv', df_table)


def transformation_tech(path):
    df_tech_data = pd.read_excel(path)
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
    s3.save_csv_header_w('full_tech.csv', df_tech_data)