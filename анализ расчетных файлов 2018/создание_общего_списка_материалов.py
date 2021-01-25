import pandas as pd
import time

start_time = time.time()
csv1 = pd.read_csv(r"C:\Python's_project\RTB-job\анализ расчетных файлов 2018\good_address_file.csv", names=['path'])
total = csv1.loc[:, 'path']

for i in range(len(total)):
    way = 'r' + str(total[i])
    df = pd.read_excel(str(total[i]), sheet_name='расчет', header=11,)
    columns1 = df.loc[2:,'наименование материала': 'потребность в материале']
    columns1.dropna(subset=['наименование материала'], inplace=True)
    columns2 = columns1.reset_index(drop=True)
    columns2.set_axis(["наименование_материала",
                        "Code",
                        "Description",
                        "уд_вес",
                        "стоимость_за_1кг",
                        "диаметр",
                        "толщина",
                        "длина",
                        "ширина",
                        "на_кол-во",
                        "потребность_в_материала"],
                        axis='columns', inplace=True)
    columns3 = columns2.loc[:, ['наименование_материала', 'диаметр', 'толщина', 'длина', 'ширина']]
    columns3 = columns3.fillna(0)
    path = 'info_mat.csv'
    if i == 0:
        columns3.to_csv(path, encoding='utf-8', index=False, header=True, mode='a')
    else:
        columns3.to_csv(path, encoding='utf-8', index=False, header=False, mode='a')

print("--- %s seconds ---" % (time.time() - start_time))
csv2 = pd.read_csv(r"C:\Python's_project\RTB-job\анализ расчетных файлов 2018\info_mat.csv")
csv2.info()
