from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable
import pandas as pd

df = pd.read_excel('C:\\Users\\oshurek_m\\Desktop\\Пеленг общий.xlsx', sheet_name='matmod')
df.info()
model = LpProblem('prod', LpMaximize)
names_det = list(df['Наименование детали'])
costs = dict(zip(names_det, df['Стоимость, $']))
print(costs)
'''https://proglib.io/p/lineynoe-programmirovanie-praktika-resheniya-zadach-optimizacii-na-python-2020-11-26
https://www.machinelearningmastery.ru/linear-programming-and-discrete-optimization-with-python-using-pulp-449f3c5f6e99/'''