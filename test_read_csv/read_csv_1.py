import pandas as pd

csv = pd.read_csv(r"C:\Python's_project\RTB-job\address_file.csv", names=['path'])
print()
total = csv.loc[:, 'path']
print(len(total), total[0])
way = 'r' + str(total[0])
df = pd.read_excel(str(total[0]), sheet_name='расчет', header=11,)

columns1 = df.loc[2:,['Unnamed: 1',
                      'Unnamed: 5',
                      'Unnamed: 6',
                      'наименование материала',
                      'размеры заготовки',
                      'Unnamed: 18',
                      'Unnamed: 19',
                      'Unnamed: 20',
                      'Unnamed: 21',
                     ]]

columns1.info()
print(columns1.head())
columns1.set_axis(["обозначение_детали",
                              "наименование_детали",
                              "индекс",
                              "наименование_материала",
                              "диаметр",
                              "толщина",
                              "длина",
                              "ширина",
                              "на_кол-во",
                              ],
                             axis='columns', inplace=True)

columns1.info()
columns1.dropna(subset=['наименование_детали'], inplace=True)
columns1.info()

