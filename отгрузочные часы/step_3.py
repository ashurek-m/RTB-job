import pandas as pd


def save_csv_header_w(path, data_frame, columns=True, w_or_a='w'):
    data_frame.to_csv(path, mode=w_or_a, encoding='utf-8', index=False, header=columns)


def shape_r62(shape_list, name_file):
    for i in range(len(shape_list)):
        if shape_list[i] == 62:
            df_62 = pd.read_csv(name_file[i])
            save_csv_header_w('united_pay_file_2021.csv', df_62, columns=False)
        elif shape_list[i] == 63:
            df_63 = pd.read_csv(name_file[i])
            columns_drop63 = ['price, $']
            df_63.drop(columns_drop63, inplace=True, axis=1)
            save_csv_header_w('united_pay_file_2021.csv', df_63, columns=False, w_or_a='a')
        elif shape_list[i] == 64:
            df_64 = pd.read_csv(name_file[i])
            columns_drop64 = ['Unnamed: 8', 'price']
            df_64.drop(columns_drop64, inplace=True, axis=1)
            save_csv_header_w('united_pay_file_2021.csv', df_64, columns=False, w_or_a='a')
        elif shape_list[i] == 65:
            df_65 = pd.read_csv(name_file[i])
            columns_drop65 = ['..\..\..\Department - Quality\Metrology\Calibers', 'Unnamed: 27', 'price, $']
            df_65.drop(columns_drop65, inplace=True, axis=1)
            save_csv_header_w('united_pay_file.csv', df_65, columns=False, w_or_a='a')
        elif shape_list[i] == 66:
            df_66 = pd.read_csv(name_file[i])
            columns_drop66 = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 10']
            df_66.drop(columns_drop66, inplace=True, axis=1)
            save_csv_header_w('united_pay_file.csv', df_66, columns=False, w_or_a='a')
        elif shape_list[i] == 67:
            df_67 = pd.read_csv(name_file[i])
            columns_drop67 = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 10', 'price']
            df_67.drop(columns_drop67, inplace=True, axis=1)


def shape_r61(shape_list, name_file):
    for i in range(len(shape_list)):
        if shape_list[i] == 61:
            df_61 = pd.read_csv(name_file[i])
            save_csv_header_w('united_pay_file_2021.csv', df_61, columns=False)
        elif shape_list[i] == 62:
            df_62 = pd.read_csv(name_file[i])
            save_csv_header_w('united_pay_file_2021.csv', df_62, columns=False, w_or_a='a')
        elif shape_list[i] == 63:
            df_63 = pd.read_csv(name_file[i])
            columns_drop63 = ['price, $']
            df_63.drop(columns_drop63, inplace=True, axis=1)
            save_csv_header_w('united_pay_file_2021.csv', df_63, columns=False, w_or_a='a')
        elif shape_list[i] == 64:
            df_64 = pd.read_csv(name_file[i])
            columns_drop64 = ['Unnamed: 8', 'price']
            df_64.drop(columns_drop64, inplace=True, axis=1)
            save_csv_header_w('united_pay_file_2021.csv', df_64, columns=False, w_or_a='a')
        elif shape_list[i] == 65:
            df_65 = pd.read_csv(name_file[i])
            columns_drop65 = ['..\..\..\Department - Quality\Metrology\Calibers', 'Unnamed: 27', 'price, $']
            df_65.drop(columns_drop65, inplace=True, axis=1)
            save_csv_header_w('united_pay_file.csv', df_65, columns=False, w_or_a='a')
        elif shape_list[i] == 66:
            df_66 = pd.read_csv(name_file[i])
            columns_drop66 = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 10']
            df_66.drop(columns_drop66, inplace=True, axis=1)
            save_csv_header_w('united_pay_file.csv', df_66, columns=False, w_or_a='a')
        elif shape_list[i] == 67:
            df_67 = pd.read_csv(name_file[i])
            columns_drop67 = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 10', 'price']
            df_67.drop(columns_drop67, inplace=True, axis=1)
            save_csv_header_w('united_pay_file_2021.csv', df_67, columns=False, w_or_a='a')


def union(shape_list, name_file, name):
    if shape_list[0] == 61:
        shape_r61(shape_list, name_file)
    elif shape_list[0] == 62:
        shape_r62(shape_list, name_file)
    columns_for_excel = ['обозначение',
                         'наименование',
                         'индекс',
                         'коэф_входимости',
                         'заказанное_кол',
                         'уровень_критичности',
                         'примечания',
                         'наименование_материала',
                         'locmat_name',
                         'locmat',
                         'уд_вес',
                         'стоимость_мат_за_1кг_м',
                         'заг_диаметр',
                         'заг_толщина',
                         'заг_длина',
                         'заг_ширина',
                         'заг_на_кол_во',
                         'прутки',
                         'плиты',
                         'вес',
                         'стоимость_мат_ла',
                         'индустриализация_вид',
                         'индустриализация_стоимость',
                         'подряд_вид',
                         'подряд_стоимость',
                         'термообработка_вид',
                         'терообработка_стоимость',
                         'покрытие_площадь',
                         'покрытие_вид',
                         'покрытие_стоимость',
                         'резка_т_подг_мин',
                         'резка_т_маш_мин',
                         'резка_т_сум_ч',
                         'cn_т_подг_мин',
                         'cn_т_маш_мин',
                         'cn_т_сум_ч',
                         'dart_т_подг_мин',
                         'dart_т_маш_мин',
                         'dart_т_сум_ч',
                         'mx-cn_т_подг_мин',
                         'mx-cn_т_маш_мин',
                         'mx-cn_т_сум_ч',
                         'tour_т_подг_мин',
                         'tour_т_маш_мин',
                         'tour_т_сум_ч',
                         'mx\\dart-tour_т_подг_мин',
                         'mx\\dart-tour_т_ман_мин',
                         'mx\\dart-tour_т_сум_ч',
                         'финишная_т_подг_мин',
                         'финишная_т_маш_мин',
                         'финишная_т_сум_ч',
                         'слесарная_т_подг_мин',
                         'слесарная_т_маш_мин',
                         'слесарная_т_сум_ч',
                         'шлифовальная_т_подг_мин',
                         'шлифовальная_т_маш_мин',
                         'шлифовальная_т_сум_ч',
                         'резерв_т_подг_мин',
                         'резерв_т_маш_мин',
                         'резерв_т_сум_ч',
                         'т_партии_ч',
                         'номер_заказа']
    df_united = pd.read_csv('united_pay_file_2021.csv', names=columns_for_excel)
    save_csv_header_w(name, df_united)
    return name


'''
columns_drop67 = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 10', 'price']
df_shape_67.drop(columns_drop67, inplace=True, axis=1)
save_csv_header_w('united_pay_file_2021.csv', df_shape_67, columns=False, w_or_a='a')
columns_drop68 = ['Unnamed: 2', 'Unnamed: 3', 'Unnamed: 4', 'Unnamed: 10', 'Unnamed: 27', '$.2']
df_shape_68.drop(columns_drop68, inplace=True, axis=1)
save_csv_header_w('united_pay_file_2020.csv', df_shape_68, columns=False, w_or_a='a')
'''
