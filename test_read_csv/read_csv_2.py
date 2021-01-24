import pandas as pd

csv = pd.read_csv(r"C:\Python's_project\RTB-job\address_file.csv", names=['path'])
print()
total = csv.loc[:, 'path']
way = 'r' + str(total[0])
df = pd.read_excel(str(total[0]), sheet_name='расчет', header=11,)
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
columns3.info()
path = 'info.csv'
columns3.to_csv('info.csv', encoding='utf-8', index=False, header=False, mode='a')
columns3.to_csv('info.csv', encoding='utf-8', index=False, header=False, mode='a')