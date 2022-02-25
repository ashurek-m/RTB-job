from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
import pandas as pd

df = pd.read_excel('C:\\Users\\oshurek_m\\Desktop\\Пеленг общий.xlsx', sheet_name='matmod')
df_1 = df[['Индекс RTB', 'Наименование детали', 'Кол-во', 'N° ITEM', 'Стоимость, $', 'CN', 'DART', 'TOUR']]
df_2 = df_1.dropna(axis=0)
df_2.info()
model = LpProblem('prod', LpMaximize)
names_det = list(df_2['Наименование детали'])
costs = dict(zip(names_det, df_2['Стоимость, $']))
cn = dict(zip(names_det, df_2['CN']))
dart = dict(zip(names_det, df_2['DART']))
tour = dict(zip(names_det, df_2['TOUR']))

vat = LpVariable.dict('vat', names_det, cat='Binary')
model += lpSum(costs[i]*vat[i] for i in names_det)
t_cn = 350
t_dart = 20
t_tour = 100
model += lpSum(cn[j]*vat[j] for j in names_det) <= t_cn
model += lpSum(dart[j]*vat[j] for j in names_det) <= t_dart
model += lpSum(tour[j]*vat[j] for j in names_det) <= t_tour
model.solver()
print("Status:", LpStatus[model.status])
for v in model.variables():
    if v.varValue > 0:
        print(v.name, "=", v.varValue)
    else:
        print(v.name, "=", v.varValue)

'''https://proglib.io/p/lineynoe-programmirovanie-praktika-resheniya-zadach-optimizacii-na-python-2020-11-26
https://www.machinelearningmastery.ru/linear-programming-and-discrete-optimization-with-python-using-pulp-449f3c5f6e99/'''